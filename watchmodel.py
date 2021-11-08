from stable_baselines3 import PPO
import torch as th

import sys
import random
import os
from stable_baselines3.common.vec_env.dummy_vec_env import DummyVecEnv
from gym_unity.envs import UnityToGymWrapper
from animalai.envs.arena_config import ArenaConfig
from animalai.envs.environment import AnimalAIEnvironment

def train_agent_single_config(configuration_file):
    
    training = False #Set to false to watch the agent. 
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
        useRayCasts=True,
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
    # env = UnityToGymWrapper(aai_env, uint8_visual=False, allow_multiple_obs=True, flatten_branched=True)
    env = UnityToGymWrapper(aai_env, uint8_visual=False, allow_multiple_obs=True, flatten_branched=True)
    runname = "megacourse2" #megacourse2

    model = PPO.load("results/"  + runname + "/model_1800000")
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
