import os, sys, inspect, locale, shutil, time
from tabulate import tabulate

cliWR = shutil.get_terminal_size().columns  # Réelle CLI Width


def tbl(data, headers=[], indexes=False):
    print(
        tabulate(
            data,
            headers,
            tablefmt="rounded_outline",
            showindex=indexes,
        )
    )


def chrono(function):
    """Décorateur: Calcule le temps en secondes que met une fonction à s'executer.\n
    Placer @ chrono dans la ligne précédent le def de la fonction."""

    def wrapper(*args, **kwargs):
        """Décore la fonction avec un calcul du temps."""
        # retourne le temps en secondes depuis le 01/01/1970.
        # (Le temps "epoch").
        start = time()

        result = function(*args, **kwargs)

        end = time()
        # Différence entre 2 temps "epochs", celui qui est gardé dans "start", et celui qui sera gardé dans "end". ;)
        time_spent = end - start

        print(f"{str(args[0]) + ': ' if args else ''}{time_spent:.2f}\"")
        print(f"{str(args[0]) + ': ' if args else ''}{time_spent:.2f}\"")

        return result

    wrapper.__doc__ = function.__doc__
    return wrapper


def nf(f, dec=2):
    "Number Format 123456789 → 123 456,79"
    format_str = "%." + str(dec) + "f"
    return locale.format_string(format_str, f, grouping=True)


def caller_info(justFileName: bool = False) -> tuple | str:
    """
    Without argument: (tuple) Path of caller file, caller function name, index of line where is the instruction.\nIf argument is True (or 1): (str) Just theCcller file name
    """
    # Obtenir le cadre deux niveaux au-dessus dans la pile
    frame = inspect.currentframe().f_back.f_back
    # Obtenir le chemin complet du fichier appelant
    callerFilePath = os.path.relpath(inspect.getfile(frame))  # Chemin relatif
    # Obtenir le numéro de ligne
    callerLineNumber = frame.f_lineno
    # Nom de la fonction appelante
    function_name = frame.f_code.co_name
    context = "main" if function_name == "<module>" else f"{function_name}()"

    if justFileName:
        # return callerFilePath # 2ar vérif si dessous ok
        return os.path.basename(callerFilePath)
    return callerFilePath, context, callerLineNumber


def pf(var: str, style: int = 0):
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
            return f"<{type(value).__name__}> {value}"

    # Retrieve caller information
    lineNumber = caller_info()[2]
    frame = inspect.currentframe().f_back

    # Handle multiple variables passed in `var`
    vars = [v.strip() for v in var.split(",")]
    formatted_values = []
    try:
        for single_var in vars:
            # Evaluate and format each variable independently
            value = eval(single_var, frame.f_globals, frame.f_locals)
            formatted_values.append((single_var, format_value(value)))
    except NameError as e:
        print(f"Error: {e}")
        return

    # Print the formatted values for non-table styles
    if style:
        for var_name, formatted_value in formatted_values:
            print(f"\n\033[1;36;40m{var_name} = {formatted_value}\033[0m")
    else:
        # Display the main en-tête
        print(f"\033[0;36;40m{f' pf({var})':-^{cliWR}}\033[0;37;40m")
        print()

        # Display separate tables for each variable without separation
        for var_name, formatted_value in formatted_values:
            # Create a separate table for each variable
            data = [[formatted_value]]
            headers = [f"\033[1;36m{var_name}\033[0;37;40m"]

            # print("DATA for tbl:", data)
            # print("HEADERS for tbl:", headers)
            tbl(data, headers)  # No text between tables

    # Display the final line (only once)
    print(
        f"\033[0;36;40m{' '+'Lg. '+str(nf(lineNumber, 0))+' ':-^{cliWR}}\033[0;37;40m"
    )
