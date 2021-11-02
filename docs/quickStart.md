# Quick Start Guide

## Running the standalone arena

The basic environment contains a single agent in an enclosed arena. In this environment you can add objects the agents can interact with, as well as goals or rewards the agent must collect or avoid. To see what this looks like, you can run the executable environment directly. This will spawn an arena filled with randomly placed objects. Of course, this is a very messy environment to work with, so we provide many hand-designed configuration files that you can also use.

You can toggle the camera between first person, third person and Bird's eye view using the `C` key on your keyboard. The agent can then be controlled using `W,A,S,D` on your keyboard. Hitting `R` or collecting certain rewards (green or red) will reset the arena.

## Running and designing specific configurations

Once you are familiarized with the environment and its physics, you can start building and visualizing your own. Assuming you followed the [installation instruction](../README.md#requirements), go to the `examples/` folder and run `python play.py`. This loads a random configuration from the competition we ran in 2019.

Have a look at the [configuration files](../configs/competition) which specifies the objects to place. You can select objects, their size, location, rotation and color, randomizing any of these parameters as you like. For more details on the configuration options and syntax please read the relevant documentation:
 - The [configuration file documentation page](configFile.md) which explains how to write the configuration files.
 - The [definitions of objects page](definitionsOfObjects.md) which contains a detailed list of all the objects and their properties.

## Training an agent

The `animalai` package includes several features to help with this:

- You can define multiple arenas in a single configuration file and the agent will cycle through them as it learns.
- It is possible to **change the environment configuration between episodes** (allowing for techniques such as curriculum learning).
- You can **choose the length of each episode** as part of the configuration files, even having infinite episodes.