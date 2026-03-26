from pyparsing import C
from tabulate import tabulate
import sys

sys.path.append("c:/laragon/www/PYTHON/python/tools/")
from globals import *
from main_tools import *


def format_string(text, w=55):
    """
    Formats a string to fit within a defined width,
    ensuring line breaks occur only at appropriate places (after a comma).
    """
    w -= 1
    lines = []
    current_line = ""

    for segment in text.split(", "):  # Preserve ", " in the structure
        if len(current_line) + len(segment) + 1 > w:  # +2 for the ", │"
            lines.append(
                "│ " + current_line + ","
            )  # Keep the comma at the end of the line
            current_line = segment  # Start a new line with the next segment
        else:
            current_line += (
                ", " + segment if current_line else segment
            )  # Append normally

    lines.append("│ " + current_line + "\b")  # Last line without extra comma

    # allLines = "\n".join(lines)
    # allLines[0] = ""
    print(type(lines))
    lines[0] = lines[0][2:]

    # print(lines, len(lines))
    print([(i, lines[i], "\n") for i in range(len(lines))])
    allLines = "\n".join(lines)
    return allLines  # Join lines with newlines


def pf(var: str, style: int = 0, indexes=False, w=cliWR):
    """Show (str) 'var', type and value as prinf(f'{var}=') if int=1 (color cyan)
    else show same data in a table
    """

    def format_value(value):

        if isinstance(value, dict):
            # Format each key-value pair for dictionaries
            return (
                "<dict> {"
                + ", ".join(
                    f"<{type(k).__name__}> {k}: <{type(v).__name__}> {v}"
                    for k, v in value.items()
                )
                + "}"
            )
        elif isinstance(value, tuple):
            # Format each element for tuples, using parentheses
            return (
                f"<tuple> ("
                + ", ".join(f"<{type(item).__name__}> {item}" for item in value)
                + ")"
            )
        elif isinstance(value, list):
            # Format each element for lists, using brackets
            return (
                f"<list> ["
                + ", ".join(f"<{type(item).__name__}> {item}" for item in value)
                + "]"
            )
        elif hasattr(value, "__dict__"):  # Safely handle objects with attributes
            try:
                return (
                    "<object> {"
                    + ", ".join(
                        f"<{type(v).__name__}> {k}: {v}"
                        for k, v in value.__dict__.items()
                    )
                    + "}"
                )
            except Exception as e:
                return f"<object> Error extracting attributes: {e}"
        else:
            # Default formatting for scalar values
            # t = type(value)
            # if t == float or t == int:
            #     value = nf(value)
            return f"<{type(value).__name__}> {value}"

    # Retrieve caller information
    caller = caller_info()
    frame = inspect.currentframe().f_back

    # Handle multiple variables passed in `var`
    vars = [v.strip() for v in var.split(",")]
    formatted_values = []

    try:
        allHeadsL = allFVL = 0  # All formatted values length

        for single_var in vars:

            value = eval(single_var, frame.f_globals, frame.f_locals)

            newValue = format_value(value)
            # lenNV = len(newValue) + 3

            # currentLL += lenNV
            # print(value, f"{currentLL=}")

            # print("allFVL", allFVL)

            formatted_values.append((single_var, newValue))
            # formatted_values.append((single_var, len(single_var), newValue))
            # print("lenV", lenNV)

            # Check if we have complex data or long values
            if isinstance(value, (list, tuple, dict)) or hasattr(value, "__dict__"):
                # 2do check if we have long values // cliWR
                complex_data = True  # Mark as complex
        allFVL = sum([len(str(v)) for v in formatted_values]) + 1
    except NameError as e:
        print(f"Error: {e}")
        return

    # print([formatted_value for _, formatted_value in formatted_values])

    # Print the formatted values for non-table styles
    print(
        f"\033[1;36;40m{f' pf(\'{var}\', {style}, {indexes*1}) ':-^{cliWR}}\033[0;37;40m"
    )

    print(f"{style=} | {indexes=}")

    if style == 1:
        headers = [f"\033[1;36;40mVar", f"Value{eb}"]
        data = [[v[0], v[1]] for v in formatted_values]
        tbl(data, headers, indexes)
    elif style == 2:
        headers = [
            f"\033[1;36;40mVar{eb}",
            "lenVar",
            f"\033[1;36;40mValue{eb}",
            "lenVal",
            "lenMax",
        ]
        data = [
            [v[0], len(v[0]), v[1], len(v[1]), max(len(v[0]), len(v[1]))]
            for v in formatted_values
        ]
        tbl(data, headers, indexes=True)
    else:

        print(f"{allFVL=}", cliWR)

        # If all variables are scalar, display them in a single-row table
        if allFVL < cliWR + 10:
            headers = [
                f"\033[1;36m{var_name}\033[0;37;40m" for var_name, _ in formatted_values
            ]
            data = [[formatted_value for _, formatted_value in formatted_values]]
            tbl(data, headers, indexes)
        else:
            # Separate tables for each complex variable
            for var_name, formatted_value in formatted_values:
                # print("LONGLINE", len(formatted_value), cliWR)
                fv = formatted_value
                data = (
                    [[fv]]
                    if len(fv) < cliWR
                    else [
                        [format_string(fv, cliWR - 4)],
                        ["\033[0;30;40m" + "-" * (cliWR - 4) + "\033[0;37m"],
                    ]
                )
                # data = [[" " * 50], [fv]]
                headers = [f"\033[1;36m{var_name}\033[0;37;40m"]
                tbl(data, headers, indexes=False)

    s = f"\033[1;36;40m{f' {caller[1]}'+f' - {caller[0]}:{'\033[1;31;47m'+str(nf(caller[2], 0))}'}{eb} "
    print(f"{s:-^{cliWR+rawStrLength(s)[1]}}")

    # headers = [f"\033[1;36;40mVar{eb}", "lenVar", f"\033[1;36;40mValue{eb}", "lenVal"]
    # data = [[v[0], len(v[0]), v[1], len(v[1])] for v in formatted_values]
    # tbl(data, headers)


def auto_partition(data: list, L: int) -> list:
    """Découpe la liste 'data' en sous-groupes en fonction de L."""

    partitions = []
    i_validated = index = part_cumul = 0

    for _, v in data:
        if (part_cumul + v) > L:
            partitions.append(tuple(data[i_validated:index]))  # Ajoute le bloc validé
            i_validated = index  # Début du nouveau segment
            part_cumul = v  # Ajoute v dès le début du segment
        else:
            part_cumul += v
        index += 1  # Avancer l'index
    # Ajoute le dernier segment
    if i_validated < len(data):
        partitions.append(tuple(data[i_validated:]))

    return partitions


if __name__ == "__main__":

    cls("Width Tests")

    aaaaatreslong = 7
    b = "22"
    c = 333
    pf("aaaaatreslong,b,c", 2, True)
    # pf("aaaaa,b,c", 1)
    pf("aaaaatreslong,b,c", 1)
    ls()
    pf("aaaaatreslong,b,c")

    exit()
