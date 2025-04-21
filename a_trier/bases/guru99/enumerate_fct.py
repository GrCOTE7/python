n='lionel'
print(*enumerate(n,7), '\n')

my_dict = {"a": "PHP", "b":"JAVA", "c":"PYTHON", "d":"NODEJS"}
print('Dict:', my_dict, '\n\nenumerate(Dict) :', *enumerate(my_dict), '\n')
for i in enumerate(my_dict):
  print("%s \nClé de l'énumérate : %s\nValue (Clé du tuple) : %s\n %s"
        % (i, i[0], i[1], my_dict[i[1]]))
  # print(i, my_dict[i])
