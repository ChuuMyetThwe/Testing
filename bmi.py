def bmi_calculator(weight,height):
    print("weight =" + str(weight))
    print("height =" + str(height))
    bmi = weight / (height * height)
    print(bmi)

    if (bmi < 18.5):
        return -1
    elif (bmi >= 18.5 and bmi <= 25.0):
        return 0
    else:
        return 1

bmi_calculator(57, 1.73)
