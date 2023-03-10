#!/usr/bin/python3

if __name__ == "__main__":
    """prints all names defined by the hidden_4 compiled module."""

    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[0] != "_":
            name.sort()
            print(name)
