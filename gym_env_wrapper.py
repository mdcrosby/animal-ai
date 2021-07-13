import numpy as np 
import gym 
from gym import spaces
import random
from mlagents_envs.base_env import ActionTuple
from animalai.envs.arena_config import ArenaConfig
from animalai.envs.environment import AnimalAIEnvironment

def format_observation(observation, rays = 3): 
    num_rays = 2*rays + 1
    for i in range(len(observation)):
        # removes immovable, movable, badGoal from observations (irrelevant for current task) 
        if i == 0:
            observation[i] = observation[i].reshape(8, num_rays)
            observation[i] = np.delete(observation[i], [1, 2, 5], axis = 0)
        observation[i] = np.array(observation[i]).flatten()
    observation = np.hstack(observation)
    return observation

class AnimalAIGym(gym.Env): 
    def __init__(self, config, use_cam = False, use_rays = True, rays = 3, frame_skips = 5, res = 84, use_vel=True, **kwargs):
        super(AnimalAIGym, self).__init__()
        self.config = config
        self.configuration = ArenaConfig(self.config)
        self.rays = rays
        self.env = AnimalAIEnvironment(
                file_name = "env/AnimalAI",
                base_port = 5005 + random.randint(0, 100),
                arenas_configurations = self.configuration,
                play = False,
                useCamera = use_cam,
                useRayCasts = use_rays,
                raysPerSide = rays, 
            )
        n_actions = 9
        self.action_space = spaces.Discrete(9)
        obs_shape = 0
        if use_cam:
            obs_shape += res*res*3
        if use_rays:
            obs_shape += 5 * (2*rays + 1)
        if use_vel:
            obs_shape += 6
        self.observation_space = spaces.Box(low=-50, high=50, shape=(obs_shape,))
        self.behavior = list(self.env.behavior_specs.keys())[0]
        self.action_dict = {0: [0,0], 1:[0,2], 2:[0,1], 3:[1,0], 4:[1,2], 5:[1,1], 6:[2,0], 7:[2,2], 8:[2,1]}
        self.prev_observation = None
        self.frame_skips = frame_skips

    def reset(self):
        self.configuration = ArenaConfig(self.config)
        self.env.reset(arenas_configurations = self.configuration)
        decision_steps, terminal_steps = self.env.get_steps(self.behavior)
        observation = decision_steps.obs 
        observation = format_observation(observation, self.rays)
        self.prev_observation = observation
        return observation

    def step(self, action):
        # TODO: implement frame_skips
        action = self.action_dict.get(action)
        action = np.array([action], dtype = np.int32)
        action_tuple = ActionTuple(discrete = action)
        self.env.set_actions(self.behavior, action_tuple)
        reward = 0
        for i in range(self.frame_skips-1):
            self.env.step()
            decision_steps, terminal_steps = self.env.get_steps(self.behavior)
            interrupt = terminal_steps.interrupted
            if len(interrupt) == 0:
                reward += float(decision_steps.reward[0])
            else:
                

        return observation, reward, done, {}

    def close(self):
        self.env.close()
                
