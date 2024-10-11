age = int(input("how old are you? "))
student = input("are you a student? ")

if 0 <= age < 12:
    print("£5")

elif 12 <= age < 64 and student == "yes":
    print("£8")

elif 12 <= age < 64 and student == "no":
    print("£10")

else:
    print("please enter a valid age")
