day_of_week = input("what day of the week is it? ")

if day_of_week == "monday" or day_of_week == "tuesday" or day_of_week == "wednesday" or day_of_week == "thursday" or day_of_week == "friday":
    print("It is a weekday")

elif day_of_week == "saturday" or day_of_week == "sunday":
    print("It is the weekend")

else:
    print("not valid day")
