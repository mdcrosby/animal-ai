import numpy as np
from enum import Enum
from mlagents_envs.base_env import ActionTuple

class AAIActions():
    def __init__(self, no_agents=1):
        self.NOOP = ActionTuple(continuous=np.zeros((no_agents,0)), discrete=np.array([0,0], dtype=np.int32))
        self.LEFT = ActionTuple(continuous=np.zeros((no_agents,0)), discrete=np.array([0,2], dtype=np.int32))
        self.RIGHT = ActionTuple(continuous=np.zeros((no_agents,0)), discrete=np.array([0,1], dtype=np.int32))
        self.FORWARDS = ActionTuple(continuous=np.zeros((no_agents,0)), discrete=np.array([[1,0]], dtype=np.int32))
        self.FORWARDSLEFT = ActionTuple(continuous=np.zeros((no_agents,0)), discrete=np.array([1,2], dtype=np.int32))
        self.FORWARDSRIGHT = ActionTuple(continuous=np.zeros((no_agents,0)), discrete=np.array([1,1], dtype=np.int32))
        self.BACKWARDS = ActionTuple(continuous=np.zeros((no_agents,0)), discrete=np.array([2,0], dtype=np.int32))
        self.BACKWARDSLEFT = ActionTuple(continuous=np.zeros((no_agents,0)), discrete=np.array([2,2], dtype=np.int32))
        self.BACKWARDSRIGHT = ActionTuple(continuous=np.zeros((no_agents,0)), discrete=np.array([2,1], dtype=np.int32))