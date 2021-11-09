import attr
import cattr

from typing import Optional, List, Dict, Any
from mlagents_envs.side_channel.side_channel import SideChannel
from mlagents.trainers.cli_utils import load_config
from mlagents.trainers.exception import TrainerConfigError

@attr.s(auto_attribs=True)
class AAIOptions():
    arenaConfig: str = attr.ib()
    useCamera: bool = attr.ib()
    resolution: int = attr.ib()
    grayscale: bool = attr.ib()
    useRayCasts: bool = attr.ib()
    raysPerSide: int = attr.ib()
    rayMaxDegrees: int = attr.ib()

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
