#Sound Poetry Machine Friend (until I make a better name)
#By Gabe Raines
#2020

#Import Modules

#Import OS Module to use os.path.join to write file
import os

#Import Sys Module to use sys.exit to break infinite loop at end
import sys

#It's nice to be polite
name = input('Hello there! What is your name? ')
print('Hi ',name,'!',sep='')

print()

mood = input('How are you today? ')
print('I hear you!')

print()

#Getting down to business
print("Now let's get started.")
print("I am your Sound Poetry Machine Friend!  Or SPMF for short.")
print("I can take in pieces of language and make poems for you, or help you make poems.")

print()

#Consent is always important
ready = input("Are you ready? ")
if ready in ['n', 'N', 'no', 'No', 'NO']:
    print("No worries!  See you later!")
    exit(0)

def poetry_generator():
    print()
    print("OK!  Let's do it!")
    print()

    #Get the input
    syl1 = input("Let's start with a single syllable: ")
    syl2 = input("Perfect, now a second syllable, please: ")
    syl3 = input("Awesome, one more and we'll be ready to go: ")

    print()

    print("Great! Now I am making a sound poem for you.")

    print()

    #Poetic Form 1
    #Try multipliers var * 3 etc

    # f1l1 = syl1, syl1, syl2
    # f1l2 = syl2, syl1, syl2, syl3, syl2
    # f1l3 = syl1, syl3, syl1, syl3, syl1
    # f1l4 = "\n"
    # f1l5 = syl3, syl3, syl2, syl2, syl1
    # f1l6 = syl2, syl3, syl1, syl1, syl1
    # f1l7 = syl3, syl1, syl2
    # f1l8 = syl1, syl2, syl3
    # f1l9 = syl1, syl2
    #
    # print(f1l1)
    # print(f1l2)

    print(syl1, syl1, syl2)
    print(syl2, syl1, syl2, syl3, syl2)
    print(syl1, syl3, syl1, syl3, syl1)
    print()
    print(syl3, syl3, syl2, syl2, syl1)
    print(syl2, syl3, syl1, syl1, syl1)
    print(syl3, syl1, syl2)
    print(syl1, syl2, syl3)
    print(syl1, syl2)

    print()

    print("There you go!")

    print()

    write = input("Would you like to write it to a file? ")
    if write in ['n', 'N', 'no', 'No', 'NO']:
        print()
        print("No worries!")

    save_path = os.path.expanduser("~/Desktop")
    name_of_file = syl1+"-"+syl2+"-"+syl3
    completeName = os.path.join(save_path, name_of_file+".txt")

    file = open(completeName, "w")

    print()

    print ("OK! File written to desktop!")

    print()

    again = input("Would you like to make another one? ")
    if again in ['n', 'N', 'no', 'No', 'NO', 'Nope', 'No thanks', 'No thank you']:
        print()
        print("OK!  See you later, friend!")
        sys.exit(0)

    poetry_generator()

poetry_generator()



