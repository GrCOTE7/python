from pymox_kit import end
import flet, pyperclip


def main():

    str_to_clip = "A string in the clipboard"
    pyperclip.copy(str_to_clip)
    print("Ok, fait !\n → Do CTRL + V to paste the string in the clipboard")


if __name__ == "__main__":

    main()
    end()
