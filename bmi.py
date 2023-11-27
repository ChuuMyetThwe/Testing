def bmi_calculator(weight,height):
    print("weight =" + str(weight))
    print("height =" + str(height))
    bmi = weight / (height * height)
    print(bmi)

    if (bmi < 18.5):
        print("Underweight")
    elif (bmi >= 18.5 and bmi <= 25.0):
        print("Normal weight")
    else:
        print("Over weight")

bmi_calculator(57, 1.73)
