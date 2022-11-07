rain = input("Whether it's raining? Y\\n: ")
bus = input("Is there a bus? Y\\n: ")

if (rain == "Y" or rain == "y") and (bus == "Y" or bus == "y"):
    print("Take an umbrella, you'll be admitted to college")
elif (rain == "Y" or rain == "y") and (bus == "N" or bus == "n"):
    print("You're not getting into college")
elif (rain == "N" or rain == "n") and (bus == "Y" or bus == "y"):
    print("You will get to universities, have a nice day and beautiful weather")
else:
    print("Error")
