from animalai.envs.actions import AAIActions
from dis import dis
import sys
import random
import os
import numpy as np
import time

from mlagents_envs.base_env import ActionTuple

from animalai.envs.arena_config import ArenaConfig
from animalai.envs.environment import AnimalAIEnvironment

"""

"""

def load_config(configuration_file: str) -> None:
    """
    Loads a configuration file for a single arena and gives examples usage of mlagent python Low Level API
    See https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Python-API.md for details.
    """
    env_path = "env/AnimalAI"
    
    port = 5005 + random.randint(
        0, 100
    )  # use a random port so (probably) do not need to wait for previous to close if need to relaunch
    
    configuration = ArenaConfig(configuration_file)

    # Start the environment using the custom AnimalAI scripts to pass configuration and options
    env = AnimalAIEnvironment(
        file_name=env_path,
        base_port=port,
        arenas_configurations=configuration,
        play=False,
        useCamera=False,
        # resolution=84,
        useRayCasts=True,
        raysPerSide=1,
        rayMaxDegrees = 30,
        targetFrameRate= 60,
        captureFrameRate = 60, #Set this so the output on screen is visible - set to 0 for faster training but no visual updates
    )
   
    env.reset()

    #list the behaviour name (by default should be AnimalAI?team=0    
    behavior = list(env.behavior_specs.keys())[0]
    print(behavior)
    acts = AAIActions() # Easier to use actions directly 
    
    # print out the observations from the environment
    # will depend on the options selected for camera and raycasts
    # will always include velocity and position
    # print(env.get_steps(behavior)[0].obs) 
    totalreward = 0

    while(True): #Run a single episode with the agent just moving forwards.
        dec, term = env.get_steps(behavior)
        totalreward += dec.reward #update the reward
        if len(term) > 0: #the episode has ended
            print(totalreward)
            break
        env.set_actions(behavior, acts.FORWARDS)
        env.step()
       

        


# Loads a random competition configuration unless a link to a config is given as an argument.
if __name__ == "__main__":
    if len(sys.argv) > 1:
        configuration_file = sys.argv[1]
    else:
        competition_folder = "competition_configurations/"
        configuration_files = os.listdir(competition_folder)
        configuration_random = random.randint(0, len(configuration_files))
        configuration_file = (
            competition_folder + configuration_files[configuration_random]
        )
    load_config(configuration_file=configuration_file)
