import re
from datetime import datetime
from difflib import SequenceMatcher
import time
now = datetime.now() #gets the current date and time
T1 = time.process_time() #starts a timer


file = 'EnglishWords.txt'    #engl
with open(file) as f:       #opens text file
    text = f.read()     #reads from text file
alt = text.split()   #splits text in text file into seperate lines

quit = False
option = None
while quit is False:   #condition is True so the loop will run
    option = None
    try:
        print("\u250c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
              "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
              "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510")
        print("\u2502        S P E L L  C H E C K E R         \u2502")
        print("\u2502 1. Check a file                         \u2502 \n\u2502 2. Check a sentence                     "
              "\u2502 \n\u2502""                                         \u2502\n\u2502 0. Quit                           "
              "      \u2502")
        print("\u251C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
              "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
              "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518 ")
        option = input("\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
                        "\u2500\u2500\u2500\u2500 Enter a choice: ")
        if option != "0" and option != "1" and option != "2":       #if user input does not equal 0, 1 or 2 then the program would do the following
            raise Exception("Wrong option!")        #tells the program that there is an incorrect input
    except Exception as exc:
        print("Wrong option!")
        continue        #loops back to the start

    if option == "0":
        print("program ended!")
        break       #stops the whole program is user input is "0"
    if option == "1":
        print("\u250c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
              "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"      
              "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510")                         #unicode for a straight horizontal line
        print("\u2502          L O A D  F I L E               \u2502")
        print("\u2502                                         \u2502")
        print("\u2502 Enter the filename then press [enter]   \u2502")
        print("\u2502                                         \u2502")
        print("\u251C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
              "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
              "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518 ")
        filename = input("\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
                      "\u2500\u2500\u2500\u2500 filename: ")
        with open(filename) as f:       #opens a file
            text_2 = f.read()
            text_2 = text_2.lower()     #converts all the characters in the text file to lower case
            sentence_2 = re.sub(r'[^a-zA-Z ]+', "", text_2)     #gets rid of any non alpha numeric characters
            correct_2 = 0
            incorrect_2 = 0
            ignore = 0
            mark = 0
            add = 0
            wordList_2 = []     #creates an empty list
            f = open("checkMe2.txt", "a")
            for word_1 in sentence_2.split():       #loops through every word in the file
                if word_1 in text.split():      #if word from checkMe text file is in EnglishWords text file
                    f.write(word_1 + " ")       #then write the word to a new text file "checkMe2"
                    correct_2 += 1
                elif word_1 not in text.split():        #if word not it dictionary
                    incorrect_2 += 1
                    for i in range(0, 84094):       #loops through every word in the EnglishWords file
                            score1 = SequenceMatcher(None, word_1, alt[i]).ratio()      #compares the wrong word with each word in EnglishWords file and gives a ratio of how similar the words are
                            if score1 >= 0.75:      #if the ratio similarity of the word in greater than 0.75
                                print("\u250c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
                                    "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
                                    "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510")
                                print("\u2502          W O R D  N O T  F O U N D      \u2502")
                                print("\u2502                                         \u2502")
                                print("\u2502 " + word_1 ,(" "*(23-len(word_1))),"               \u2502")
                                print("\u2502 Did you mean:                           \u2502")
                                print("\u2502 " + alt[i] ,(" "*(23-len(alt[i]))),"               \u2502")
                                print("\u2502                                         \u2502")
                                print("\u251C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
                                    "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
                                    "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518 ")
                                suggestions = input(
                                    "\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
                                    "\u2500\u2500\u2500\u2500 enter [y] or [n]: ")      #asks for user input if the meant to type the suggested word
                                if suggestions == "y" or suggestions == "Y":
                                    f.write(alt[i] + " ")       #writes the suggested word to "checkMe2 text file
                                    break
                                while suggestions == "n" or suggestions == "N":
                                    choice = None
                                    try:
                                        print("\u250c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
                                              "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
                                              "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510")
                                        print("\u2502          W O R D  N O T  F O U N D      \u2502")
                                        print("\u2502                                         \u2502")
                                        print("\u2502 1. ignore word.                         \u2502")
                                        print("\u2502 2. Mark the word as incorrect           \u2502")
                                        print("\u2502 3. Add word to dictionary.              \u2502")
                                        print("\u2502                                         \u2502")
                                        print(
                                            "\u251C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
                                            "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
                                            "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518 ")
                                        choice = input("\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
                                            "\u2500\u2500\u2500\u2500 enter choice: ")
                                        if choice != "1" and choice != "2" and choice != "3":
                                            raise Exception("Wrong option!")
                                    except Exception as exc:
                                        print("Wrong option!")
                                        continue

                                    if choice == "1":       #if user choice = 1
                                        f.write("!" + word_1 + "! ")      #write the word to the text file with exclamation marks around the word
                                        ignore += 1
                                        break
                                    elif choice == "2":
                                        f.write("?" + word_1 + "? ")
                                        mark += 1
                                        break
                                    elif choice == "3":     #if user choice = 3
                                        f.write("*" + word_1 + "* ")
                                        add += 1
                                        with open("EnglishWords.txt", "a") as a:    #open the englishWords file to append extra data to it
                                            a.write("\n" + word_1)
                                        wordList_2.append(word_1)       #add the new word to the end of EnglishWords text file
                                        break
                                    choice = None
                                break       #breaks for loop

            file2 = open("checkMe2.txt","r+")   #reads from checkMe2 text file
            lines = file2.readlines()
            contents = (now.strftime("%d/%m/%Y %H:%M:%S")+"\nNumber of words: " + str(len(wordList_2))+"\ncorrect words: " + str(correct_2)+"\nincorrect words: "+str(incorrect_2)+"\n   number ignored: " + str(ignore)+"\n   number marked: " + str(mark)+"\n   number added to dictionary: " + str(add)+"\n"+""+"\n")
            #the variable contains the time and date the program was executed along with how my words was enetered by the user, how many correct words etc.
            print("\n"+contents)
            file2.seek(0)       #goes to the top of a file
            file2.write(contents)   #write out the contents to the file
            for line in lines:      #for every line in file2
                file2.write("\n"+ line)
            file2.close()       #close file2

    elif option == "2":
        words = input("Enter a sentence: ")
        words = words.lower()
        sentence = re.sub(r'[^a-zA-Z ]+', "", words) #gets rid of any non alpha numeric characters
        print(sentence)
        sentence = sentence.split()     #words in the file is split into seperate lines so its easy for the program to read from
        correct = 0
        incorrect = 0
        wordList = []       #creates an empty list
        for W in sentence:      #loops through each word in the sentence entered by the user
            if W in text.split():
                print(W + ":" " spelt correctly")
                correct += 1
            else:
                print(W + ":" " not found in the dictionary")
                incorrect += 1
            wordList.append(W)      #adds each word from the sentence the user entered into a list
        print("")
        print("number of words: " + str(len(wordList)))
        print("number of correctly spelt words: " + str(correct))
        print("number of incorrectly spelt words: " + str(incorrect))
        option = None
    question = input(str("Press q [enter] to quit or any other key [enter] to go again:"))
    if question == "q":
        print("program ended!")
        break
    else:
        Quit = False     #if the user input is not "q" to quit the program then it will loop back to the start

T2 = time.process_time()        #starts a second timer
timer = (T2 - T1)       #time taken for the program to process
print("\nTime elapsed: ", timer * 1000000, " microseconds\n")

