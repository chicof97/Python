weight = float(input("What's your weight? "))

while True:
    measure_unit = input("(K)gs or (L)bs? ").lower()
    if measure_unit == "k" or measure_unit == "l":
        break

if measure_unit == "k":
    # can use round(weight,1) too
    print("Your weight is ", "{:.1f}".format(weight * 2.2046), "lbs")
    # print(f"Your weight is {round(weight * 2.2046,3)} lbs")

elif measure_unit == "l":
    print("Your weight is ", "{:.1f}".format(weight * 0.45359237), "lbs")
