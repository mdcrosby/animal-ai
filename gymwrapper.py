import gym
import sys
import random
import os

from baselines import deepq
from baselines import logger

from mlagents_envs.environment import UnityEnvironment
from gym_unity.envs import UnityToGymWrapper

from animalai.envs.arena_config import ArenaConfig
from animalai.envs.environment import AnimalAIEnvironment

def main(configuration_file):
    
    aai_env = AnimalAIEnvironment(
        file_name="env/AnimalAI",
        arenas_configurations=ArenaConfig(configuration_file),
        play=False,
        useCamera=False,
        # resolution=84,
        useRayCasts=True,
        raysPerSide=1,
        rayMaxDegrees = 30,
        targetFrameRate= 60,
        captureFrameRate = 60, #Set this so the output on screen is visible - set to 0 for faster training but no visual updates
    )
    
    env = UnityToGymWrapper(aai_env, uint8_visual=True, allow_multiple_obs=True, flatten_branched=True)
    logger.configure('./logs') # Change to log in a different directory
    act = deepq.learn(
        env,
        "mlp",
        lr=2.5e-4,
        total_timesteps=1000000,
        buffer_size=50000,
        exploration_fraction=0.05,
        exploration_final_eps=0.1,
        print_freq=20,
        train_freq=5,
        learning_starts=20000,
        target_network_update_freq=50,
        gamma=0.99,
        prioritized_replay=False,
        checkpoint_freq=1000,
        checkpoint_path='./logs', # Change to save model in a different directory
        dueling=True
    )
    print("Saving model to unity_model.pkl")
    act.save("unity_model.pkl")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        configuration_file = sys.argv[1]
    else:
        competition_folder = "competition_configurations/"
        configuration_files = os.listdir(competition_folder)
        configuration_random = random.randint(0, len(configuration_files))
        configuration_file = (
            competition_folder + configuration_files[configuration_random]
        )
    main(configuration_file )
