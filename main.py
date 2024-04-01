import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#
# letter = data.letter
#
# print(letter)
#
# row_D = data[data.letter == "D"]
# print(row_D)
# print(row_D.index*2)

dictionary = {row.letter:row.code for (index,row) in data.iterrows()}
# print(dictionary)

user_name = input("Please insert a user name: \n").upper()

split_names = user_name.split()

for i in range(len(split_names)):
    new_list_i = [n.capitalize() for n in split_names[i]]
    new_list_2i = [dictionary[letter] for letter in new_list_i]

    # dictionary_2 = {letter:dictionary[letter] for letter in new_list_i}
    #
    # print(dictionary_2)

    # print(new_list_i)
    print(new_list_2i)
















# letters = data["letter"]
#
# print(letters)
#
# row = data[data.letter == "C"]

# print(row)

# print(type(data))

# print(dictionary)

# print(type(dictionary))

# dictionary = {key:value for (key,value) in data.items()}


# dictionary = {row.letter:row.code for (index,row) in data.iterrows()}

# print(dictionary)

# user_name = input("Please insert a user name: \n").lower()
#
# split_names = user_name.split()

# capitalize(): mayúscula la primera letra
# upper(): mayúsculas toda la cadena

# new_list = [n.upper() for n in split_names]
# print(new_list)

# for i in range(len(split_names)):
#     new_list_i = [n.capitalize() for n in split_names[i]]
#
# #
# #
# #     print(new_list_i)
#     print(new_list_2i)


