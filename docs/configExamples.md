# Detailed examples

Let's take a look at some examples:

&nbsp;

### EXAMPLE 1 - Standard Parameters & Randomisation
```
!ArenaConfig
arenas:
  0: !Arena
    t: 0
    items:
    - !Item
      name: Wall
      positions:
      - !Vector3 {x: 10, y: 0, z: 10}
      - !Vector3 {x: -1, y: 0, z: 30}
      colors:
      - !RGB {r: 204, g: 0, b: 204 }
      rotations: [45]
      sizes:
      - !Vector3 {x: -1, y: 5, z: -1}
    - !Item
      name: CylinderTunnel
      colors:
      - !RGB {r: 204, g: 0, b: 204 }
      - !RGB {r: 204, g: 0, b: 204 }
      - !RGB {r: 204, g: 0, b: 204 }
    - !Item
      name: GoodGoal
```

First of all, we can see that the number of parameters for `positions`, `rotations` and `sizes` do not need to match. The environment will spawn `max( len(positions), len(rotations), len(sizes) )` objects, where `len()` is the length of the list. Except in special-parameter cases, any missing parameter will be assigned a randomly generated value.

In this case this will lead to (in order that they will spawn):
- a pink `Cube` spawned at `[10,10]` on the ground with rotation `45` and a size randomized on both `x` and `z` and of `y=5`.
- a `Cube` spawned on the ground, with a random `x` and `z=30`. Its rotation, size  and color will be random.
- three pink `CylinderTunnel` objects, completely randomized.
- a `GoodGoal` randomized.
- the agent with position and rotation randomized.

&nbsp;

### EXAMPLE 2 - SignPosterboard (Preset Symbols)
```
!ArenaConfig
arenas:
  0: !Arena
    pass_mark: 0
    t: 250
    items:
    - !Item
      name: Agent
      positions:
      - !Vector3 {x: 10, y: 0, z: 20}
      rotations: [90]
    - !Item
      name: SignPosterboard
      positions:
      - !Vector3 {x: 20, y: 0, z: 8}
      - !Vector3 {x: 20, y: 0, z: 14}
      - !Vector3 {x: 20, y: 0, z: 20}
      - !Vector3 {x: 20, y: 0, z: 26}
      - !Vector3 {x: 20, y: 0, z: 32}
      rotations: [0, 0, 0, 0, 0]
      sizes:
      - !Vector3 {x: 1, y: 1, z: 1}
      - !Vector3 {x: 1, y: 1, z: 1}
      - !Vector3 {x: 1, y: 1, z: 1}
      - !Vector3 {x: 1, y: 1, z: 1}
      - !Vector3 {x: 1, y: 1, z: 1}
      symbolNames:
      - "left-arrow"    
      - "letter-a"    
      - "circle"    
      - "u-turn-arrow"    
      - "tick"
```

This example demonstrates the use of preset symbols declared as the list `symbolNames`, a unique parameter for SignPosterboard objects. Each symbol has a default colour that can be overridden using the `colors` list (but in this example, default colours are used).

<p align="center">
  <img height="300" src="PrefabsPictures/Other-Unique/SignPosterboard-preset-symbols.PNG">
</p>

&nbsp;

### EXAMPLE 3 - SignPosterboard (Special Symbols)
```
!ArenaConfig
arenas:
  0: !Arena
    pass_mark: 0
    t: 250
    items:
    - !Item
      name: Agent
      positions:
      - !Vector3 {x: 10, y: 0, z: 20}
      rotations: [90]
    - !Item
      name: SignPosterboard
      positions:
      - !Vector3 {x: 20, y: 0, z: 8}
      - !Vector3 {x: 20, y: 0, z: 14}
      - !Vector3 {x: 20, y: 0, z: 20}
      - !Vector3 {x: 20, y: 0, z: 26}
      - !Vector3 {x: 20, y: 0, z: 32}
      rotations: [0, 0, 0, 0, 0]
      sizes:
      - !Vector3 {x: 1, y: 1, z: 1}
      - !Vector3 {x: 1, y: 1, z: 1}
      - !Vector3 {x: 1, y: 1, z: 1}
      - !Vector3 {x: 1, y: 1, z: 1}
      - !Vector3 {x: 1, y: 1, z: 1}
      symbolNames:
      - "01/10"    
      - "111/110/001"    
      - "001010/011000/100001/101010/111001"    
      - "0101/**10/0010/0***"
      - "13x11"
```

This example demonstrates the use of *special codes* to generate black-and-white pixel grids to use as symbols. `0` -> black, `1` -> white, and `*` is a 'joker' character that chooses to output black or white at random. The dimensions of the grid are given by the `/` character - each row between `/`s must be of the same size for the code to be valid.

Fully-random grids can be generated using the code `"MxN"`, where `M` and `N` are the grid width and height dimensions respectively.

<p align="center">
  <img height="300" src="PrefabsPictures/Other-Unique/SignPosterboard-special-symbols-annotated.png">
</p>

&nbsp;
