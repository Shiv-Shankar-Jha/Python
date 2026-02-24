wheat = []
rice1 = []


while True:
    input1 = input("How many kg of wheat:" \
    "type rice to switch: ")

    if input1 == "rice":
        input2 = float(input("How much Rice: "))
        rice1.append(input2)

    else:
        try:
            input3 = float(input1)
            wheat.append(input3)
        except ValueError:
            print("Wrong Input")

    

    

    print(f"Total Wheat: {sum(wheat)}")
    print(f"Total Rice: {sum(rice1)}")

