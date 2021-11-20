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


# def text_lines(file):
#     file5 = open(file, "r")
#     print(file5.read())
#
# text_lines("countries.txt")

# file6 = open("text.txt", "r")
# content_list = list()
# for line in file6:
#     content_list.append(line)
# print(content_list)
# file6.close()
#
# with open('text.txt', 'r') as file:
#     print (file.readlines())


# def longest_word(filename):
#     with open(filename, "r") as f:
#         words = f.read().split()
#     print(words)
#     max_len = len(max(words, key = len))
#     return [word for word in words if len(word) == max_len]
# print(word)
# longest_word("text.txt")

# list = ("Nastka", "Monika", "Gosia", "Basia")
#
# def List_to_file(list):
#     with open("imiona.txt", "w+") as file:
#         for el in list:
#             file.write(str(el) + ", ")
#
# # new_file = open("imionka.txt", "r")
# # print(new_file.readlines())
#
# List_to_file(list)
#
# f = open('imiona.txt', 'r')
# print(f.closed)
# f.close()
# print(f.closed)

def file_opener(file):
    with open(file, "r") as f:
        words = f.read().split()
        # print(words)
        length = len(words)
        # print(length)
    return length

def seventh_line_length(file):
    with open(file, "r") as f:
            lines = f.readlines()
            list_length = len(lines)
            # print(lines)
            # print(list_length)
            new_lines = lines [0::7]
            # n = 1
            # while n < list_length:
            #     new_lines = f.readlines(n)
            #     n+=7
            print(new_lines)
            final_lenght_list = list()
            for line in new_lines:
                len_each_line = len(line.split())
                final_lenght_list.append(len_each_line)
            # each_line = line.split()
            # len_each_line = len(each_line)
            # for len_each_line [ : ,7]:
            #     print(len_each_line)
    return final_lenght_list

print(file_opener("imiona.txt"))
print(seventh_line_length("imiona.txt"))