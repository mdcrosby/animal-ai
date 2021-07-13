from stable_baselines3 import PPO

import sys
import random
import os

from gym_unity.envs import UnityToGymWrapper
from animalai.envs.arena_config import ArenaConfig
from animalai.envs.environment import AnimalAIEnvironment

def train_agent_single_config(configuration_file):
    
    aai_env = AnimalAIEnvironment(
        file_name="env/AnimalAI",
        arenas_configurations=ArenaConfig(configuration_file),
        play=False,
        useCamera=False,
        # resolution=32,
        useRayCasts=True,
        raysPerSide=5,
        rayMaxDegrees = 30,
        targetFrameRate= 60,
        captureFrameRate = 60, #Set this so the output on screen is visible - set to 0 for faster training but no visual updates
    )
    
    env = UnityToGymWrapper(aai_env, uint8_visual=False, allow_multiple_obs=False, flatten_branched=True)

    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=1000000)

    obs = env.reset()
    for i in range(1000):
        action, _states = model.predict(obs, deterministic=True)
        obs, reward, done, info = env.step(action)
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