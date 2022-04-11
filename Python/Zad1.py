from tkinter import Variable


print("Program przelicza Celsjusze na Fahrenheita lub odwrotnie")
stopnie = input("Podaj stopnie (np. 20C lub 20F): ")
if stopnie.endswith("F"):
    stopnie_liczba = stopnie[0 : len(stopnie) - 1] #Tworzymy nowy string, który będzie miał usuniętą jedną litere z prawej strony
    Celsjusza = (int(stopnie_liczba) - 32) * 5 / 9 # Wymuszamy intigera na stringu który już posiada same liczby
    Fahrenheity = int(stopnie_liczba)
    print(str(Celsjusza) + "C")
elif stopnie.endswith("C"):
    stopnie_liczba = stopnie[0 : len(stopnie) - 1]
    Fahrenheity = int(stopnie_liczba) * 9 / 5 + 32
    Celsjusza = int(stopnie_liczba)
    print(str(Fahrenheity) + "F")
else:
    print("Podałeś błędną instrukcje")
