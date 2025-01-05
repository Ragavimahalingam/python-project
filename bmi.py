#BMI COnverter
#height =float
#weight =float
#height=height/100
#BMI=weight/(height*height)
#print("BMI:",BMI)
#BMI<=16 - severely underweight
#BMI<=18.5 - underweight
#BMI <=25 - Normal
#BMI<=30 obessed
#else - severly overweight

height=float(input("Enter your height:"))
weight=float(input("Enter your weight:"))
height=height/100
bmi=weight/height**2
print("Your BMI value is",bmi)
if bmi<=16:
    print("You are severely underweight.")
elif bmi<=18.5:
    print("You are underweight.")
elif bmi<=25:
    print("You are normal.")
elif bmi<=30:
    print("You are obese.")
else:
    print("You are severely overweight.")