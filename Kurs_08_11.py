# print ("Hello world")

# def simple_function():
#     print('Hello world!')
#     print('Wikipedia')
#
#
# simple_function()
#
# def my_function ():
#   return 3+3
#
#
# print( my_function() )

# def add(x, y):
#     '''Dokumentacja funkcji dodawania'''
#     return x + y
#
#
# print(add(100, 1))
# help (add)

# def fibbonaci_numbers (n):
#     """zwraca liczby Fibonnaciego mniejsze od n"""
#     wynik = []
#     a, b = 0, 1
#     while a < n:
#         wynik.append (a)
#         a, b = b, a + b
#
#
#     return wynik
#
# x = fibbonaci_numbers (24)
# print(x)
# print(fibbonaci_numbers.__doc__)

# def fibbonaci_numbers(n):
#     ''' zwraca liczby Fibonacciego mniejsze od n '''
#     wynik = []
#     a, b = 0, 1
#     while a < n:
#         # while len(wynik) < n:
#         wynik.append(a)
#         a, b = b, a + b
#     return wynik

# def dlugosc(str1):
#     """zwraca długość łańcucha"""
#     count = 0
#     for litera in str1:
#         count +=1
#     return count
#
#
# print(dlugosc("LOL"))
#
# def string_length(str1):
#     count = 0
#     for char in str1:
#         count += 1
#     return count
# print(string_length('Python'))

# def suma (n):
#     x = 0
#     for el in n:
#         x += el
#     return x
# print (suma ([1,2,3,4]))

# def mnozenie(lista):
#     """zwraca wynik mnożenia wszystkich elemntów z listy"""
#     wynik = lista[0]
#     for el in lista[1:]:
#         wynik *= el
#     return wynik
#
# print(mnozenie([2,3,4]))

# def maksimum(lista):
#     """zwraca maksymalną liczbę z listy"""
#     max = lista[0]
#     for el in lista[1:]:
#         if el > max:
#             max = el
#     return max
#
# print(maksimum([-10,-100,-5000,-1]))

#Napisz funkcję w Pythonie, który zlicza liczbę znaków (częstotliwość znaków) w ciągu.

def zliczanie (string):
    """zlicza liczbę znaków (częstotliwość znaków) w ciągu"""
    wynik = {}
    for litera in string:
         klucze = wynik.keys()
         print(klucze)

         if litera in klucze:
             wynik [litera] += 1
         else:
             wynik [litera] = 1
    return wynik
print(zliczanie("Nastka"))



def letter_count (phrase):
    result = {}
    for character in phrase:
        if character in result:
            result[character] = result[character] + 1
        else:
            result[character] = 1
        #print(result)
    return result

print (letter_count("Nastka"))

# Napisz funkcję w Pythonie, który zlicza ciągi znaków, w których długość ciągu wynosi 2 lub więcej, a pierwszy i ostatni znak są takie same z podanej listy ciągów.

# def liczba_ciagow (lista):
#     wynik = 0
#     for element in lista:
#         if len(element) >= 2 and element[0] == element[-1]:
#             wynik += 1
#     return wynik
# print (liczba_ciagow(["abc" , "XYZ", "aaa", "1231"]))

#Napisz funkcję w Pythonie, aby uzyskać listę posortowaną w porządku rosnącym według ostatniego elementu w każdej krotce z podanej listy niepustych krotek.
# lista = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# lista.sort()
# print(lista)
# def drugi_element (krotka):
#     return krotka[-1]
#
#
# def sort(lista):
#     return sorted(lista,key=drugi_element)
# print(sort(lista))

# def lancuch(string):
#     if len(string) < 2:
#         print(" ")
#     else:
#         print(string[:2] + string[-2:])
#
# lancuch("kot")

# def silnia(n):
#        if n!=1:
#         wynik = n*silnia(n-1)
#         return wynik
#        else:
#         wynik = 1
#         return wynik
#
# print(silnia(3))

#Rekurencyjny ciąg Fibonacciego

# def ciag_fibonnaciego(n):
#     if n >= 2:
#         return ciag_fibonnaciego(n-2) + ciag_fibonnaciego(n-1)
#     else:
#         return n
#
#
# print(ciag_fibonnaciego(12))