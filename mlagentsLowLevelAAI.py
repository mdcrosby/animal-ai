import sys
import random
import os

from animalai.envs.arena_config import ArenaConfig
from animalai.envs.environment import AnimalAIEnvironment

"""

"""

def load_config_and_play(configuration_file: str) -> None:
    """
    Loads a configuration file for a single arena and lets you play manually
    :param configuration_file: str path to the yaml configuration
    :return: None
    """
    env_path = "env/AnimalAI"
    port = 5005 + random.randint(
        0, 100
    )  # use a random port to allow relaunching the script rapidly
    configuration = ArenaConfig(configuration_file)

    print("initializaing AAI environment")
    env = AnimalAIEnvironment(
        file_name=env_path,
        base_port=port,
        arenas_configurations=configuration,
        play=False,
    )
    env.reset()
    behaviour_names=list(env.behavior_specs.keys())
    print(behaviour_names[0])
    print(env.get_steps("AnimalAI?team=0")[0].obs)

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
    load_config_and_play(configuration_file=configuration_file)
