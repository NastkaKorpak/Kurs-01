# file = open("sonety.txt","r")
# file2 = open("countries.txt","w+")
# countries_and_capitals = {"Poland" : "Warsaw", "Hungary" : "Budapest", "Czech Republic" : "Prague", "Germany" : "Berlin" }
# print(countries_and_capitals)
# for country, capital in countries_and_capitals.items():
#     file2.write("The capital of this country: " + country + " is " + capital+ "\n")
# file2.close()
# file3 = open("countries.txt","r")
# for line in file3.readlines():
#     print(line.strip())
# file3.close()

# file4 = open("witaj.txt", "w+")
# file4.write ("Cześć" +"/n" + "Jak masz na imię?")
# pos = file4.tell()
# print("Aktualna pozycja to: " + str(pos))
# line = file4.readline()
# print("Czytaj linię: >" + line + "<")
# pos2 = file4.tell()
# print("Aktualna pozycja to: " + str(pos2))
# file4.close()


def text_lines(file):
    file5 = open(file, "r")
    print(file5.read())

text_lines("countries.txt")
