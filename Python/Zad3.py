from tkinter import Variable

slowo_podane = input("Podaj słowo które chcesz wypisać od końca: ")
length = len(slowo_podane)
for x in range(0, length):
    length -= 1
    print(slowo_podane[length], end="") # end="" to coś dzięki czemu te litery wypisują się jedne po drugiej