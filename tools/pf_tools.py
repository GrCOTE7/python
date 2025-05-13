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


def pf_ori(var: str, style: int = 0, w=cliWR):
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

        return (
            s,
            len(s),
            len(s[0]),
        )

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

    ls(color=red)

    fvs = []
    # v = "aaa"
    # value = eval(v, frame.f_globals, frame.f_locals)
    # fv = [v, *format_value(value)]
    # fvs.append(fv)
    # v = "b"
    # value = eval(v, frame.f_globals, frame.f_locals)
    # fv = [v, *format_value(value)]
    # fvs.append(fv)
    # v = "c"
    # value = eval(v, frame.f_globals, frame.f_locals)
    # fv = [v, *format_value(value)]
    # fvs.append(fv)
    print(fvs)
    # exit()

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

    ls()

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


def pf(ks: str, style: int = 0, indexes=False, w=cliWR):
    """Show (str) 'var', type and value as prinf(f'{var}=')
    style :
        0 | None → tableau simple (Default)
        1 → En colonne
        2 → En colonne avec lengthes
    """

    def format_value(val):

        if isinstance(val, dict):
            # Format each key-value pair for dictionaries
            return (
                "<dict> {"
                + ", ".join(
                    f"<{type(val).__name__}> {val}: <{type(v).__name__}> {val}"
                    for k, v in k.items()
                )
                + "}"
            )
        elif isinstance(val, tuple):
            # Format each element for tuples, using parentheses
            return (
                f"<tuple> ("
                + ", ".join(f"<{type(item).__name__}> {item}" for item in val)
                + ")"
            )
        elif isinstance(val, list):
            # Format each element for lists, using brackets
            return (
                f"<list> ["
                + ", ".join(f"<{type(item).__name__}> {item}" for item in val)
                + "]"
            )
        elif hasattr(val, "__dict__"):  # Safely handle objects with attributes
            try:
                return (
                    "<object> {"
                    + ", ".join(
                        f"<{type(val).__name__}> {val}: {v}"
                        for k, v in val.__dict__.items()
                    )
                    + "}"
                )
            except Exception as e:
                return f"<object> Error extracting attributes: {e}"
        else:
            # Default formatting for scalar values
            return f"{type(val).__name__}", val

    def auto_partition(data: list, L: int, decalU: int = 0, decalP: int = 0) -> list:
        """Retourne le nombre d'élément pour chaque sous-groupe en fonction de L.
        decalU: Décallage Unitaire
        decalP: Décallage Partie
        """

        parts = []
        part = 0
        part_cumul = decalP
        for v in data:
            if part_cumul + v + decalU > L:
                if part:
                    parts.append(
                        part
                    )  # Ajoute l'index du dernier élément du segment valide
                part_cumul = v + decalU  # Redémarre le cumul avec l'élément actuel
                part = 1
            else:
                part += 1
                part_cumul += v + decalU
        parts.append(part)
        return parts

    # Retrieve caller information
    caller = caller_info()
    frame = inspect.currentframe().f_back
    # Handle if multiple variables passed in `var`
    kso = ks
    ks = [k.strip() for k in ks.split(",")]
    formatted_values = []
    # print(keys)
    # print(vals)

    try:
        for k in ks:
            v = eval(k, frame.f_globals, frame.f_locals)
            newV = format_value(v)
            formatted_values.append((newV[0], k, newV[1]))
            # Check if we have complex data or long values
            if isinstance(v, (list, tuple, dict)) or hasattr(v, "__dict__"):
                # 2do check if we have long values // cliWR
                complex_data = True  # Mark as complex
        # allFVL = sum([len(str(v)) for v in formatted_values]) + 1
    except NameError as e:
        print(f"Error: {e}")
        return

    # print([formatted_value for formatted_value in formatted_values])

    print(f"{style=} | {indexes=}")

    if style > 0:
        lengths = [len(str(val)) for item in formatted_values for val in item[1:]]
    if style == 1:
        headers = [
            f"\033[1;36;40mType{eb}",
            f"\033[1;36;40mVar{eb}",
            f"\033[1;36;40mVal{eb}",
        ]
        data = [[v[0], v[1], v[2]] for v in formatted_values]
        colalign = ["center", "left", "right"]
        # tbl(data, headers, indexes)
    elif style == 2:
        print("style 2 - ", lengths)
        headers = [
            f"\033[1;36;40mType{eb}",
            f"\033[1;36;40mKey{eb}",
            "KLen",
            f"\033[1;36;40mVal{eb}",
            "VLen",
            "MaxLen",
        ]
        data = [
            [
                v[0],
                v[1],
                len(v[1]),
                v[2],
                len(str(v[2])),
                max(len(v[1]), len(str(v[2]))),
            ]
            for v in formatted_values
        ]
        colalign = ["center", "left", "right", "right", "right", "right"]
        # tbl(data, headers)
    else:
        indexes = False

        # print(formatted_values)
        # lengths = [max(len(v[1]), len(v[2])) for v in formatted_values]
        lengths = [len(str(val)) for item in formatted_values for val in item[1:]]
        print("ligne 460: ", lengths)
        # print(auto_partition(lengthes, cliWR))
        # print(auto_partition(lengths, 20, 3, 1))
        # Print the formatted values for non-table styles
        # print(f"{allFVL=}", cliWR)

        # If all variables are scalar, display them in a single-row table
        if 1000 < cliWR + 10 and 0:
            headers = [
                f"\033[1;36m{var_name}\033[0;37;40m" for var_name, _ in formatted_values
            ]
            data = [[formatted_value for _, formatted_value in formatted_values]]
            # tbl(data, headers, indexes)
        elif 0:
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
                # tbl(data, headers, indexes=False)

    print(
        f"\033[1;36;40m{f' pf(\'{kso}\', {style}, {indexes*1}) ':-^{cliWR}}\033[0;37;40m"
    )
    if indexes:
        headers.insert(0, "#")
        colalign.insert(0, "right")
    # print(headers)
    # print(data)
    tbl(
        data,
        headers,
        colalign=colalign,
        indexes=indexes,
    )
    s = f"\033[1;36;40m{f' {caller[1]}'+f' - {caller[0]}:{'\033[1;31;47m'+str(nf(caller[2], 0))}'}{eb} "
    print(f"{s:-^{cliWR+rawStrLength(s)[1]}}")


