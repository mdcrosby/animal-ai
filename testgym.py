from mlagents_envs.environment import UnityEnvironment
from gym_unity.envs import UnityToGymWrapper


env = UnityEnvironment(file_name="env/AnimalAI", seed=1, side_channels=[])
gymenv = UnityToGymWrapper(env, use_visual=True)
