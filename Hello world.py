# print ("Hello world")
# print (2+2)
# x = "Nastka"
# print (x)
# print (type (x))
# y = 3.559
# print (round (y))
# print (int (y))
# i = 2
# print ( type ( i ))
# f = 2.71828
# print ( type (f))
# c = 0.5 +1j
# print ( type (c))
# print (float (i), " ", int (f), " ", c)
# a = 2 > 1
# print (a)
# print (type  (a))
# znak = "A"
# print (znak)
# print ( type (znak))
# print (znak [:])
# napis = "koteczek"
# print (napis [::2])
# napis = "Ala ma kota"
# print (napis [:10]+ "y")
# zmienna = 127
# print (zmienna)
# print ( type (zmienna))
#
# str1 = "kalendar"
# sr_znaki = len (str1)
# print (sr_znaki)
# print (str1 [(int(sr_znaki/2))-1:int(sr_znaki/2)+2])
# s1 = "FullStack"
# s2 = "Python"
# print ("Ciąg pierwszy to: " + s1)
# print ("Ciąg drugi to: " + s2)
# srodek1 = int(len(s1)/2)
# print (srodek1)
# nowe_slowo= s1[:srodek1] + s2 + s1 [srodek1:]
# print ("Twoje nowe slowo to: "+ nowe_slowo)
# s1 = "America"
# s2 = "Japan"
# print ("dwa oryginalne ciągi to: " + s1 +" i "+ s2)
# srodek1 = int(len(s1)/2)
# srodek2 = int (len(s2)/2)
# print ("Twoje nowe slowo to: "+ s1[0] + s2[0] +s1[srodek1:srodek1+1]+ s2 [srodek2:srodek2+1] + s1 [-1] + s2 [-1] )
# str1 = "Python"
# print ("Twój oryginalny ciąg to: " + str1)
# str2 = str1 [::-1]
# print (str2)
# lista = [1, 2, 3, 4, -5, 6, -10]
# print (lista)
# print( type (lista))
# liczby = [0.1, 0.2, 0.3, 4.5, -7.3, 6.87, 10]
# print (liczby)
# print( type (liczby))
# lista = [1, "Berta", 3, 4, -5, "kot", -10.75, 3.14]
# print (lista [1:6])
# print(lista[2:6:2])
# lista.append ("zebra")
# print (lista)
# lista.insert (2, "zebra")
# print (lista)
# print (lista.count('zebra'))
# imiona = ["łukasz", "michał", "nastka", "paweł", "joanna", "Kamil", "magdalena", "Elżbieta"]
# print(imiona)
# print (len(imiona))
# #imiona.sort()
# imiona2 = sorted (imiona)
# print(imiona2)
# slownik =  { "ala": "kot", "ola": 1 , "brainer": True}
# print(slownik)
# tel = {}
# print (tel)
# tel = {'Maja': 500456 , 'Jasio': 343455}
# print (tel)
# print(type(tel))
# tel ['Ola'] = 3024127
# print (tel)
# del tel['Maja']
# print (tel)
# tel = dict([('Jan', 4139277), ('Kazimierz', 4126327)])
# print (tel)
# c = {x: x**2 for x in (2, 4, 6)}  # {2: 4, 4: 16, 6: 36}
# print(c)
#
# print ("Cześć")
# #l1 = float(input ("podaj pierwszą liczbę: "))
# #l2 = float(input ("podaj drugą liczbę: "))
# #print ("wynik dzielenia: " , l1/l2)
# #print ("reszta z dzielenia: " , l1%l2)
# #print ("wynik dzielenia całkowitego: " , l1//l2)
#
# #punkty = int (input ("podaj liczbę punktów: "))
# if punkty >=90:
#     ocena = '5'
# elif punkty >=75:
#     ocena = '4'

# x = 8
# y = 15
# if x>3 or y%2==0:
#     print ("Co najmniej jeden z warunków jest spełniony")
# if x<=3 and y%2!=0:
#     print ("Żaden warunek nie jest spełniony")

# niepusta_wartosc = 0 or 0.0 or "" or [] or "test" or [123]
# print (niepusta_wartosc)
#
# x = int(input("Podaj x:" ))
# print (x>3 and x<10)

# x = float(input("Podaj x:" ))
# print (x>4 or x<3)
#
# x = float(input("Podaj x:" ))
# print (not (x>3 and x<10))

# string = "kot"
# for litera in string:
#     print ("litera: ", litera)

# imiona = ["Anastazja", "Tomasz" , "Magdalena", "Michał", "Paweł", "Paweł", "Elżbieta", "Joanna", "Michał", "Łukasz", "Kamil", "Marcin", "Jakub", "Natalia"]
# print(imiona.sort())
# kobieta = 0
# for imię in imiona:
#     if imię[-1] == "a":
#         kobieta +=1
#         print ("kobieta")
# print (kobieta)

# print("Przykład range() w Pythonie")
# print("Uzyskaj liczby z zakresu od 0 do 5")
# for i in range(0,7,2):
#     print(i, end=' - ')
# print ( list (range(0,7,2)))
#
# for i in range(5):
#     print(i, end= " - ")
# else:
#     print ("Gotowe!")
#
# liczby = list()
# i = 1
# while i < 11:
#     liczby.append(i)
#     i += 1
# print (liczby) # [2, 4, 6, 8, 10]
#
# lines = list()
# print('Wprowadź tekst po linijce.')
# print('Żeby zakończyć wprowadź pustą linię.')
# line = input('Następna linijka: ')
# while line != '':
#     lines.append(line)
#     line = input('Następna linijka: ')  # reset
# print(lines)

# l1 = float (input ("Podaj pierwszą liczbę: "))
# l2 = float (input ("Podaj drugą liczbę: "))
# max = int (max (l1,l2))
# min = int (min (l1,l2))
# print ("Max = ", max)
# print ("Min = ", min)
# for num in range (min,0,-1):
#     if l1%num ==0 and l2%num ==0:
#      print (num)
#     break
#
a = "Code Brainers"
b = 317
print("a: {}, b: {}".format(a,b))
b, a = a, b
print("a: {}, b: {}".format(a,b))
lista = list ()
for num in range (1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        lista.append(str(num))
print (" ; ". join (lista))
