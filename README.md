# Animal-AI 3 (BETA)

<p align="center">
  <img height="300" src="figs/steampunkFOURcrop.png">
</p>

## Overview

The [Animal-AI Testbed](http://animalaiolympics.com/AAI) is used to study the cognitive abilities of artificial agents. It provides a research environment to help build and test AI systems with the common sense physical reasoning abilities found in many animals. Most modern AI benchmarks are solvable without common sense reasoning whereas Animal-AI is designed to isolate and measure such abilities.

| ![](figs/animal-cyl-fail.gif) | ![](figs/agent-cyl-fail.gif) |
|---|---|
| ![](figs/animal-cyl-pass.gif) | ![](figs/agent-cyl-pass.gif) |

## Version

The environment will be undergoing heavy development over the next few years. This initial Beta release is designed to work just like the old version. The only new features are upgrading to MLAgents 2.0 and adding agent global location and raycasts to the observation space. Due to the large number of changes planned, it is unlikely that exact continuity between releases will be maintained going forwards.

## This Repo

This repo contains some introductory python scripts for interacting with the training environment as well as the [900 tasks](competition_configurations) which were used in the original Animal-AI Olympics competition. Details of the tasks can be found on the [AAI website](http://animalaiolympics.com/AAI/testbed) where they can also be played and competition entries watched. More tutorials and documentation (as well as environment features) will be added as we approach 3.0.0.

The environment is built using [Unity ml-agents](https://github.com/Unity-Technologies/ml-agents/tree/master/docs). This version uses release 2 (python package 0.26.0).

## Requirements

First **download the environment** for your system:

**Environments for Linux, Windows, and Mac can be found [here](https://drive.google.com/drive/folders/1CkqmZ_rxsvPa8aTS3qhllTvb9uDCjRvg?usp=sharing).**

Current version 3-0-0-a.

Unzip the **entire content** of the archive to the `env` folder. On linux you may have to make the file executable by running `chmod +x env/AnimalAI.x86_64`. Note that the env folder should contain the AnimalAI.exe/.x86_84/.app depending on your system and any other folders from the zip.

The Animal-AI environment and packages are currently tested on linux with python 3.8 but should also work on Windows and Mac.

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

## More to come with the official release.

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

- v3.0.0-a beta release
  - Upgraded to ML-Agents release 2 (0.26.0)
  - New features
    - Added raycast observations
    - Added agent global position to observations