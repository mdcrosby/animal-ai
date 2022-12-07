# Deprecated - New Home [Here](https://github.com/Kinds-of-Intelligence-CFI/animal-ai).

:bangbang: :no_entry: THIS REPOSITORY IS NO LONGER BEING MAINTAINED OR MONITORED. :no_entry: :bangbang:

We have relocated this repository to a [new home](https://github.com/Kinds-of-Intelligence-CFI/animal-ai). Further updates and releases will be published there.


~
~


# AnimalAI 3

AAI supports interdisciplinary research to help better understand human, animal, and artificial cognition. It aims to support AI research towards unlocking cognitive capabilities and better understanding the space of possible minds. It is designed to facilitate testing across animals, humans, and AI.

| ![](docs/figs/animal-cyl-fail.gif) | ![](docs/figs/agent-cyl-fail.gif) |
|---|---|
| ![](docs/figs/animal-cyl-pass.gif) | ![](docs/figs/agent-cyl-pass.gif) |

## This Repo

This repo contains the AnimalAI environment, some introductory python scripts for interacting with it, as well as the [900 tasks](competition_configurations) which were used in the original Animal-AI Olympics competition (and some others for demonstration purposes). Details of the tasks can be found on the [AAI website](http://animalaiolympics.com/AAI/testbed) where they can also be played and competition entries watched.

The environment is built using [Unity ml-agents](https://github.com/Unity-Technologies/ml-agents/tree/master/docs) release 2.1.0-exp.1 (python version 0.27.0).

The AnimalAI environment and packages are currently only tested on linux (Ubuntu 20.04.2 LTS) with python 3.8 but have been reported working with python 3.6+, other linux distros and Windows and Mac.

**The Unity Project** for the environment is available [here](https://github.com/mdcrosby/animal-ai-unity-project).


## Quick Install

*see [here](docs/installationGuide.md) for a more detailed installation guide, including information on Python/pip/conda and using the command line during installation*

To get started you will need to:
1. Clone this repo.
2. **Install the animalai python package** and requirements by running `pip install -e animalai` from the root folder.
3. **Download the environment** for your system:

| OS | Environment link |
| --- | --- |
| Linux |  [v3.0.1](https://kv301.user.srcf.net/wp-content/uploads/2022/04/AAI_v3.0.1_build_linux_090422.zip) |
| Mac | [v3.0.1](https://kv301.user.srcf.net/wp-content/uploads/2022/04/AAI_v3.0.1_build_macOS_090422.zip) |
| Windows | [v3.0.1](https://kv301.user.srcf.net/wp-content/uploads/2022/04/AAI_v3.0.1_build_windows_090422.zip) |

(Old v2.x versions can be found [here](docs/oldVersions.md))

Unzip the **entire content** of the archive to the (initially empty) `env` folder. On linux you may have to make the file executable by running `chmod +x env/AnimalAI.x86_64`. Note that the env folder should contain the AnimalAI.exe/.x86_84/.app depending on your system and *any other folders* in the same directory in the zip file.

## Tutorials and Examples

Some example scripts to get started can be found in the `examples` folder. The following docs provide information for some common uses of the environment.

- [Getting started with the environment](docs/quickStart.md)
- [Using the ML-Agents Low-Level API: A hand-coded Braitenberg Vehicle baseline](docs/lowLevelAPI.md)
- [Designing Experiments](docs/configFile.md)
- [Training examples](docs/training.md)

## Manual Control

If you launch the environment directly from the executable or through the `play.py` script it will launch in player mode. Here you can control the agent with the following:

| Keyboard Key  | Action    |
| --- | --- |
| W   | move agent forwards |
| S   | move agent backwards|
| A   | turn agent left     |
| D   | turn agent right    |
| C   | switch camera       |
| R   | reset environment   |

## Citing
If you use the Animal-AI environment in your work you can cite the environment paper:

 Crosby, M., Beyret, B., Shanahan, M., Hernández-Orallo, J., Cheke, L. & Halina, M.. (2020). The Animal-AI Testbed and Competition. Proceedings of the NeurIPS 2019 Competition and Demonstration Track, in Proceedings of Machine Learning Research 123:164-176 Available [here](http://proceedings.mlr.press/v123/crosby20a.html).
```
 @InProceedings{pmlr-v123-crosby20a, 
    title = {The Animal-AI Testbed and Competition}, 
    author = {Crosby, Matthew and Beyret, Benjamin and Shanahan, Murray and Hern\'{a}ndez-Orallo, Jos\'{e} and Cheke, Lucy and Halina, Marta}, 
    booktitle = {Proceedings of the NeurIPS 2019 Competition and Demonstration Track}, 
    pages = {164--176}, 
    year = {2020}, 
    editor = {Hugo Jair Escalante and Raia Hadsell}, 
    volume = {123}, 
    series = {Proceedings of Machine Learning Research}, 
    month = {08--14 Dec}, 
    publisher = {PMLR}, 
} 
```

## Unity ML-Agents

The Animal-AI Olympics was built using [Unity's ML-Agents Toolkit.](https://github.com/Unity-Technologies/ml-agents)

Juliani, A., Berges, V., Vckay, E., Gao, Y., Henry, H., Mattar, M., Lange, D. (2018). [Unity: A General Platform for 
Intelligent Agents.](https://arxiv.org/abs/1809.02627) *arXiv preprint arXiv:1809.02627*

Further the documentation for [mlagents](https://github.com/Unity-Technologies/ml-agents) should be consulted if you want to make any changes.

## Version History

- v3.0.1
  - Added Agent Freezing Parameter, enabling you to freeze the agent for no reward decrement at the start of an episode, while other objects continue to move around.
- v3.0 **Note that due to the changes to controls and graphics agents trained on previous versions might not preform the same**
  - Updated agent handling. The agent now comes to a stop more quickly when not moving forwards or backwards and accelerates slightly faster.
  - Added new objects, spawners, signs, goal types (see [doc](docs/definitionsOfObjects.md)) 
  - Added 3 animal skins to the player character.
  - Updated graphics for many objects. Default shading on many previously plain objects make it easier to determine location(s)/velocity.
  - Made the Unity Environment available (see link on main page).
  - Many improvements to documentation and examples.
  - Upgraded to Mlagents 2.1.0-exp.1 (ml-agents python version 0.27.0)
  - Fixed various bugs.
- v2.2.3
  - Now you can specify multiple different arenas in a single yml config file ant the environment will cycle through them each time it resets
- v2.2.2 
  - Low quality version with improved fps. (will work on further improvments to graphics & fps later)
- v2.2.1
  - Improve UI scaling wrt. screen size
  - Fixed an issue with cardbox objects spawning at the wrong sizes
  - Fixed an issue where the environment would time out after the time period even when health > 0 (no longer intended behaviour)
  - Improved Death Zone shader for weird Zone sizes
- v2.2.0 Health and Basic Scripts
  - Switched to health-based system (rewards remain the same).
  - Updated overlay in play mode.
  - Allow 3D hot zones and death zones and make them 3D by default in old configs.
  - Added rewards that grow/decay (currently not configurable but will be added in next update).
  - Added basic Gym Wrapper.
  - Added basic heuristic agent for benchmarking and testing.
  - Improved all other python scripts.
  - Fixed a reset environment bug when resetting during training.
  - Added the ability to set the DecisionPeriod (frameskip) when instantiating and environment.
- v2.1.1 bugfix
  - Fixed raycast length being less then diagonal length of standard arena
- v2.1 beta release
  - Upgraded to ML-Agents release 2 (0.26.0)
  - New features
    - Added raycast observations
    - Added agent global position to observations

### Notice

   Copyright 2022 Matthew Crosby
   
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
