from stable_baselines3 import PPO
from stable_baselines3 import DQN
import torch as th

import sys
import random
import os
from stable_baselines3.common.vec_env.dummy_vec_env import DummyVecEnv
from gym_unity.envs import UnityToGymWrapper
from animalai.envs.arena_config import ArenaConfig
from animalai.envs.environment import AnimalAIEnvironment

def train_agent_single_config(configuration_file):
    
    training = True #Set to false to watch the agent. 
    targetFrameRate = -1 if training else 60
    captureFrameRate = 0 if training else 60
    base_port = 5000 if training else 5001
    inference = not training

    aai_env = AnimalAIEnvironment(
        seed = 123,
        file_name="env/AnimalAI",
        arenas_configurations=ArenaConfig(configuration_file),
        play=False,
        base_port=base_port,
        inference=inference, #Set true when watching the agent
        useCamera=True,
        resolution=36,
        useRayCasts=False,
        raysPerSide=1,
        rayMaxDegrees = 30,
    )

    # env = UnityToGymWrapper(aai_env, uint8_visual=False, allow_multiple_obs=True, flatten_branched=False)
    # def make_env():
    #     def _thunk():
    #         env = UnityToGymWrapper(aai_env, uint8_visual=False, allow_multiple_obs=True, flatten_branched=True)
    #         return env
    #     return _thunk
    # env = DummyVecEnv([make_env()])
    env = UnityToGymWrapper(aai_env, uint8_visual=True, allow_multiple_obs=False, flatten_branched=True)
    runname = "puretest"

    if training:
        policy_kwargs = dict(activation_fn=th.nn.ReLU)
        model = DQN("CnnPolicy", env, policy_kwargs=policy_kwargs, verbose=1, tensorboard_log=("./ppo_tensorboard/" + runname))

        reset_num_timesteps = True
        for i in range(1000):
            model.learn(100000, reset_num_timesteps=reset_num_timesteps) #100,000 * 1,000 = 100,000,000
            model.save("results/" + runname + "/model_" + str( (i+1)*100000 ))
            reset_num_timesteps = False

    else:

        model = DQN.load("results/"  + runname + "/model_1800000")
        obs = env.reset()
        while True:
            action, _states = model.predict(obs, deterministic=True)
            obs, reward, done, info = env.step(action)
            # print(obs)
            env.render()
            if done:
                obs=env.reset()
        env.close()

    
# Loads a random competition configuration unless a link to a config is given as an argument.
if __name__ == "__main__":
    if len(sys.argv) > 1:
        configuration_file = sys.argv[1]
    else:   
        competition_folder = "configs/competition/"
        configuration_files = os.listdir(competition_folder)
        configuration_random = random.randint(0, len(configuration_files))
        configuration_file = (
            competition_folder + configuration_files[configuration_random]
        )
    train_agent_single_config(configuration_file=configuration_file)
