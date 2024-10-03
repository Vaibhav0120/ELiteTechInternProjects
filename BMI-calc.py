def calculate_bmi():
    print("Welcome to the BMI Calculator!")

    try:
        weight = float(input("Enter your weight in kilograms (kg): "))
        height = float(input("Enter your height in meters (m): "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers. Please try again.")
            return

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            classification = "Underweight"
        elif 18.5 <= bmi < 24.9:
            classification = "Normal weight"
        elif 25 <= bmi < 29.9:
            classification = "Overweight"
        else:
            classification = "Obese"


        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"This is classified as: {classification}")

    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")

calculate_bmi()
