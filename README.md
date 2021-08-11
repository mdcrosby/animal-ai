# Animal-AI 3 (BETA)

AAI supports interdisciplinary research to help better understand human, animal, and artificial cognition. It also supports AI research towards unlocking cognitive capabilities and will also help track progress towards those with societal implications.

| ![](figs/animal-cyl-fail.gif) | ![](figs/agent-cyl-fail.gif) |
|---|---|
| ![](figs/animal-cyl-pass.gif) | ![](figs/agent-cyl-pass.gif) |

## Version

The environment will be undergoing heavy development over the next few years. Currently on version 2.2.2 you can see the roadmap towards the next major release [here](docs/roadMap.md).

## This Repo

This repo contains some introductory python scripts for interacting with the training environment as well as the [900 tasks](competition_configurations) which were used in the original Animal-AI Olympics competition. Details of the tasks can be found on the [AAI website](http://animalaiolympics.com/AAI/testbed) where they can also be played and competition entries watched. More tutorials and documentation (as well as environment features) will be added as we approach 3.0.

The environment is built using [Unity ml-agents](https://github.com/Unity-Technologies/ml-agents/tree/master/docs) release 2 (python package 0.26.0).

## Requirements

First **download the environment** for your system:

| OS | Environment link | Old Versions |
| --- | --- | --- |
| Linux |  [v2.2.3](https://www.doc.ic.ac.uk/~mcrosby/aai_builds/AnimalAI_LINUX_2.2.3.zip) | [v2.2.2](https://www.doc.ic.ac.uk/~mcrosby/aai_builds/AnimalAI_LINUX_2.2.2.zip), [v2.2.1](https://www.doc.ic.ac.uk/~mcrosby/aai_builds/AnimalAI_LINUX_2.2.1.zip), [v2.2.0](https://www.doc.ic.ac.uk/~mcrosby/aai_builds/AnimalAI_LINUX_2.2.0.zip), [v2.1.1](https://www.doc.ic.ac.uk/~mcrosby/aai_builds/AnimalAI_LINUX_2.1.1.zip), [v2.1](https://www.doc.ic.ac.uk/~mcrosby/aai_builds/AnimalAI_LINUX_2.1.zip) |
| Mac | [v2.2.3](https://www.doc.ic.ac.uk/~mcrosby/aai_builds/AnimalAI_MAC_2.2.3.zip) | [v2.2.2](https://www.doc.ic.ac.uk/~mcrosby/aai_builds/AnimalAI_MAC_2.2.2.zip), [v2.2.1](https://www.doc.ic.ac.uk/~mcrosby/aai_builds/AnimalAI_MAC_2.2.1.zip) [v2.2.0](https://www.doc.ic.ac.uk/~mcrosby/aai_builds/AnimalAI_MAC_2.2.0.zip), [v2.1.1](https://www.doc.ic.ac.uk/~mcrosby/aai_builds/AnimalAI_MAC_2.1.1.zip), [v2.1](https://www.doc.ic.ac.uk/~mcrosby/aai_builds/AnimalAI_MAC_2.1.zip) |
| Windows | [v2.2.3](https://www.doc.ic.ac.uk/~mcrosby/aai_builds/AnimalAI_WINDOWS_2.2.3.zip) | [v2.2.2](https://www.doc.ic.ac.uk/~mcrosby/aai_builds/AnimalAI_WINDOWS_2.2.2.zip), [v2.2.1](https://www.doc.ic.ac.uk/~mcrosby/aai_builds/AnimalAI_WINDOWS_2.2.1.zip) [v2.2.0](https://www.doc.ic.ac.uk/~mcrosby/aai_builds/AnimalAI_WINDOWS_2.2.0.zip), [v2.1.1](https://www.doc.ic.ac.uk/~mcrosby/aai_builds/AnimalAI_WINDOWS_2.1.1.zip), [v2.1](https://www.doc.ic.ac.uk/~mcrosby/aai_builds/AnimalAI_WINDOWS_2.1.zip) |

Unzip the **entire content** of the archive to the `env` folder. On linux you may have to make the file executable by running `chmod +x env/AnimalAI.x86_64`. Note that the env folder should contain the AnimalAI.exe/.x86_84/.app depending on your system and *any other folders* in the same directory in the zip file.

The Animal-AI environment and packages are currently only tested on linux with python 3.8 but should also work on Windows and Mac.

**The Unity Project** for the environment will be made available later. If you would like access for your research please get in contact. 

## Manual Control

If you launch the environment directly from the executable or through the `play_config.py` script it will launch
 in player mode. Here you can control the agent with the following:

| Keyboard Key  | Action    |
| --- | --- |
| W   | move agent forwards |
| S   | move agent backwards|
| A   | turn agent left     |
| D   | turn agent right    |
| C   | switch camera       |
| R   | reset environment   |

## While Still in Beta

For now many of the documentation from [version 2](https://github.com/beyretb/AnimalAI-Olympics) may be a useful reference until everything is fully migrated and updated. Further the documentation for [mlagents](https://github.com/Unity-Technologies/ml-agents) is very good and includes a lot of useful examples.

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

## Version History

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
