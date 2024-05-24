import os, time, shutil, glob, sys

def car(delai=3):
    for i in range(delai, 0, -1):
        print(i)
        time.sleep(1)

def create_folder_if_not_exists(folder):
    if os.path.exists(folder):
        print(f"Le répertoire {folder} existe déjà.")
    else:
        # Créer le répertoire
        os.system(f"mkdir {folder}")
        print(f"Le répertoire '{folder}' a été créé.")
        
        
print(glob.glob('*.py'))
car(7)

print('Écriture de :', shutil.copyfile('data.txt', 'data_sav.txt'))

help(shutil)
car()

# sys.exit()
create_folder_if_not_exists('archives')
print('Copie de data_sav.txt')
shutil.move('data_sav.txt', 'archives/data_sav.txt')
car()

print(dir(os))
car()

print("On est dans:", os.getcwd())  # Return the current working directory
car()

os.chdir("./modules/")  # Change current working directory
print("On est dans:", os.getcwd())  # Return the current working directory
car()

os.chdir("..")  # Change current working directory
print("On est dans:", os.getcwd())  # Return the current working directory
car()

# Vérifier si le répertoire existe
if os.path.exists("today"):
    print("Le répertoire 'today' existe déjà.")
else:
    # Créer le répertoire
    os.system("mkdir today")
    print("Le répertoire 'today' a été créé.")
car()

# Effacer le répertoire
os.system("rm -r today")
print("Le répertoire 'today' a été supprimé.")
car()

help(os)
