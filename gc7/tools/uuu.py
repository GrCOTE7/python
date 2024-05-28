import sys, os


def get_caller_depth():
    # Obtenir le chemin absolu du script appelant
    caller_path = os.path.abspath(os.path.dirname(sys._getframe(1).f_code.co_filename))

    # Compter le nombre de dossiers dans le chemin
    depth = caller_path.count(os.sep)

    return depth


# Test the function
# print('Module: ', get_script_depth())
print('Dans module: ', get_caller_depth())
