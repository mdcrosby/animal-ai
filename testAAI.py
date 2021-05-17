import sys
import random
import os

from mlagents_envs.environment import UnityEnvironment
# from animalai.envs.arena_config import ArenaConfig
# from animalai.envs.environment import AnimalAIEnvironment

"""

"""

env = UnityEnvironment(file_name="env/AnimalAI", seed=1, side_channels=[])

print(env.get_behavior_names)
