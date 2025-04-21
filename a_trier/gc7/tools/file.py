import sys, os, csv


def get_depth():
    print("profondeur")
    csv_path = os.getcwd() + "/bases/doc/data/persons.csv"
    print("cwd: ", os.getcwd())


def get_data():
    # print("data")
    csv_path = "c:\\laragon\\www\\python\\bases\\doc\\data\\persons.csv"
    # print("cwd: ", csv_path)
    # print("cwd: ", os.getcwd())

    try:
        # script_dir = os.path.dirname(os.path.abspath(__file__))
        # project_root = os.path.dirname(os.path.dirname(script_dir))
        # print("projet_root (<module)", project_root)
        with open(csv_path, encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file, delimiter=",")
            # for line in reader:
            # line = {key.strip(): value.strip() for key, value in line.items()}
            # print(line)
            # pass
            members=[]
            for line in reader:
                line = {key.strip(): value.strip() for key, value in line.items()}
                members.append(line)

            return members
    except Exception as e:
        print(e)


def get_caller_depth():
    # Obtenir le chemin absolu du script appelant
    caller_path = os.path.abspath(os.path.dirname(sys._getframe(1).f_code.co_filename))

    # print(caller_path)

    # Compter le nombre de dossiers dans le chemin
    depth = caller_path.count(os.sep)

    return depth


# print("Dans module: ", get_caller_depth())

# get_data()
# get_depth()
