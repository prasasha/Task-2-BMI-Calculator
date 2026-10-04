print("=== BMI Calculator ===")

while True:
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("Error: Weight and height must be greater than 0.")
            continue

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}")

        again = input("\nDo you want to calculate again? (y/n): ").lower()

        if again != "y":
            print("Thank you for using BMI Calculator!")
            break

    except ValueError:
        print("Error: Please enter numbers only.")