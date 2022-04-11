for x in range(2, 40):
    z = 0
    for y in range(2, 9):
        if x < y:
            break
        elif x % y == 0:
            z += 1
            if z < 2:
                if x == y:
                    print(x)
                else:
                    continue
            else:
                break
        else:
            continue

# Jeszcze nie zrobione
