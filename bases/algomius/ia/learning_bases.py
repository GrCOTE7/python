# https://www.youtube.com/watch?v=yx97Gm1Nsp4&list=PLo53cbpzes8ZvHD1v7n-Py-EQGdOH2WOa

"""
    Premier exemple de programme qui permet d'apprendre en cas d'absence de reponse
"""

print("Bonjour")

reponse = {"ca va ?" : "Bien et toi ?",
           "Coucou" : "Bonjour !" }

question = input()

while question != "Au revoir":
    if question in reponse:
        print(reponse[question])
    else:
        print("Je ne sais pas comment réagir, quelle serait une bonne réponse ?")
        reponse[question] = input()
        print("Merci, je m'en souviendrai et maintenant ?")
    question = input()

print("À +")
