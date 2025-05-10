from tabulate import tabulate

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


def pf(var: str, style: int = 0, w=cliWR):
    """Show (str) 'var', type and value as prinf(f'{var}=') if int=1 (color cyan)
    else show same data in a table
    """

    ls()

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
            return f"<{type(value).__name__}> {value}"

    # Retrieve caller information
    caller = caller_info()
    frame = inspect.currentframe().f_back

    # Handle multiple variables passed in `var`
    vars = [v.strip() for v in var.split(",")]
    formatted_values = []

    try:
        allFVL = 0  # All formatted values length

        for single_var in vars:

            value = eval(single_var, frame.f_globals, frame.f_locals)

            newValue = format_value(value)
            # lenNV = len(newValue) + 3

            # currentLL += lenNV
            # print(value, f"{currentLL=}")

            # print("allFVL", allFVL)

            formatted_values.append((single_var, newValue))
            # print("lenV", lenNV)

            # Check if we have complex data or long values
            if isinstance(value, (list, tuple, dict)) or hasattr(value, "__dict__"):
                # 2do check if we have long values // cliWR
                complex_data = True  # Mark as complex
        allFVL = sum([len(str(v)) for v in formatted_values]) + 1
    except NameError as e:
        print(f"Error: {e}")
        return

    # Print the formatted values for non-table styles
    if style:
        for var_name, formatted_value in formatted_values:
            print(f"\n\033[1;33;40m{var_name} = {formatted_value}\033[0m")
    else:
        print(f"\033[0;35;40m{f' pf({var}) ':-^{cliWR}}\033[0;37;40m")

        print(f"{allFVL=}", cliWR)

        # If all variables are scalar, display them in a single-row table
        if allFVL < cliWR:
            headers = [
                f"\033[1;36m{var_name}\033[0;37;40m" for var_name, _ in formatted_values
            ]
            data = [[formatted_value for _, formatted_value in formatted_values]]
            tbl(data, headers)
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
                tbl(data, headers)

    print(
        f"\033[0;35;40m{' '+'Lg. '+str(nf(caller[2], 0))+f' - {caller[0]}':-^{cliWR}}\033[0;37;40m"
    )

    print(
        f"\033[0;35;40m{' '+'Lg. '+str(nf(caller[2], 0))+f' - {caller[0]}':-^{cliWR}}\033[0;37;40m"
    )


