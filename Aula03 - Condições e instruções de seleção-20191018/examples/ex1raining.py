# Example: using a boolean variable (a flag)

isRaining = input("Is it raining? ") == "yes"
print(isRaining)

if isRaining :
    whatToDo = "take an umbrella"
    print("hi!")
else:
    whatToDo = "enjoy!"
    print("bye!")

print(whatToDo)

