from os import path
import shutil
from datetime import date, time, timedelta
import time
from zipfile import ZipFile

file = "README.md"


def save_readme():

    if path.exists(file):
        src = path.realpath(file)
        print("src:", src)

        head, tail = path.split(src)
        print(f"Chemin: {head}\nFichier: {tail}")

        dst = src + ".bak"

        shutil.copy(src, dst)  # copy file as new file
        shutil.copystat(src, dst)  # copie metadata (date, etc...)


def get_infos(file="README.md"):
    # get the modification time of a file
    mtime = path.getmtime(file)
    print("mtime:", mtime)
    print("Date de modification:", time.ctime(mtime))

    # get the creation time of a file
    ctime = path.getctime(file)
    print("ctime:", ctime)
    print("Date de création:", time.ctime(ctime))

    # get the size of a file
    size = path.getsize(file)
    print("size:", size)


def make_folder_archive(file=file):
    file += ".bak"
    if path.exists(file):
        src = path.realpath(file)
        head, tail = path.split(src)
        print(f"\nChemin: {head}\nFichier: {tail}")

        # Zip all folder designed by head
        shutil.make_archive("archive", "zip", head)


def make_some_files_archive():
    ''' Zip some files
    '''
    with ZipFile('README_Archives.zip', 'w') as newzip:
        newzip.write("README.md")
        newzip.write("README.md.bak")
    print('README.md and README.md.bak saved.')

def main():
    
    # save_readme()
    # get_infos()
    print()
    # get_infos("README.md.bak")

    print(time.ctime(time.time()))

    print("-" * 72)

    # make_some_files_archive()

if(__name__ == "__main__")  :
    main()