if __name__ == "__main__":

    cls("tests de pf()")

    aaaaatreslong = 7
    bb = "22222222222"
    c = 333
    pf("aaaaatreslong,bb,c", 2)
    pf("aaaaatreslong,bb,c")
    exit()

    pf("aaaaatreslong,b,c", 2, False)
    pf("aaaaatreslong,b,c", 1, True)
    pf("aaaaatreslong,b,c", 1, False)

    exit()
    # a = [1, 2]
    # a.insert(0, 0)
    # print(a)

    data = [13, 8, 9]
    L = 27
    ls()
    if 1:
        print(str(data) + "\n")
        l = auto_partition(data, L, 3, 1)
        if L == 14:
            print(f"LIMITE={L}")
            print("─" * len(str(l)) + "\n" + str(l) + "\n" + "─" * len(str(l)))

        print("Reconstitution:")
        i = 0
        for n in l:
            print(data[i : i + n])
            i += n

    exit()

    exit()
    if 0:
        ls()
        aaa = 7
        pf2("aaa")
        exit()
        b = 88
        c = "111"
        d = (1, 2, 3, 4, "555")
        pf2("aaa, b, c, d")

        # pf2("a, b, c")
        # ls()
        exit()
        # pf("a, b, c, d, a, c")
        # pf("a, b, c, d, a, c, b, d, b, c, a")
        ls()
        exit()

        import json

        print(json.dumps(d, indent=4))

        vars = (a, b, c, d, b, c, d, b, c, a)
        pf("vars")
        # print("vars", vars)

    def vv(v):
        return f"<{type(v).__name__}> {v}"

    # values = [vv(a) for a in vars]

    # print(values)

    # lengths = sum([len(str(v)) for v in values]) + 2 * len(vars)
    # print(lengths)
    # exit()
    # # Example usage:
    # text = "<list> [<int> 777, <int> 888, <str> 111, <tuple> (1, 2, 3, 4, '555'), <int> 888, <str> 111, <tuple> (1, 2, 3, 4, '555'), <int> 888, <str> 111, <int> 888, <str> 111, <tuple> (1, 2, 3, 4, '555'), <int> 888, <str> 111, <tuple> (1, 2, 3, 4, '555'), <int> 777]"

    # formatted_text = format_string(text, 44)
    # print(text + "\n\n\n" + formatted_text)
