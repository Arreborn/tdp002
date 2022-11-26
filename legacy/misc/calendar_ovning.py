monthsDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months = ["Januari", "Februari", "Mars", "April", "Maj", "Juni", "Juli", "Augusti", "September", "Oktober", "November", "December"]

while True:

    wkday = input("Vilken veckodag är den första januari? ").upper()

    if wkday == "MÅNDAG":
        start = 0
        break
    elif wkday == "TISDAG":
        start = 1
        break
    elif wkday == "ONSDAG":
        start = 2
        break
    elif wkday == "TORSDAG":
        start = 3
        break
    elif wkday == "FREDAG":
        start = 4
        break
    elif wkday == "LÖRDAG":
        start = 5
        break
    elif wkday == "SÖNDAG":
        start = 6
        break
    else:
        print("Felaktig input! försök igen!")

for i in range (0, 12):
    currentDate = 1 - start

    days = monthsDays[i]
    print("")
    print(months[i])
    print("---------------------")
    print("MÅ", end=" ")
    print("TI", end=" ")
    print("ON", end=" ")
    print("TO", end=" ")
    print("FR", end=" ")
    print("LÖ", end=" ")
    print("SÖ")
    print("---------------------")

    for j in range (0, 6):
        counter = 0
        for k in range (0, 7):
            if currentDate <= days:
                if currentDate <= 0:
                    print(end="   ")
                elif currentDate > 0:
                    if k == 6:
                        if currentDate < 10:
                            print("0" + str(currentDate))
                        else:
                            print(currentDate)
                    else:
                        if currentDate < 10:
                            print("0" + str(currentDate), end=" ")
                        else:
                            print(currentDate, end=" ")
                else:
                    print(end="   ")
                currentDate += 1
                counter += 1
                if currentDate == days:
                    start = counter + 1
                    if start > 6:
                        start = 0
    print("")

