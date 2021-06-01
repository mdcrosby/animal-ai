import sys
import random
import os

from animalai.envs.arena_config import ArenaConfig
from animalai.envs.environment import AnimalAIEnvironment

"""

"""

def load_config(configuration_file: str) -> None:
    """
    Loads a configuration file for a single arena and gives examples for using the Python Low Level API
    """
    env_path = "env/AnimalAI"
    port = 5005 + random.randint(
        0, 100
    )  # use a random port so (probably) do not need to wait for previous to close if need to relaunch
    configuration = ArenaConfig(configuration_file)

    print("initializaing AAI environment")
    env = AnimalAIEnvironment(
        file_name=env_path,
        base_port=port,
        arenas_configurations=configuration,
        play=False,
        useRayCasts=True,
    )

    # Below are sample methods from the Unity low level python API
    # See https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Python-API.md for details.
    
    env.reset()
    behaviour_names=list(env.behavior_specs.keys())
    print(behaviour_names[0])
    
    print(env.get_steps("AnimalAI?team=0")[0].obs)
    env.step()
    print(env.get_steps("AnimalAI?team=0")[0].obs)
    env.step()
    print(env.get_steps("AnimalAI?team=0")[0].obs)
    env.step()
    


# Loads a random competition configuration unless a link to the file system is used as an argument.
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
