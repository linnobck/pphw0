# DO NOT MODIFY THIS SECTION, SEE make_plant below
import time
from rich.console import Console

console = Console()

FLOWER = "❋"
STEM = "|"
LEAF = "~"


def make_plant(height: int) -> str:
    """
    This function should return a string representing an "ascii art" plant.

    This should be a string with {height} lines with the following rules:

    - the top line should always be the FLOWER symbol, preceded by a space
    - the second line should always be a STEM with two LEAVES, like ~|~
    - lines divisible by three should contain a STEM with two LEAVES
    - all other lines should be a STEM preceded by a space

    See the README for examples.
    """
    lines = []      # to store all the flower parst
    growing = 1     # initialize variable to keep track of how tall the flower grows
    while growing <= height:
        # adding the flower parts depending on what number line they are on
        if growing == 1:
            lines.append(f" {FLOWER}")
        elif growing == 2:
            lines.append(f"{LEAF}{STEM}{LEAF}")
        elif (growing -1) % 3 == 0:
            lines.append(f"{LEAF}{STEM}{LEAF}")
        else:
            lines.append(f" {STEM}")
        growing +=1

    # assemble and return plant
    plant = "\n".join(lines) + "\n"
    return plant


def print_plant(plant_str):
    """
    This function is used in main to print the plant to the screen.

    DO NOT MODIFY THIS FUNCTION
    """
    flower, plant = plant_str.split("\n", 1)
    console.clear()
    console.print(flower, style="magenta")
    console.print(plant, style="green")


def main():
    """
    This prints a plant growing from height=2 to height=12
    """
    for n in range(2, 13):
        print_plant(make_plant(n))
        time.sleep(0.3)


if __name__ == "__main__":
    main()
