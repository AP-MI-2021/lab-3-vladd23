###########  problema 1  #############

def is_prime(num):
    '''
    Determina daca numarul dat este prim
    :param num:
    :return: 1 daca numarul este prim, 0 in caz contrar
    '''
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                return 0
        else:
            return 1
    else:
        return 0

def test_is_prime():
    assert is_prime(2) == 1
    assert is_prime(4) == 0
    assert is_prime(5) == 1
    assert is_prime(17) == 1
    assert is_prime(27) == 0

def all_elements_are_prime(l):
    '''
    determina daca toate numerele din lista sunt prime
    :param l:
    :return: True daca toate numerele din lista sunt prime, False in caz contrar
    '''
    for x in l:
        if is_prime(x) != 1:
            return False
    return True

def test_all_elements_are_prime():
    assert all_elements_are_prime([2,3,5]) == True
    assert all_elements_are_prime([1,2]) == False
    assert all_elements_are_prime([17,23,31]) == True
    assert all_elements_are_prime([4,6,8]) == False

def get_longest_all_primes(l):
    '''
    Functie care determina cea mai lunga subsecventa de numere prime din lista l
    :param l:
    :return: cea mai lunga subsecventa de numere prime din lista l
    '''
    subsecventa_maxima = []
    for i in range(len(l)):
        for j in range(i,len(l)):
            if all_elements_are_prime(l[i:j+1]) and len(l[i:j+1]) > len(subsecventa_maxima):
                subsecventa_maxima = l[i:j+1]

    return subsecventa_maxima

def test_get_longest_all_primes():
    assert get_longest_all_primes([1,2,3,4]) == [2,3]
    assert get_longest_all_primes([]) == []
    assert get_longest_all_primes([2,2, 4, 3, 3, 5, 8]) == [3, 3, 5]
    assert get_longest_all_primes([4,4,50]) == []


##########  problema 2  ############

def numar_divizori(x):
    '''
    Functie care determina numarul de divizori al unui numar
    :param x:
    :return: numarul de divizori al numarului x
    '''
    cont = 0
    for d in range(1, x + 1):
        if x % d == 0:
            cont = cont + 1
    return cont

def test_numar_divizori():
    assert numar_divizori(6) == 4
    assert numar_divizori(1) == 1
    assert numar_divizori(7) == 2
    assert numar_divizori(9) == 3

def acelasi_numar_divizori(l):
    '''
    Functie care determina daca toate numerele din lista data au acelasi numar de divizori
    :param l: lista de numere
    :return: True daca toate numerele din lista au acelasi numar de divizori, False in caz contrar
    '''
    nr_divizori = numar_divizori(l[0])
    for x in l:
        if numar_divizori(x) != nr_divizori:
            return False
    return True

def test_acelasi_numar_divizori():
    assert acelasi_numar_divizori([6,8]) == True
    assert acelasi_numar_divizori([2, 3,5,7]) == True
    assert acelasi_numar_divizori([1,2,3,4,5]) == False
    assert acelasi_numar_divizori([6,8,10]) == True

def get_longest_same_div_count(l):
    '''
    Functie care determina cea mai lunga subseventa ce indeplineste cerinta data
    :param l: lista de nr
    :return: Returneaza subsecventa de lungime maxima a carei numere au acelasi numar de divizori
    '''
    subsecventa_maxima = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if acelasi_numar_divizori(l[i:j+1]) and len(l[i:j+1]) > len(subsecventa_maxima):
                subsecventa_maxima = l[i:j+1]
    return subsecventa_maxima

def test_get_longest_same_div_count():
    assert get_longest_same_div_count([5,7,2, 4, 8, 10]) == [5,7,2]
    assert get_longest_same_div_count([]) == []
    assert get_longest_same_div_count([4,4,9,5,7,2]) == [4,4,9]
    assert get_longest_same_div_count([1,2,3,4]) == [2,3]

############  problema 3  ######################

def is_palindrome(x):
    '''
    Functie care determina daca un numar este palindrom
    :param x:
    :return: True daca numarul este palindrom, False in caz contrar
    '''
    invers = 0
    copie_x = x
    while copie_x != 0:
        ultima_cifra = copie_x % 10
        invers = invers * 10 + ultima_cifra
        copie_x = copie_x // 10

    if invers == x:
        return True
    else:
        return False

def test_is_palindrome():
    assert is_palindrome(123) == False
    assert is_palindrome(111) == True
    assert is_palindrome(12521) == True
    assert is_palindrome(12551) == False

def all_are_palindromes(l):
    '''
    Functie care determina daca toate numerele din lista sunt palindroame
    :param l: lista
    :return: True daca toate numerele sunt palindroame, False in caz contrar
    '''
    for x in l:
        if is_palindrome(x) is False:
            return False
    return True

def test_all_are_palindromes():
    assert all_are_palindromes([121,343,99]) == True
    assert all_are_palindromes([121,343,98]) == False
    assert all_are_palindromes([11,22,33]) == True
    assert all_are_palindromes([121, 990, 878, 929]) == False

def get_longest_all_palindromes(l):
    '''
    Functie care determina subsirul de lungime maxima cu proprietatea ca toate nr sunt palindroame
    :param l: lista
    :return: o lista ce contine sirul cu proprietatea dorita
    '''
    subsecventa_maxima = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if all_are_palindromes(l[i:j+1]) and len(l[i:j+1]) > len(subsecventa_maxima):
                subsecventa_maxima = l[i:j+1]
    return subsecventa_maxima

def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([12,33,232,434,10,19]) == [33,232,434]
    assert get_longest_all_palindromes([]) == []
    assert get_longest_all_palindromes([10,11]) == [11]
    assert get_longest_all_palindromes([12,343,1001,909, 56, 88, 99]) == [343,1001,909]


############ pentru meniu ##############

def all_function_test():
    test_is_prime()
    test_numar_divizori()
    test_get_longest_all_primes()
    test_get_longest_same_div_count()
    test_all_elements_are_prime()
    test_acelasi_numar_divizori()
    test_is_palindrome()
    test_all_are_palindromes()
    test_get_longest_all_palindromes()

def citire_lista():
    l = []
    n = int(input("Numarul de elemente din lista: "))
    for i in range(n):
        l.append(int(input("l[" + str(i) + "]= ")))

    return l

def print_menu():
    print("1. Citire date")
    print("2. Cea mai lunga secventa de numere prime")
    print("3. Cea mai lunga secventa de numere care au acelasi numar de divizori")
    print("4. Cea mai lunga secventa de numere care sunt palindroame")
    print("x. Iesire")


def main():
    all_function_test()
    l =[]
    while True:
        print_menu()
        optiune = input("Alegeti optiunea dorita: ")
        if optiune == "1":
            l = citire_lista()
        elif optiune == "2":
            print(get_longest_all_primes(l))
        elif optiune == "3":
            print(get_longest_same_div_count(l))
        elif optiune == "4":
            print(get_longest_all_palindromes(l))
        elif optiune == "x":
            break
        else:
            print("Alegeti alta optiune!")



if __name__ == '__main__':
    main()