import re
from datetime import datetime
from difflib import SequenceMatcher
import time
now = datetime.now()
T1 = time.process_time()


file = 'EnglishWords.txt' #opens file
with open(file) as f:
    text = f.read() #reads from file
alt = text.split() #splits file into seperate lines

quit = False
option = None
while quit is False: #the condition is set to false so program loops
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
        if option != "0" and option != "1" and option != "2": #if options is not equal to the following
            raise Exception("Wrong option!")
    except Exception as exc:
        print("Wrong option!")
        continue

    if option == "0": #if option equal 0, do the following 
        print("program ended!")
        break
    if option == "1":
        print("\u250c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
              "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
              "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510")
        print("\u2502          L O A D  F I L E               \u2502")
        print("\u2502                                         \u2502")
        print("\u2502 Enter the filename then press [enter]   \u2502")
        print("\u2502                                         \u2502")
        print("\u251C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
              "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
              "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518 ")
        filename = input("\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500"
                      "\u2500\u2500\u2500\u2500 filename: ")
        with open(filename) as f:
            text_2 = f.read()
            text_2 = text_2.lower()
            sentence_2 = re.sub(r'[^a-zA-Z ]+', "", text_2) #gets rid of any non alphanumeric characters
            correct_2 = 0
            incorrect_2 = 0
            ignore = 0
            mark = 0
            add = 0
            wordList_2 = []
            f = open("checkMe2.txt", "a") #opens file 
            for word_1 in sentence_2.split():
                if word_1 in text.split():
                    f.write(word_1 + " ")
                    correct_2 += 1
                elif word_1 not in text.split():
                    incorrect_2 += 1
                    for i in range(0, 84094):
                            score1 = SequenceMatcher(None, word_1, alt[i]).ratio() #matches the ratio of the spelling of the words
                            if score1 >= 0.75:
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
                                    "\u2500\u2500\u2500\u2500 enter [y] or [n]: ")
                                if suggestions == "y" or suggestions == "Y":
                                    f.write(alt[i] + " ")
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

                                    if choice == "1":
                                        f.write("!" + word_1 + "! ")
                                        ignore += 1
                                        break
                                    elif choice == "2":
                                        f.write("?" + word_1 + "? ")
                                        mark += 1
                                        break
                                    elif choice == "3":
                                        f.write("*" + word_1 + "* ")
                                        add += 1
                                        with open("EnglishWords.txt", "a") as a:
                                            a.write("\n" + word_1)
                                        wordList_2.append(word_1)
                                        break
                                    choice = None
                                break

            file2 = open("checkMe2.txt","r+")
            lines = file2.readlines()
            contents = (now.strftime("%d/%m/%Y %H:%M:%S")+"\nNumber of words: " + str(len(wordList_2))+"\ncorrect words: " + str(correct_2)+"\nincorrect words: "+str(incorrect_2)+"\n   number ignored: " + str(ignore)+"\n   number marked: " + str(mark)+"\n   number added to dictionary: " + str(add)+"\n"+""+"\n")
            print("\n"+contents)
            file2.seek(0)
            file2.write(contents)
            for line in lines:
                file2.write("\n"+ line)
            file2.close()

    elif option == "2":
        words = input("Enter a sentence: ") #user enters a sentence
        words = words.lower()
        sentence = re.sub(r'[^a-zA-Z ]+', "", words)
        print(sentence)
        sentence = sentence.split()
        correct = 0
        incorrect = 0
        wordList = []
        for W in sentence:
            if W in text.split():
                print(W + ":" " spelt correctly")
                correct += 1
            else:
                print(W + ":" " not found in the dictionary")
                incorrect += 1
            wordList.append(W)
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
        Quit = False

T2 = time.process_time()
timer = (T2 - T1)
print("\nTime elapsed: ", timer * 1000000, " microseconds\n")

