print("Enter a date")
n=input().lower()
match n:
    case "monday":
        print("today is Monday")
    case "tuesday":
        print("today is tuesday")
    case "wednesday":
        print("today is wednesday")
    case "thursday":
        print("today is thursday")    
    case "friday":
        print("today is friday")
    case "saturday":
        print("today is saturday")
    case "sunday":
        print("today is sunday there is no work")
    case _:
        print("invalid date")
    

     