# -*- coding: utf-8 -*-

head = """
################################################################
           _____                          _____                 
          |  __ \                        / ____|                
          | |__) |_ _ ___ ___   ______  | |  __  ___ _ __       
          |  ___/ _` / __/ __| |______| | | |_ |/ _ \ '_ \      
          | |  | (_| \__ \__ \          | |__| |  __/ | | |     
          |_| _ \__,_|___/___/____       \_____|\___|_| |_|     
             | |           |___  /             | |              
             | |__  _   _     / / ___  ___  ___| | ____ _       
             | '_ \| | | |   / / / _ \/ _ \/ __| |/ / _` |      
             | |_) | |_| |  / /_|  __/  __/ (__|   < (_| |      
             |_.__/ \__, | /_____\___|\___|\___|_|\_\__,_|      
                     __/ |                                      
                    |___/                                       


                   ##########################                   
                   #### Team Deep PØison ####                   
                   ##########################                   
                   ##                      ##                   
                   ##  Code : - Zeecka     ##                   
                   ##                      ##                   
                   ##########################                   


################################################################
"""
print(head)

import os
import time
import datetime
import sys

### Default Values ###

ARGMOD = True  # allow cmd line mode from shell
printlog = False  # use only for debug (less time when disabled)

lMin = 6  # Min size (included)
lMax = 12  # Max size (included)

fileToSave = os.path.expanduser("~/Desktop/Passgen_" + str(int(time.time())) + ".txt")
startList = ["word1", "word2"]
wordStart = ""  # The generated words must start with
wordEnd = ""  # The generated words must end with

format_Ab = False  # add 1st letter upper-case
format_AB = False  # add upper-case word
format_ab = False  # add lower-case word
format_BA = False  # add reverse upper-case word
format_ba = False  # add reverse lower-case word
format_Ba = False  # add reverse with 1st letter upper-case
format_L33T_5P34K = False  # Add "L33T 5P34K" (leet speak) language
leet_j = True  # J --> 1 for leet speak

extra_chars = "0123456789.-"  # Extra char to Add at the end of the word
nbExtra_chars = 0  # Number of max extra char

""" Pre set of extra char """
# extra_chars = ""
# extra_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# extra_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# extra_chars = "abcdefghijklmnopqrstuvwxyz"
# extra_chars = "abcdefghijklmnopqrstuvwxyz0123456789"
# extra_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&'()*+,-./0123456789:;<=>?@[\]^_`{|}~\""

maxDisplay = -1  # Max displayed words, put -1 for printing all of them (may take time & memory)

if (ARGMOD):
    if (len(sys.argv) <= 1 or "-h" in sys.argv):  # Print Demo
        print(
            """*************************************************************************
            Passgen is on command line mode, 
            please set ARGMOD to False or use the following command
            *************************************************************************
                    -m : Min Size for the generated words
                    -M : Max Size for the generated words
                    -o : Ouput file
                    -ws : Word Start (each words will start with)
                    -we : Word End (each words will end with)
                    -i : Input file, each line will be add to the start list as a Word
                    -w : Input words, MUST BE THE LAST ARG
            *************************************************************************
            
            *************************************************************************
                  Words Options :
            *************************************************************************
                    -ab : add lowercase words
                    -AB : add UPPERCASE words
                    -Ab : add lowercase words with uppercase first letter 
                    -ba : add reverse word in lowercase
                    -Ba : add reverse word in lowercase with uppercase first letter
                    -BA : add reverse word in UPPERCASE
                    -L337 : add word in L33T 5P34K
            
            *************************************************************************
            Examples :
            *************************************************************************
            
            python passgen.py -m 5 -M 12 -w foo bar abc zeecka words nice
            
            python passgen.py -m 4 -we @live.com -i inputfile.txt
            
            python passgen.py -M 15 -ws Alex -we .fr -i inputfile.txt
            
            python passgen.py -M 10 -i inputfile.txt -o ouputfile.txt
            
            python passgen.py -m 5 -M 7 -i inputfile.txt -ab -AB -L337
            
            *************************************************************************""")
        exit(0)
    else:
        try:
            startList = []
            if ("-m" in sys.argv):  # Min Size
                lMin = int(sys.argv[sys.argv.index("-m") + 1])
            if ("-M" in sys.argv):  # Max Size
                lMax = int(sys.argv[sys.argv.index("-M") + 1])
            if ("-o" in sys.argv):  # Output file
                fileToSave = (sys.argv[sys.argv.index("-o") + 1])
            if ("-ws" in sys.argv):  # Word Start
                wordStart = (sys.argv[sys.argv.index("-ws") + 1])
            if ("-we" in sys.argv):  # Word End
                wordEnd = (sys.argv[sys.argv.index("-we") + 1])
            if ("-i" in sys.argv):  # Input file
                fileToImport = (sys.argv[sys.argv.index("-i") + 1])
                with open(fileToImport) as f:
                    for line in f:
                        startList.append(line.replace("\n", ""))
            if ("-w" in sys.argv):  # Input words
                for i in range(sys.argv.index("-w") + 1, len(sys.argv)):
                    startList.append(sys.argv[i])
            if ("-Ab" in sys.argv):
                format_Ab = True  # add 1st letter upper-case
            if ("-Ab" in sys.argv):
                format_AB = True  # add upper-case word
            if ("-ab" in sys.argv):
                format_ab = True  # add lower-case word
            if ("-BA" in sys.argv):
                format_BA = True  # add reverse upper-case word
            if ("-ba" in sys.argv):
                format_ba = True  # add reverse lower-case word
            if ("-Ba" in sys.argv):
                format_Ba = True  # add reverse with 1st letter upper-case
            if ("-L33T" in sys.argv):
                format_L33T_5P34K = True  # Add "L33T 5P34K" (leet speak) language

        except:
            print("Error during parsing arguments, please verify syntax (python " + os.path.basename(__file__) + " -h)")

