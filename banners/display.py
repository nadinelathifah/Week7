
def create_banner(message: str, textcolor: int) -> str:
    """
    This function generates and formats a custom decorative banner, enclosed by a box-line border.\n
    The banner size adjusts based on the length of the input message.
    The color of the text can be changed by inputting ANSI escape code number.
    :param message: str
    :param textcolor: int
    :return: str
    """
    text = message.title()
    line_length = 20 + len(text)

    top = " " * 6 + "\u2554" + "\u2550" * line_length + "\u2557\n"
    middle = (
            "\u2551" + "  "
            + "  ".join("\u2605" * 4)
            + "    "
            + f"\033[1;{textcolor}m{text}\033[0m"
            + "    "
            + "  ".join("\u2605" * 4)
            + "  "
            + "\u2551\n"
    )
    bottom = " " * 6 + "\u255a" + "\u2550" * line_length + "\u255d"

    return top + middle + bottom

def add_border(color):
    return "\n" + f"\033[{color}m\u2605"*200 + "\033[0m"

