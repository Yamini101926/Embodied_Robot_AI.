"""Beginner-friendly rule-based robot simulation (standard library only)."""

from dataclasses import dataclass
import argparse


@dataclass
class SensorReading:
    human: bool
    obstacle: str
    battery: int


def decide(reading: SensorReading, low_battery: int = 20) -> str:
    """Choose a safe action from one snapshot of simulated sensor readings."""
    if reading.human:
        return "STOP: human detected; wait until the path is clear."
    if reading.battery <= low_battery:
        return "RECHARGE: battery is low; stop and recharge before moving."
    if reading.obstacle == "front":
        return "TURN LEFT: obstacle ahead; check the left side before moving."
    if reading.obstacle == "left":
        return "TURN RIGHT: obstacle on the left; move away from it."
    if reading.obstacle == "right":
        return "TURN LEFT: obstacle on the right; move away from it."
    return "MOVE FORWARD: path is clear."


SCENARIOS = {
    "clear": SensorReading(False, "none", 85),
    "human": SensorReading(True, "none", 85),
    "front-obstacle": SensorReading(False, "front", 85),
    "left-obstacle": SensorReading(False, "left", 85),
    "right-obstacle": SensorReading(False, "right", 85),
    "low-battery": SensorReading(False, "none", 15),
    "human-and-obstacle": SensorReading(True, "front", 85),
}


def display(reading: SensorReading) -> None:
    print(f"Sensors: human={'YES' if reading.human else 'no'}, "
          f"obstacle={reading.obstacle}, battery={reading.battery}%")
    print("Robot:", decide(reading))


def interactive() -> None:
    print("\nRobot simulator. Enter readings; press Ctrl+C to quit.")
    while True:
        try:
            human_text = input("Human detected? [y/N]: ").strip().lower()
            human = human_text in ("y", "yes")
            obstacle = input("Obstacle direction [none/front/left/right]: ").strip().lower()
            if obstacle not in {"none", "front", "left", "right"}:
                print("Please enter none, front, left, or right.\n")
                continue
            battery_text = input("Battery level (0-100): ").strip()
            battery = int(battery_text)
            if not 0 <= battery <= 100:
                print("Battery must be between 0 and 100.\n")
                continue
            reading = SensorReading(human, obstacle, battery)
            display(reading)
            if battery <= 20 and not human:
                if input("Recharge now? [y/N]: ").strip().lower() in ("y", "yes"):
                    reading.battery = 100
                    print("Battery charged to 100%.")
            print()
        except ValueError:
            print("Enter a whole number for battery level.\n")
        except (EOFError, KeyboardInterrupt):
            print("\nSimulation ended.")
            return


def main() -> None:
    parser = argparse.ArgumentParser(description="Simulate a robot using simple sensor rules.")
    parser.add_argument("--scenario", choices=sorted(SCENARIOS), help="Run one example scenario.")
    args = parser.parse_args()
    if args.scenario:
        display(SCENARIOS[args.scenario])
    else:
        interactive()


if __name__ == "__main__":
    main()