if (lMin > lMax):
    print("Min size can't be > than Max size")
    exit(0)
print(startList)
print("Start word count: " + str(len(startList)))
print("Generating list with size [" + str(lMin) + ";" + str(lMax) + "]")

""" First of all, add all word Foo, FOO, foo, OOF, oof, Oof, Bar, BAR, bar, RAB, rab, Rab, bAr """

print("Generating start list with option :")
if (format_Ab):
    print("     *> Ab format")
if (format_AB):
    print("     *> AB format")
if (format_ab):
    print("     *> ab format")
if (format_BA):
    print("     *> BA format")
if (format_ba):
    print("     *> ba format")
if (format_Ba):
    print("     *> Ba format")
if (format_L33T_5P34K):
    print("     *> L33T 5P34K format")
if (not (format_Ab or
         format_AB or
         format_ab or
         format_BA or
         format_ba or
         format_Ba or
         format_L33T_5P34K)):
    print("     *> No Option")
print("")

temp_list = []
for elt in startList:
    if format_Ab:
        if (len(elt) > 1):
            if printlog:
                print(elt[0].upper() + elt[1::].lower())
            temp_list.append(elt[0].upper() + elt[1::].lower())
        elif elt[0].upper() not in temp_list:
            if printlog:
                print(elt[0].upper())
            temp_list.append(elt[0].upper())
    if format_AB:
        if printlog:
            print(elt.upper())
        temp_list.append(elt.upper())
    if format_ab:
        if printlog:
            print(elt.lower())
        temp_list.append(elt.lower())
    if format_BA:
        if printlog:
            print(elt[::-1].upper())
        temp_list.append(elt[::-1].upper())
    if format_L33T_5P34K:
        word = elt.upper()
        word = word.replace("O", "0")
        word = word.replace("I", "1")
        if (leet_j):
            word = word.replace("L", "1")
        word = word.replace("E", "3")
        word = word.replace("A", "4")
        word = word.replace("S", "5")
        word = word.replace("T", "7")
        if printlog:
            print(word)
        temp_list.append(word)
    if format_ba:
        if printlog:
            print(elt[::-1].lower())
        temp_list.append(elt[::-1].lower())
    if format_Ba:
        if (len(elt) > 1):
            if printlog:
                print(elt[-1].upper() + elt[-2::-1].lower())
            temp_list.append(elt[-1].upper() + elt[-2::-1].lower())
        elif elt[0].upper() not in temp_list:
            if printlog:
                print(elt[0].upper())
            temp_list.append(elt[0].upper())
    if elt not in temp_list:
        temp_list.append(elt)

""" Converting string extra char to list """

charList = []
for letter in extra_chars:
    charList.append(letter)

""" Then generating combo-words """

if (printlog):
    print("Generated simple word count: " + str(len(temp_list)))

print("*************************************************************************")
print("")
print("Generating combo word")
print("")

continueParsing = True
i = 0
while (continueParsing):
    i += 1
    print("generating ... (" + str(i) + ")")
    continueParsing = False  # Default False
    for elt in temp_list:
        for secndElt in temp_list:
            newWord = elt + secndElt
            if ((len(wordStart + newWord + wordEnd) <= lMax) and (newWord not in temp_list)):
                if printlog:
                    print(newWord)
                temp_list.append(newWord)
                continueParsing = True  # We have to parse again because of the added word
print("")
print("Generating combo-word endded !")
print("")

""" Then generating combo-words with extra char """

print("*************************************************************************")
print("")
print("Generating combo word WITH EXTRA char...")
print("")

""" Generating chargroup """

continueParsing = True

while (continueParsing):
    continueParsing = False  # Default False
    for elt in charList:
        for secndElt in charList:
            newWord = elt + secndElt
            if ((len(newWord) <= nbExtra_chars) and (newWord not in charList)):
                if printlog:
                    print(newWord)
                charList.append(newWord)
                continueParsing = True  # We have to parse again because of the added char group

""" Adding extra char to existing words """

i = 0
lenTemp = str(len(temp_list))
temp_list_extra = []

for elt in temp_list:
    i += 1
    for chargroup in charList:
        if ((len(wordStart + elt + chargroup + wordEnd) <= lMax) and ((elt + chargroup) not in temp_list)):
            if printlog:
                print(elt + chargroup)
            temp_list_extra.append(elt + chargroup)

temp_list.extend(temp_list_extra)

""" Deleting too shorts words and adding prefix / suffix """

endList = []

for elt in temp_list:
    if (len(wordStart + elt + wordEnd) >= lMin):
        if printlog:
            print(wordStart + elt + wordEnd)
        endList.append(wordStart + elt + wordEnd)

""" print few generated words """

print("*************************************************************************")
print("")
print("Generated list : " + str(len(endList)))
print("")
if (maxDisplay != -1):
    for i in range(maxDisplay):
        if (len(endList) > i):
            print(endList[i])
        else:
            break;
    if (i < len(endList) - 1):
        print("...")
else:
    for elt in endList:
        print(elt)
print("")

""" Writing the list into file """

print("*************************************************************************")
print("")
print("Writing the file...")

file = open(fileToSave, "w+")

for elt in endList:
    file.write(elt + "\r\n")
file.close()
print("")
print("File written: " + fileToSave.replace("\\", "/"))
print("")

""" displaying words count """

print("*************************************************************************")
print("")
print(str(len(endList)) + " words generated !")
print("")