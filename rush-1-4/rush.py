import sys

def rush(x, y):
    """
    Display a square pattern based on x (width) and y (height)
    Args:
        x (int): Width of the square
        y (int): Height of the square
    """
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    if y == 1:
        print('B' * x)
        return

    # Top row: A top-left, C top-right
    if x == 1:
        print('B')
    else:
        print('A' + 'B' * (x - 2) + 'C')

    # Middle rows
    for _ in range(y - 2):
        if x == 1:
            print('B')
        else:
            print('B' + ' ' * (x - 2) + 'B')

    # Bottom row: A bottom-left, C bottom-right
    if x == 1:
        print('B')
    else:
        print('A' + 'B' * (x - 2) + 'C')