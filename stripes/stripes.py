import sys


# Note: this syntax hasn't been introduced yet,
#  but indicates that size is an integer and horizontal is a bool,
#  and that the function returns a list of lists of strings
def make_stripes(size: int, horizontal: bool) -> list[list[str]]:
    """
    Create a square list of lists with a striped pattern of '*' and 'o'.

    The pattern should follow these rules:

    If pattern is horizontal:
        - then each even-numbered row (starting with 0) should be made of '*',
        - odd-numbered rows should be made of 'o'.
    If pattern is vertical (horizontal=False):
        - then each even-numbered column (starting with 0) should be made of '*',
        - odd-numbered columns should be made of 'o'.

    Parameters:
        size: int - Size of square's side.
        horizontal: bool - True if horizontal, False if vertical.
    """
    # REPLACE THIS COMMENT WITH YOUR CODE


def show_grid(list_of_lists: list[list[str]]) -> None:
    """
    Print a list of lists of strings (like the one created by stripes)
    """
    for row in list_of_lists:
        print("".join(row))


def main():
    # this code does not need to be understood yet
    # is extracts the two command line parameters and ensures they are
    # of the correct type before passing them to strips
    try:
        n = int(sys.argv[1])
        direction = sys.argv[2]
        if direction not in ("horizontal", "vertical"):
            raise ValueError("invalid direction")
    except Exception:
        print("Usage: python3 stripes.py <n> <direction>")
        sys.exit(1)

    show_grid(make_stripes(n, direction == "horizontal"))


if __name__ == "__main__":
    main()
