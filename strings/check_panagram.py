# Created by sarathkaul on 12/11/19


def check_panagram(
    input_str: str = "The quick brown fox jumps over the lazy dog",
) -> bool:
    """
    A Panagram String contains all the alphabets at least once.
    >>> check_panagram("The quick brown fox jumps over the lazy dog")
    True
    >>> check_panagram("My name is Unknown")
    False
    >>> check_panagram("The quick brown fox jumps over the la_y dog")
    False
    """
    input_str = input_str.replace(
        " ", ""
    )  # Replacing all the Whitespaces in our sentence
    frequency = {
        alpha.lower() for alpha in input_str if "a" <= alpha.lower() <= "z"
    }
    return len(frequency) == 26


if __name__ == "main":
    check_str = "INPUT STRING"
    status = check_panagram(check_str)
    print(f"{check_str} is {'not ' if status else ''}a panagram string")
