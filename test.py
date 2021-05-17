import sys
import random
import os

from mlagents_envs.environment import UnityEnvironment
# from animalai.envs.arena_config import ArenaConfig
# from animalai.envs.environment import AnimalAIEnvironment

"""

"""

env = UnityEnvironment(file_name="mlenvs/WallJump", seed=1, side_channels=[])


# def load_config_and_play(configuration_file: str) -> None:
#     """
#     Loads a configuration file for a single arena and lets you play manually
#     :param configuration_file: str path to the yaml configuration
#     :return: None
#     """
#     env_path = "env/AnimalAI"
#     # env_path = "mlenvs/WallJump"
#     port = 5005 + random.randint(
#         0, 100
#     )  # use a random port to allow relaunching the script rapidly
#     configuration = ArenaConfig(configuration_file)

#     environment = UnityEnvironment(
#         file_name=env_path,
#         base_port=port,
#         # arenas_configurations=configuration,
#         # play=True,
#     )
#     environment.reset()
#     # try:
#     #     while environment.proc1:
#     #         continue
#     # except KeyboardInterrupt:
#     #     pass
#     # finally:
#     #     environment.close()

# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         configuration_file = sys.argv[1]
#     else:
#         competition_folder = "competition_configurations/"
#         configuration_files = os.listdir(competition_folder)
#         configuration_random = random.randint(0, len(configuration_files))
#         configuration_file = (
#             competition_folder + configuration_files[configuration_random]
#         )
#     load_config_and_play(configuration_file=configuration_file)
