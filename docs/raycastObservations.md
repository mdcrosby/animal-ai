# Agent Observations

This page details the observations available to the agent. Currently only the Raycast observations are covered in detail.

## Camera Observations

With the camera enabled (via useCamera) the agent receives 1st-person pixel observations of its environment with configurable resolution.

## Raycast observations

Raycasts are implemented to make it easier to work with a wide range of algorithms within AnimalAI. They are not designed to compete with pixel inputs as they naturally contain much less information about the environment. Nevertheless, they can be extremely useful for protyping and for testing certain cognitive abilities such as episodic memory or when analysing network dynamics compared to performance on many tasks. 


There are four relevant arguments to pass to the environment when using raycasts. See the lowLevelAPI.py script for examples.
* useCamera: set to false if you do not also want pixel observations
* useRayCasts: set to true to use raycast observations
* raysPerSide: sets the number of rays to cast to the left and right of the central one. e.g raysPerSide=2 means 5 rays total
* rayMaxDegrees: sets the maximum degrees for the left/right rays. e.g. 90 means the agent casts rays exactly to the left and right. other rays are spaced equally between the center and the max.

There are currently 5 types of objects that the rays report. This is intentional to keep the observation space down, but does limit the types of problem solvable. In order they are:
* arena: this is the outside of the arena and should usually be hit by a ray if it misses other objects (this is useful for the distance)
* Immovable: Inner Walls, Cylinders, ramps i.e. all the objects listed under immovable [here](definitionsOfObjects.md)
* Movable: Cardboxes and L/U objects i.e. all the objects listed as movable [here](definitionsOfObjects.md)
* goodGoal: A green goal
* goodGoalMulti: A yellow goal
* badGoal: Both red goals and death zones.

Note that this means that ramps and transparent objects are not distinguished from opaque walls, thus limiting the number of tasks it is possible for a raycast only agent to solve. 

For each ray:
* The first 6 elements of the returned observation are a one-hot vector for the type of object hit (ordered as above).
* The next element is 0 if the ray hit something (1 otherwise).
* The next element is the normalised distance to the object that was hit.

So the full observation space is of size 8 * (2*raysPerSide + 1)

## Velocity and Position

The agent also receives a vector of length 6 containing its velocity and (global) position.