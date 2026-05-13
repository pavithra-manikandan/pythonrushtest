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
        print('o' + '-' * (x - 2) + 'o' if x > 1 else 'o')
        return

    # Top row
    if x == 1:
        print('o')
    else:
        print('o' + '-' * (x - 2) + 'o')

    # Middle rows
    for _ in range(y - 2):
        if x == 1:
            print('|')
        else:
            print('|' + ' ' * (x - 2) + '|')

    # Bottom row
    if x == 1:
        print('o')
    else:
        print('o' + '-' * (x - 2) + 'o')