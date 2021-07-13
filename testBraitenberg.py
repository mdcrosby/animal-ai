import sys
import os
import datetime

from animalai.envs.actions import AAIActions
from animalai.envs.arena_config import ArenaConfig
from animalai.envs.environment import AnimalAIEnvironment
from animalai.envs.braitenberg import Braitenberg

def testOnAllConfigs() -> None:
    """
    Runs the braitenberg agent on all config files and saves results
    """
    env_path = "env/AnimalAI"
    competition_folder = "configs/competition/"
    configuration_files = os.listdir(competition_folder)
    #sort the files alphabetically
    configuration_files.sort()
    rewards = []

    port = 5000
    for config in configuration_files:
        configuration = ArenaConfig(competition_folder + config)
        totalRays = 11
        port = port + 1
        # Start the environment using the custom AnimalAI scripts to pass configuration and options
        env = AnimalAIEnvironment(
            file_name=env_path,
            base_port=port,
            arenas_configurations=configuration,
            play=False,
            useCamera=False,
            # resolution=84, # not needed without camera
            useRayCasts=True,
            raysPerSide=int((totalRays-1)/2),
            rayMaxDegrees = 30,
            targetFrameRate= 60,
            captureFrameRate = 60, #Set this so the output on screen is visible - set to 0 for faster training but no visual updates
        )
        # acts = AAIActions() # Helper to reference actions directly (you probably won't need this).
        braitenbergAgent = Braitenberg(totalRays) #A simple BraitenBerg Agent that heads towards food items.
        env.reset()
        behavior = list(env.behavior_specs.keys())[0] # by default should be AnimalAI?team=0
        # print(env.get_steps(behavior)[0].obs) #print out the observations

        totalreward = 0
        while(True): #Run a single episode with the Braitenberg-style agent
            dec, term = env.get_steps(behavior)
            if len(term) > 0: #the episode has ended
                totalreward += term.reward
                out = config + ": " + str(totalreward) + "\n"
                print(out)
                rewards.append(out)
                break
            totalreward += dec.reward #update the reward
            raycasts = dec.obs[0][0] # Get the raycast data
            # print(braitenbergAgent.prettyPrint(raycasts)) #print raycasts in more readable format
            action = braitenbergAgent.get_action(raycasts)
            env.set_actions(behavior, action.action_tuple)
            env.step()
        env.close()
    
    #writes the rewards to a file with current date/time
    file_name = "testresults/braitenberg-" + str(datetime.datetime.now()) + ".txt"
    with open("file_name", "w") as file:
        for reward in rewards:
            file.write(reward)

testOnAllConfigs()