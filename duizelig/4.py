Day = input("Typ een dag van de week: ")
a = 2
while a < 3:
    if Day == "Maandag":
        print("Maandag")
        break
    elif Day == "Dinsdag":
        print("Maandag", "Dinsdag")
        break
    elif Day == "Woensdag":
        print("Maandag", "Dinsdag", "Woensdag")
        break
    elif Day == "Donderdag":
        print("Maandag", "Dinsdag", "Woensdag", "Donderdag")
        break
    elif Day == "Vrijdag":
        print("Maandag", "Dinsdag", "Woensdag", "Donderdag", "Vrijdag")
        break
    elif Day ==  "Zaterdag":
        print("Maandag", "Dinsdag", "Woensdag", "Donderdaf", "Vrijdag", "Zaterdag")
        break
    elif Day == "Zondag":
        print("Maandag", "Dinsdag", "Woensdag", "Donderdag", "Vrijdag", "Zaterdag", "Zondag")
        break
    else:
        print("Syntax Error | Zorg ervoor dat de dag met een hoofdletter begint.")
        break
      