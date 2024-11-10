# Traffic Light Simulator
light=input("Enter the colour of your traffic light: ")
light=light.lower()
if light=="green":
    print("You can go.")
elif light=="orange":
    print("Be ready to go.")
elif light=="red":
    print("You can not go.")
else:
    print("Error")