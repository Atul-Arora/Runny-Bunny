# Runny Bunny — Endless Runner Game (Pygame)

## Overview

Runny Bunny is an endless runner game developed using Python and Pygame.  
The project began as a basic runner tutorial and was subsequently extended to improve gameplay mechanics, difficulty progression, and code structure.

The purpose of this project was to gain practical experience with event-driven game loops, sprite-based animation and movement, collision detection, and incremental difficulty scaling.


## Gameplay Summary

- The player controls a character that runs continuously.
- The objective is to survive as long as possible by avoiding obstacles.
- The score increases with the amount of time survived.
- The game becomes progressively more difficult as the score increases.



## Differences from the Tutorial / Base Code

### Dynamic Speed Scaling
- Tutorial code used a fixed movement speed.
- This implementation increases speed gradually with score and applies an upper limit to maintain fairness.

### Moving Background and Ground
- Tutorial code used static background elements.
- This implementation scrolls both the background and ground at different speeds to create a sense of motion.

### Expanded Enemy Behavior
- Tutorial code included only a ground-based enemy.
- This implementation adds flying enemies and enemies with sinusoidal vertical movement.

### Improved Collision Handling
- Tutorial code relied on default sprite rectangles.
- This implementation uses reduced collision hitboxes to better match visible sprites.

### Adaptive Spawn Rate
- Tutorial code spawned enemies at a fixed interval.
- This implementation reduces spawn delay at score milestones while enforcing a minimum delay.

### Rendering Order Improvements
- Rendering was reorganized to ensure background, gameplay elements, and UI are drawn in a consistent and correct order.


## Technical Details

- Language: Python  
- Library: Pygame  
- Architecture: Object-oriented design using pygame.sprite.Sprite  
- Input: Keyboard and mouse  
- Update model: Frame-based game loop  


## How to Run

1. Install dependencies:
   pip install pygame

2. Run the game:
   python Runny-Bunny.py


## Future Improvements

- Coyote time and jump buffering
- Screen shake on collision
- High score persistence
- Ghost run (previous run replay)
- Additional enemy movement patterns

