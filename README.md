# Animal-AI 3.0.0

<p align="center">
  <img height="300" src="figs/steampunkFOURcrop.png">
</p>


| ![](figs/animal-cyl-fail.gif) | ![](figs/agent-cyl-fail.gif) |
|---|---|
| ![](figs/animal-cyl-pass.gif) | ![](figs/agent-cyl-pass.gif) |

## Overview

The [Animal-AI Testbed](http://animalaiolympics.com/AAI) is used to study the cognitive abilities of artificial agents and provides research tools for building AI systems with the common sense physical reasoning abilities found in many animals, but that are not required to solve many existing AI benchmarks.

The environment will be undergoing heavy development over the next few years. This initial 3.0.0 release is designed to be as backwards compatible as possible with the old version. Internally, AAI has been rewritten, but externally it should look roughly the same. The only new features (for now) are adding agent global location and the ability for raycasting. Future releases plan to include a flag to be compatible with the 3.0.0 version, but, due to the large number of changes planned, it is likely that exact continuity between releases will not be maintained.

This repo contains the [training environment](animalai), a [training library](animalai_train) as well as [900 tasks](competition_configurations) which were used in the original Animal-AI Olympics competition. Details of the tasks can be found on the [AAI website](http://animalaiolympics.com/AAI/testbed) where they can also be played and competition entries watched.

The environment is built using [Unity ml-agents](https://github.com/Unity-Technologies/ml-agents/tree/master/docs). This version uses release 1 (0.16.1). In the future we will upgrade to release 2.

## Requirements

First **download the environment** for your system:

| OS | Environment link |
| --- | --- |
| Windows | TODO |
| Mac | TODO |
| Linux |  TODO |

Unzip the **entire content** of the archive to the `examples/env` folder. On linux you may have to make the file executable by running `chmod +x env/AnimalAI.x86_64`.

The Animal-AI packages are currently only tested on linux with python 3.8

**The Unity source files** for the environment will be made available later. If you need them for your research please get in contact. 

## Manual Control

If you launch the environment directly from the executable or through the `load_config_and_play,py` script it will launch
 in player mode. Here you can control the agent with the following:

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

## Version History

- v3.0.0: 
  - initial release
  - New features
    - Added raycast observations
    - Added agent global position to observations
  - Upgraded to ML-Agents release 1 (0.16.1)
    
