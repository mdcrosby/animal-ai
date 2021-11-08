from animalai.envs.actions import AAIActions
import time

from animalai.envs.arena_config import ArenaConfig
from animalai.envs.environment import AnimalAIEnvironment
from animalai.envs.braitenberg import Braitenberg

def run_agent_single_config(configuration_file: str) -> None:
    """
    Loads a configuration file for a single arena and gives some example usage of mlagent python Low Level API
    See https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Python-API.md for details.
    For demo purposes uses a simple braitenberg vehicle-inspired agent that solves most tasks from category 1.
    """
    env_path = "env/AnimalAI"
    
    configuration = ArenaConfig(configuration_file)

    totalRays = 11
    # Start the environment using the custom AnimalAI scripts to pass configuration and options
    env = AnimalAIEnvironment(
        file_name=env_path,
        arenas_configurations=configuration,
        seed = 0, # random.randint(0, 1000000),
        play=False,
        useCamera=True,
        resolution=84,
        useRayCasts=True,
        raysPerSide=int((totalRays-1)/2),
        # decisionPeriod=3, #The number of Academy steps before the agent is asked for a new action
        rayMaxDegrees = 30,
    )

    env.reset()
 
    # braitenbergAgent = Braitenberg(totalRays) #A simple BraitenBerg Agent that heads towards food items.

    behavior = list(env.behavior_specs.keys())[0] # by default should be AnimalAI?team=0

    # # # # # # # # # #
    # # Observation examples
    # obs = (env.get_steps(behavior)[0].obs)
    # print(obs)
    # o = env.getDict(obs)
    # print(o["camera"])
    # print(o["rays"])
    # print("health: " + str(o["health"]))
    # print("velocity: " + str(o["velocity"]))
    # print("position: " + str(o["position"]))
    # sys.exit()
    # # # # # # # # # #

    actions = AAIActions()

    totalreward = 0
    while(True): #Run a single episode with the Braitenberg-style agent
        dec, term = env.get_steps(behavior)
        if len(term) > 0: #the episode has ended
            totalreward += term.reward
            print("Episode reward: " + str(totalreward))
            break
        totalreward += dec.reward #update the reward
        # raycasts = env.getDict(dec.obs)["rays"] # Get the raycast data
        # print(braitenbergAgent.prettyPrint(raycasts)) #print raycasts in more readable format
        # action = braitenbergAgent.get_action(raycasts)
        action = actions.random()
        env.set_actions(behavior, action.action_tuple)
        env.step()
       
# Loads a random competition configuration unless a link to a config is given as an argument.
if __name__ == "__main__":
    start = time.time()
    run_agent_single_config("configs/tests/allobjs-10000.yml")
    end = time.time()
    print("fps: " + str(int(10000/(end-start))))