from stable_baselines3 import PPO
import torch as th

import sys
import random
import os

from gym_unity.envs import UnityToGymWrapper
from animalai.envs.arena_config import ArenaConfig
from animalai.envs.environment import AnimalAIEnvironment

def train_agent_single_config(configuration_file):
    
    training = True #Set to false to watch the agent. 
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
        useCamera=False,
        # resolution=48,
        useRayCasts=True,
        raysPerSide=5,
        rayMaxDegrees = 60,
        targetFrameRate= targetFrameRate,
        captureFrameRate = captureFrameRate, #Set this so the output on screen is visible - set to 0 for faster training but no visual updates
    )
    
    env = UnityToGymWrapper(aai_env, uint8_visual=False, allow_multiple_obs=False, flatten_branched=True)

    if training:
        policy_kwargs = dict(activation_fn=th.nn.ReLU, net_arch=[dict(pi=[1024, 1024, 512], vf=[32,32])])
        model = PPO("CnnPolicy", env, policy_kwargs=policy_kwargs, verbose=1, tensorboard_log="./ppo_tensorboard/5-5-5-5_wall")

        reset_num_timesteps = True
        for i in range(1000):
            model.learn(100000, reset_num_timesteps=reset_num_timesteps)
            model.save("results/ppo_5-5-5-5_wall/model_" + str( (i+1)*100000 ))
            reset_num_timesteps = False

    else:
        model = PPO.load("results/ppo_5-5-5-5_wall/model_16000000")
        obs = env.reset()
        for i in range(10):
            action, _states = model.predict(obs, deterministic=True)
            obs, reward, done, info = env.step(action)
            print(obs)
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