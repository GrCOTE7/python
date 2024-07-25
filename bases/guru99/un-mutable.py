print('Mutable:\n')
mut_list = [1, 2, 3]
print(f"The list in Python %s{' '*8}→ %d"% (mut_list, id(mut_list)))
mut_list[0] = 'Guru99'

print("The list in Python after list[0] = 'Gurru99'")
print("The list in Python %s → %d"% (mut_list, id(mut_list)))

print('-'*57)

print('\nImmutable:\n')
a=1
print("Variable a: %d → Id: %d" % (a, id(a)))
a=2
print ("%s" % ('a=2'))
print("Variable a: %d → Id: %d" % (a, id(a)))
