def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)


# spam = "local spam" : Ici, spam est une variable locale à la fonction do_local(). Elle n'affecte pas la variable spam dans la fonction englobante scope_test() ou la variable globale spam.

# nonlocal spam et spam = "nonlocal spam" : Ici, spam est déclarée comme non locale, ce qui signifie qu'elle fait référence à la variable spam dans la fonction englobante la plus proche, qui est scope_test(). Lorsque nous assignons "nonlocal spam" à spam, cela modifie la valeur de spam dans scope_test().

# global spam et spam = "global spam" : Ici, spam est déclarée comme globale, ce qui signifie qu'elle fait référence à la variable spam au niveau du module. Lorsque nous assignons "global spam" à spam, cela modifie la valeur de la variable globale spam.
