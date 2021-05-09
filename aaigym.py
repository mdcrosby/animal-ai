from mlagents_envs.environment import UnityEnvironment
from gym_unity.envs import UnityToGymWrapper

def main():
    unity_env = UnityEnvironment("./env/AnimalAI")
    env = UnityToGymWrapper(unity_env, use_visual=False, uint8_visual=True, allow_multiple_visual_obs=True)

if __name__ == '__main__':
    main()