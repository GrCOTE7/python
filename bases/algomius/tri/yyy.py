params = {"ecrans": 2, "op_name": "Tri itératif", "xdec": 5, "ydec": 8}


def mon_module(params=None):
    if params is None:
        params = {}

    # values = [params.get(key, valeur_par_defaut) for key in keys]
    # # values = [params[key] for key in keys]

    # ecrans, op_name, xdec, ydec = values

    # print(ecrans, xdec)

    keys = list(params.keys())

    print(keys)

    print([params[k] for k in keys][1])

    for k in keys:
        print(params[k])


if __name__ == "__main__":
    mon_module(params)
