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

############ pentru meniu ##############

def all_function_test():
    test_is_prime()
    test_numar_divizori()
    test_get_longest_all_primes()
    test_get_longest_same_div_count()
    test_all_elements_are_prime()
    test_acelasi_numar_divizori()

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
    print("x. Iesire")


def main():
    all_function_test()
    while True:
        print_menu()
        optiune = input("Alegeti optiunea dorita: ")
        if optiune == "1":
            l = citire_lista()
        elif optiune == "2":
            print(get_longest_all_primes(l))
        elif optiune == "3":
            print(get_longest_same_div_count(l))
        elif optiune == "x":
            break
        else:
            print("Alegeti alta optiune!")



if __name__ == '__main__':
    main()