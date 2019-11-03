#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Menu choices in a loop and call to functions
"""
import menu
import analyzer
filename = "phil.txt"

while True:
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print("Choose your battle: ")

    menu.menu()
    choice = input("=> ")

    if choice == "q":
        print("Well, bye then!")
        break



    elif choice == "lines":
        print(analyzer.line_counter())

    elif choice == "words":
        print(analyzer.word_counter())

    elif choice == "letters":
        print(analyzer.letter_counter())

    elif choice == "word_frequency":
        print(analyzer.word_frequency())

    elif choice == "letter_frequency":
        print(analyzer.letter_frequency())

    elif choice == "all":
        analyzer.analyze_all()



    else:
        print("Not a valid choice. Choose from the menu.")

    input("\nPress enter to continue...")
