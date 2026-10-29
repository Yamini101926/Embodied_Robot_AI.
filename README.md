# Simulate Embodied Behavior Using Python

A small, beginner-friendly terminal lab. The simulated robot reads a human-detection sensor, obstacle direction, and battery percentage, then selects an action. No physical robot or extra Python packages are needed.

## Requirements

- Python 3.9 or newer
- A terminal (PowerShell, Command Prompt, macOS Terminal, or Linux shell)

## Run it

From this folder, start the interactive simulation:

```text
python robot_sim.py
```

At each step, answer whether a human is detected, give the obstacle direction (`none`, `front`, `left`, or `right`), and enter a battery percentage from 0 to 100. At low battery, the robot recommends stopping to recharge and offers to set the simulated battery to 100%.

Run a repeatable example by name:

```text
python robot_sim.py --scenario front-obstacle
```

See all scenario names with:

```text
python robot_sim.py --help
```

On some computers, use `python3` in place of `python`.

## Decision rules

The robot applies rules in this order:

1. If a human is detected, stop and wait.
2. Otherwise, if battery is 20% or lower, stop and request a recharge.
3. Otherwise, turn away from an obstacle (front means suggest left; left means right; right means left).
4. If no hazard is reported, move forward.

This priority makes a human stop take precedence when several conditions occur together. A suggested turn is a simple teaching rule: the simulation does not verify that the chosen side is actually clear.

## Sample scenarios and expected outputs

Run each with `python robot_sim.py --scenario NAME`.

| Scenario | Sensor readings | Expected action |
|---|---|---|
| `clear` | Human: no; obstacle: none; battery: 85% | `MOVE FORWARD: path is clear.` |
| `human` | Human: yes; obstacle: none; battery: 85% | `STOP: human detected; wait until the path is clear.` |
| `front-obstacle` | Human: no; obstacle: front; battery: 85% | `TURN LEFT: obstacle ahead; check the left side before moving.` |
| `left-obstacle` | Human: no; obstacle: left; battery: 85% | `TURN RIGHT: obstacle on the left; move away from it.` |
| `right-obstacle` | Human: no; obstacle: right; battery: 85% | `TURN LEFT: obstacle on the right; move away from it.` |
| `low-battery` | Human: no; obstacle: none; battery: 15% | `RECHARGE: battery is low; stop and recharge before moving.` |
| `human-and-obstacle` | Human: yes; obstacle: front; battery: 85% | Human stop takes priority. |

Example:

```text
$ python robot_sim.py --scenario front-obstacle
Sensors: human=no, obstacle=front, battery=85%
Robot: TURN LEFT: obstacle ahead; check the left side before moving.
```

## Suggested lab activity

1. Run `clear`, then run `human` and compare the robot's actions.
2. Try all three obstacle directions. Explain how the direction changes the suggested turn.
3. Change the battery in `SCENARIOS` in `robot_sim.py` to 20, then to 21. Observe the threshold.
4. Try `human-and-obstacle`. Explain why the robot stops.
5. Add a scenario or change one rule. Describe how the change affects the behavior.

## Files

- `robot_sim.py` — simulator, sensor input, decision rules, and built-in scenarios.
- `LAB_REPORT.md` — short report template with the model, observations, and limitations.