def pf2(var: str, style: int = 0, w=cliWR):
    """Show (str) 'var', type and value as prinf(f'{var}=') if int=1 (color cyan)
    else show same data in a table
    """

    def format_value(value) -> tuple[str, str]:
        """Retrun tupple ((str) <type> value, len this str)"""
        if value is None:
            return "<None>"

        if isinstance(value, dict):
            # Format each key-value pair for dictionaries
            s = (
                "<dict> {"
                + ", ".join(
                    f"<{type(k).__name__}> {k}: <{type(v).__name__}> {v}"
                    for k, v in value.items()
                )
                + "}"
            )

        elif isinstance(value, tuple):
            # Format each element for tuples, using parentheses
            s = (
                f"<tuple> ("
                + ", ".join(f"<{type(item).__name__}> {item}" for item in value)
                + ")"
            )

        elif isinstance(value, list):
            # Format each element for lists, using brackets
            s = (
                f"<list> ["
                + ", ".join(f"<{type(item).__name__}> {item}" for item in value)
                + "]"
            )

        elif hasattr(value, "__dict__"):  # Safely handle objects with attributes
            try:
                s = (
                    "<object> {"
                    + ", ".join(
                        f"<{type(v).__name__}> {k}: {v}"
                        for k, v in value.__dict__.items()
                    )
                    + "}"
                )
            except Exception as e:
                s = f"<object> Error extracting attributes: {e}"
        else:
            # Default formatting for scalar values
            s = f"<{type(value).__name__}> {value}"

        return s, len(s)

    # Retrieve caller information
    caller = caller_info()
    frame = inspect.currentframe().f_back

    # var = var[:-3]
    # print(var)
    # # Handle multiple variables passed in `var`
    # vars = [v.strip() for v in var.split(",")]
    # print(f"{vars=}")
    # formatted_values = []
    # sl(yellow)

    ls(color=yellow)

    fvs = []
    v = "a"
    value = eval(v, frame.f_globals, frame.f_locals)
    fv = [v, *format_value(value)]
    fvs.append(fv)
    v = "b"
    value = eval(v, frame.f_globals, frame.f_locals)
    fv = [v, *format_value(value)]
    fvs.append(fv)
    v = "c"
    value = eval(v, frame.f_globals, frame.f_locals)
    fv = [v, *format_value(value)]
    fvs.append(fv)

    print(fvs)

    ls(color=yellow)
    ls(color=blue)
    import string

    n = 8
    headers = list(string.ascii_uppercase[:n])
    headers[2] = f"{'\033[1;36mOk': <9}" + eb
    print(len(headers[2]))
    print(rawStrLength(headers[2])[0])
    vs = range(1, n + 1)
    # print(*enumerate(vs))
    tbl([vs], headers)
    ls(color=blue)
    ls(color=yellow)
    ls(color=blue)
    headers = ["a 1", "b 2", "c 3", "d 4", "e 5", "f 6", "g 7", "h 8"]
    vs = [1, 22, 333, 4444, 55555, 666666, 7777777, 88888888]
    tbl([vs], headers)
    ls(color=blue)
    print(7 * 7 + 7 * 2)
    print(56 // 2)
    # v = vars[0]
    # value = eval(v, frame.f_globals, frame.f_locals)
    # newValue = format_value(value)
    # formatted_values.append((v, newValue[0], newValue[1]))
    # print("v:", formatted_values)

    # try:
    #     allFVL = 0  # All formatted values length

    #     for single_var in vars:

    #         value = eval(single_var, frame.f_globals, frame.f_locals)

    #         newValue = format_value(value)[0]
    #         # newValue = format_value(value)
    #         # lenNV = len(newValue) + 3

    #         # currentLL += lenNV
    #         # print(value, f"{currentLL=}")

    #         # print("allFVL", allFVL)

    #         formatted_values.append((single_var, newValue))
    #         # print("lenV", lenNV)

    #         # Check if we have complex data or long values
    #         if isinstance(value, (list, tuple, dict)) or hasattr(value, "__dict__"):
    #             # 2do check if we have long values // cliWR
    #             complex_data = True  # Mark as complex
    #     # allFVL = sum([len(str(v)) for v in formatted_values]) + 1
    #     allFVL = sum([len(str(v)) for v in formatted_values]) + 1
    # except NameError as e:
    #     print(f"Error: {e}")
    #     return

    # # Print the formatted values for non-table styles
    # if style:
    #     for var_name, formatted_value in formatted_values:
    #         print(f"\n\033[1;33;40m{var_name} = {formatted_value}\033[0m")
    # else:
    #     print(f"\033[0;35;40m{f' pf({var}) ':-^{cliWR}}\033[0;37;40m")

    #     print(f"{allFVL=}", cliWR)

    #     print("HERE TABLE")

    # If all variables are scalar, display them in a single-row table
    # if allFVL <= cliWR:
    #     headers = [
    #         f"\033[1;36m{var_name}\033[0;37;40m" for var_name, _ in formatted_values
    #     ]
    #     data = [[formatted_value for _, formatted_value in formatted_values]]
    #     tbl(data, headers)
    # else:
    #     # Separate tables for each complex variable
    #     for var_name, formatted_value in formatted_values:
    #         # print("LONGLINE", len(formatted_value), cliWR)
    #         fv = formatted_value
    #         data = (
    #             [[fv]]
    #             if len(fv) < cliWR
    #             else [
    #                 [format_string(fv, cliWR - 4)],
    #                 ["\033[0;30;40m" + "-" * (cliWR - 4) + "\033[0;37m"],
    #             ]
    #         )
    #         # data = [[" " * 50], [fv]]
    #         headers = [f"\033[1;36m{var_name}\033[0;37;40m"]
    #         tbl(data, headers)

    print(
        f"\033[0;35;40m{' '+'Lg. '+str(nf(caller[2], 0))+f' - {caller[0]}':-^{cliWR}}\033[0;37;40m"
    )

    # print(
    #     f"\033[0;35;40m{' '+'Lg. '+str(nf(caller[2], 0))+f' - {caller[0]}':-^{cliWR}}\033[0;37;40m"
    # )


if __name__ == "__main__":

    cls("tests de pf()")

    a = 7
    b = 88
    c = "111"
    d = (1, 2, 3, 4, "555")
    # pf2("a, b, c")
    # ls()
    pf2("a, b, c, d")
    exit()
    pf("a, b, c, d, a, c")
    pf("a, b, c, d, a, c, b, d, b, c, a")
    ls()
    exit()

    import json

    print(json.dumps(d, indent=4))

    vars = (a, b, c, d, b, c, d, b, c, a)
    pf("vars")
    # print("vars", vars)

    def vv(v):
        return f"<{type(v).__name__}> {v}"

    values = [vv(a) for a in vars]
    # print(values)

    # lengths = sum([len(str(v)) for v in values]) + 2 * len(vars)
    # print(lengths)
    # exit()
    # # Example usage:
    # text = "<list> [<int> 777, <int> 888, <str> 111, <tuple> (1, 2, 3, 4, '555'), <int> 888, <str> 111, <tuple> (1, 2, 3, 4, '555'), <int> 888, <str> 111, <int> 888, <str> 111, <tuple> (1, 2, 3, 4, '555'), <int> 888, <str> 111, <tuple> (1, 2, 3, 4, '555'), <int> 777]"

    # formatted_text = format_string(text, 44)
    # print(text + "\n\n\n" + formatted_text)
