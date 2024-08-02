from string import Template

str = "mot_1" "mot_2" "mot_3"
str2 = "mot_1" + "mot_2" + "mot_3"
print(str,'-',str2)

print("-" * 55)

print(ord("a"))
print(ord("A"), type(ord("A")))

print(chr(97))
print(chr(65), type(chr(65)))

print("-" * 55)

print(
    """Ma chaine sur plusieurs lignes:
\t Ligne
La tabulation reste"""
)

print("-" * 55)

print("{} {} {}".format("1", "2", "3"))
print("{1} {2} {0}".format("1", "2", "3"))
print("{1} {2} {0}".format(*"7c56_666"))

print("\nJe m'appelle {prenom} {nom}.".format(nom="CÔTE", prenom="Lionel"))
print("{zero} {un} {deux}".format(un="1", deux="2", zero="0"))

print("\n{:,.2f}".format(1e8), "- {:,.2f}".format(123.456789))
print("{:05d}".format(1),"- ou : {:5d}".format(1))

print("-" * 55)

# Template
s= Template('$elle aime les chats.\n$lui aime les chien')
print(s.substitute(elle="Elle", lui="Lui"))
# print(s.substitute(elle="Elle")) => Provoque erreur
print(s.safe_substitute(elle="Elle"))

print("-" * 55)

entier = 6
print ('entier =6 et print(): \'entier + 1\' - Avec eval():',eval('entier + 1'))

name='Oki'
string = 'print (name+\':\', 777)'
exec(string)
