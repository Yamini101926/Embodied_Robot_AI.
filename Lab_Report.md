# Lab Report: Simulate Embodied Behavior Using Python

**Name:** ____________________  **Date:** ____________________

## Aim

To model how a simple robot senses its surroundings and chooses an action using Python.

## Setup

The project uses simulated readings for human presence, obstacle direction, and battery level. The program applies a priority-ordered set of rules: stop for a human, request a recharge at 20% battery or below, turn away from an obstacle, or move forward if the path appears clear.

## Procedure

1. Run the interactive simulator with `python robot_sim.py`, or run built-in examples with `python robot_sim.py --scenario NAME`.
2. Record sensor inputs and the printed action for at least three different situations.
3. Include one situation where more than one condition is present.

## Observations

| Human detected? | Obstacle direction | Battery | Robot action | Was the action sensible? |
|---|---|---:|---|---|
| No | None | 85% | Move forward | Yes / No: __________ |
| Yes | Front | 85% | Stop and wait | Yes / No: __________ |
| No | Left | 15% | Recharge / stop | Yes / No: __________ |

Replace or add rows with your own runs.

## Result and conclusion

The simulated robot used sensor readings to select different actions. A human detection triggered a stop, a low battery triggered a recharge request, obstacles caused a suggested turn, and a clear reading allowed forward movement. This demonstrates a basic perception-to-action loop: sense, decide, act.

## Limitations

The sensors are typed in by a person and can be wrong. The robot does not move in a map, measure distance, or check whether its suggested turn is safe. Its rules are illustrative and are not suitable for controlling a real robot.

## Reflection

1. Which sensor reading has the highest priority, and why?
2. What additional sensor or rule would make obstacle avoidance safer?
3. What changed when battery reached the 20% threshold?
