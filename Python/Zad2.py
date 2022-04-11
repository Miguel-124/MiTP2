data = input("Podaj date (np. 31.02): ")
day = data[0:2]
month = data[3:5]

while (  # WIOSNA
    32 > int(day) >= 20
    and int(month) == 3
    or 0 < int(day) < 20
    and int(month) == 6
    or 3 < int(month) < 6
    and 0 < int(day) < 32
):
    print("Aktualna pogoda to wiosna")
    break

while (  # LATO
    32 > int(day) > 20
    and int(month) == 6
    or 0 < int(day) < 24
    and int(month) == 9
    or 6 < int(month) < 9
    and 0 < int(day) < 32
):
    print("Aktualna pogoda to lato")
    break

while (  # JESIEN
    32 > int(day) > 22
    and int(month) == 9
    or 0 < int(day) < 22
    and int(month) == 12
    or 9 < int(month) < 12
    and 0 < int(day) < 32
):
    print("Aktualna pogoda to jesień")
    break

while (  # ZIMA
    32 > int(day) > 21
    and int(month) == 12
    or 0 < int(day) < 20
    and int(month) == 3
    or 1 < int(month) < 2
    and 0 < int(day) < 32
):
    print("Aktualna pogoda to zima")
    break
