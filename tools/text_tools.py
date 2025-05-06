import lorem, textwrap
from tools import cls

# from tools import cliW, rawStrLength


def justify(text, width):
    # Divise le texte en mots
    lines = textwrap.wrap(text, width)
    justified_lines = []

    for line in lines[:-1]:  # Ne pas justifier la dernière ligne
        words = line.split()
        if len(words) == 1:  # Si une seule mot, aucune justification
            justified_lines.append(line)
            continue
        # Calcule les espaces nécessaires pour justifier
        total_spaces = width - sum(len(word) for word in words)
        spaces_between_words = len(words) - 1
        spaces = [total_spaces // spaces_between_words] * spaces_between_words
        for i in range(total_spaces % spaces_between_words):
            spaces[i] += 1
        # Assemble la ligne justifiée
        justified_line = "".join(
            word + " " * space for word, space in zip(words, spaces + [0])
        )
        justified_lines.append(justified_line)

    justified_lines.append(lines[-1])  # Ajouter la dernière ligne non justifiée
    return "\n".join(justified_lines)


def justifyCenter(text, width):
    # Divise le texte en mots et calcule les lignes justifiées

    lines = textwrap.wrap(text, width)
    justified_lines = []

    for line in lines[:-1]:  # Ne pas justifier la dernière ligne
        words = line.split()
        if len(words) == 1:  # Si une seule mot, aucune justification
            justified_lines.append(line.center(width))
            continue
        total_spaces = width - sum(len(word) for word in words)
        spaces_between_words = len(words) - 1
        spaces = [total_spaces // spaces_between_words] * spaces_between_words
        for i in range(total_spaces % spaces_between_words):
            spaces[i] += 1
        justified_line = "".join(
            word + " " * space for word, space in zip(words, spaces + [0])
        )
        justified_lines.append(
            justified_line.center(width)
        )  # Centrer la ligne justifiée

    justified_lines.append(
        lines[-1].center(width)
    )  # Centrer la dernière ligne non justifiée
    return "\n".join(justified_lines)


cliW = 55


def wordWrap(msg: tuple, w: int = cliW, align="<"):

    msg = "𐍈".join(str(item) for item in msg)
    # 2ar lengthes = rawStrLength(msg)
    # pf("lengthes")

    # pf("len(msg), rawStrLength(msg)[0] > w, w")
    # if 2ar lengthes[0] <= w:
    # print("DÉBUT TITRE: 1 ligne")
    # msg = msg.replace("𐍈", hyphen)
    # 2ar hyphen = " "
    # 2ar else:
    # print("DÉBUT TITRE: Des lignes")
    # 2ar msgParts = msg.split("𐍈")
    # print(msgParts)
    # 2armsg = "".join(
    # 2ar list(map(lambda l: f"{l: {align}{w+rawStrLength(l)[1]}}", msgParts))
    # 2ar)

    # return (msg, lengthes)
    # msg = f"{msg[0]} {msg[1]}"
    # msg = tuple(msg)


if __name__ == "__main__":
    cls()
    print("ok")
    # print(tools.__file__)

    txt = lorem.paragraph()
    print(justify(txt, 55), "\n\n", justifyCenter(txt, 55), "\n\n", txt)
    print(wordWrap(txt))

    print(lorem.paragraph())
    print("-" * 55)
    long_lorem = lorem._Lorem(prange=(20, 30))
    print(long_lorem.paragraph())
