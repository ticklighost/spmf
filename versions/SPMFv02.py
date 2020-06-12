#Sound Poetry Machine Friend
#By Gabe Raines
#2020

#Import OS Modules
# os to use os.path.join to write file
# sys to use sys.exit to break loop and end program
# random to generate random numbers to get new form each time
import os, sys, random, pyttsx3

#Define global variables
syl1 = ""
syl2 = ""
syl3 = ""
poem = ""
rnd = ""
poemlist = ""

#Saying hello
def greeting():
    print()
    #It's nice to be polite
    name = input('Hello there! What is your name? ')
    print('Hi ',name,'!',sep='')

    print()

    #The friend has no time for drama
    mood = input('How are you today? ')
    print('I hear you!')

    print()

    #Getting down to business
    print("Now let's get started.")
    print("I am your Sound Poetry Machine Friend!  Or SPMF for short.")
    print("I can take in pieces of language and make poems for you, or help you make poems.")

    print()

#Consent is always important
def consent():
    ready = input("Are you ready? ")
    if ready in ['n', 'N', 'no', 'No', 'NO', 'Nope', 'No thanks', 'No thank you', 'No thx', 'no thx', 'nah']:
        print()
        print("No worries!  See you later!")
        exit(0)

#Be kind
def affirmation():
    print()
    print("OK!  Let's do it!")
    print()

#Get the goods
def syl():
    global syl1
    global syl2
    global syl3
    syl1 = input("Let's start with a single syllable: ")
    syl2 = input("Perfect, now a second syllable, please: ")
    syl3 = input("Awesome, one more and we'll be ready to go: ")
    print()

#Be considerate
def reassure1():
    print("Great! Now I am making a sound poem for you.")
    print()

def randomizer():
    global rnd
    rnd = random.randint(1, 3)

def makeList():
    global poemlist
    poemlist = [syl1, syl2, syl3]

#The veggie meat of the program
#Form 1
def poetry1():
    global poem
    poem = (f"{syl1} {syl1} {syl2}\n"
            f"{syl2} {syl1} {syl2} {syl3} {syl2}\n"
            f"{syl1} {syl3} {syl1} {syl3} {syl1}\n"
            f"\n"
            f"{syl3} {syl3} {syl2} {syl2} {syl1}\n"
            f"{syl2} {syl3} {syl1} {syl1} {syl1}\n"
            f"{syl3} {syl1} {syl2}\n"
            f"{syl1} {syl2} {syl3}\n"
            f"{syl1} {syl2}\n")

    print(poem)
    return(poem)

#Form 2
def poetry2():
    global poem
    poem = (f"{syl2} {syl1} {syl2} {syl3} {syl3}\n"
            f"{syl1} {syl1} {syl3}\n"
            f"{syl2} {syl3} {syl1} {syl1} {syl2}\n"
            f"{syl3} {syl1} {syl1} {syl2} {syl3}\n"
            f"\n"
            f"{syl1}\n"
            f"{syl1} {syl2} {syl1} {syl2} {syl3}\n"
            f"{syl3} {syl3} {syl2}\n"
            f"{syl3} {syl1}\n")

    print(poem)
    return(poem)

#Form3
def poetry3():
    global poem
    poem = (f"{syl3} {syl3} {syl2} {syl2} {syl2} {syl1} {syl2}\n"
            f"{syl2} {syl1} {syl1} {syl2} {syl2} {syl3} {syl2}\n"
            f"{syl1} {syl3} {syl3} {syl1} {syl3} {syl3} {syl1}\n"
            f"\n"
            f"{syl3} {syl3} {syl2} {syl1} {syl2} {syl2} {syl1}\n"
            f"{syl2} {syl1} {syl2} {syl3} {syl3} {syl2} {syl2}\n"
            f"{syl2} {syl3} {syl2} {syl3} {syl1} {syl1} {syl1}\n"
            f"\n"
            f"{syl3} {syl1} {syl1} {syl3} {syl1} {syl1} {syl2}\n"
            f"{syl2} {syl2} {syl3} {syl2} {syl2} {syl2} {syl3}\n"
            f"{syl1} {syl3} {syl3} {syl1} {syl1} {syl1} {syl1}\n")

    print(poem)
    return(poem)

#Contractor MacDonald, who built the great subway, is proud of it
def reassure2():
    print("There you go!")
    print()

#Offer to read it aloud
def r4u():
    aloud=input("Would you like me to read it for you? ")
    if aloud in ['n', 'N', 'no', 'No', 'NO', 'Nope', 'No thanks', 'No thank you', 'No thx', 'no thx', 'nah']:
        print()
        print("OK! No problem!")
        print()
        fileQ()

#Text-to-Speech
def tts():
    voiceEngine = pyttsx3.init()
    voiceEngine.setProperty('rate', 125)
    engine = pyttsx3.init()
    engine.say(poem)
    engine.runAndWait()
    print()

#Keep it for posterity
def fileQ():
    write = input("Would you like to write it to a text file? ")
    if write in ['n', 'N', 'no', 'No', 'NO', 'Nope', 'No thanks', 'No thank you', 'No thx', 'no thx', 'nah']:
        print()
        print("No worries!")
        print()
        playagain()

#Flip those bits
def toFile():
    save_path = os.path.expanduser("~/Desktop")
    name_of_file = syl1+"-"+syl2+"-"+syl3
    completeName = os.path.join(save_path, name_of_file+".txt")

    file = open(completeName, "w")
    file.write(str(poem))
    file.close

    print()
    print ("OK! File written to desktop!")
    print()

#You spin me right round baby right round
def playagain():
    while True:
        again = input("Would you like to make another one? ")
        if again in ['n', 'N', 'no', 'No', 'NO', 'Nope', 'No thanks', 'No thank you', 'No thx', 'no thx', 'nah']:
            print()
            print("OK!  See you later, friend!")
            sys.exit(0)
        else:
            affirmation()
            syl()
            reassure1()
            randomizer()
            makelist()

            if rnd == 1:
                poetry1()

            if rnd == 2:
                poetry2()

            if rnd == 3:
                poetry3()

            reassure2()
            r4u()
            tts()
            fileQ()
            toFile()
            playagain()

#Calling the functions in order
greeting()
consent()
affirmation()
syl()
reassure1()
randomizer()
makeList()

#randomize the poetic form chosen
if rnd == 1:
    poetry1()

if rnd == 2:
    poetry2()

if rnd == 3:
    poetry3()

reassure2()
r4u()
tts()
fileQ()
toFile()
playagain()




