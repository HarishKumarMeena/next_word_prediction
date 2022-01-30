# Creating dictionary 
my_dictionary = {} 

#Taking input
user_input = input('> ')

#Printing length of string
words = user_input.split()
user_input_length = len(words)

print("Length of the input string: {}".format(user_input_length))

#Taking last word
last_word = words[user_input_length - 1]
print("The last word from the input: {}".format(last_word))

#opening dataset file
dataset = open("dataset.txt", "r")

#setting index to 0 to check the line number, no use in predecting the word
index = 0

#going through the file line by line
for line in dataset:
    print("\n")
    index += 1
    line_length = len(line.split())
    print("Line{}: {}, length:{}".format(index, line.strip(), line_length))
    
    #checking if string is present in line
    words_in_line = line.split()
    if last_word in words_in_line:
        position_of_word = words_in_line.index(last_word)
        print("Position of {} in this line: {}".format(last_word, position_of_word))
        if position_of_word  == line_length - 1:
            continue
        else:
            next_word = words_in_line[position_of_word + 1]
            if next_word in my_dictionary:
                my_dictionary[next_word] += 1
            else:
                my_dictionary[next_word] = 1
    else:
        continue


print("\n")
#checking if dictionary is empty
empty_or_not = not bool(my_dictionary)


#Key with maximum value
if empty_or_not == True:
    print("\nSorry we have insufficient dataset to predict 😶")
else:
    Keymax = max(zip(my_dictionary.values(), my_dictionary.keys()))[1]
    print("Suggested next word: {}".format(Keymax))

    
#priinting values  of dictionary
print("\n")
print(my_dictionary)