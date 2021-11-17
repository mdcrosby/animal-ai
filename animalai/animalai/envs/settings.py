import attr
import cattr

from typing import Optional, List, Dict, Any
from mlagents_envs.side_channel.side_channel import SideChannel
from mlagents.trainers.cli_utils import load_config
from mlagents.trainers.exception import TrainerConfigError

@attr.s(auto_attribs=True)
class AAIOptions():
    """The options used by the animalai environment"""
    arenaConfig: str = attr.ib() #The path of a valid arena config yaml file
    useCamera: bool = attr.ib() #If true, then camera observations are returned
    resolution: int = attr.ib() #The (square) resolution of camera observations (if useCamera is true)
    grayscale: bool = attr.ib() #If the camera observations are grayscale or RGB
    useRayCasts: bool = attr.ib() #If true, then raycast observations are returned
    raysPerSide: int = attr.ib() #The number of rays on each side of the central ray (see observations doc)
    rayMaxDegrees: int = attr.ib() #The number of degrees between the central ray and furthest ray in each direction.

    @staticmethod
    def load_config(config_path) -> "AAIOptions":
        # Load YAML
        configured_dict: Dict[str, Any] = {
            "arenaConfig": {},
            "useCamera": {},
            "resolution": {},
            "grayscale": {},
            "useRayCasts": {},
            "raysPerSide": {},
            "rayMaxDegrees": {},
        }
        configured_dict.update(load_config(config_path))

        for key in configured_dict.keys():
            # Detect bad config options
            if key not in attr.fields_dict(AAIOptions):
                raise TrainerConfigError(
                    "The option {} was specified in your YAML file, but is invalid.".format(
                        key
                    )
                )
                
        return cattr.structure(configured_dict, AAIOptions)
