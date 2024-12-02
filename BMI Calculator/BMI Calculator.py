import random

def get_health_tip(category):
    """
    Provide a health tip based on the BMI category.
    """
    tips = {
        "Underweight": [
            "Include more calories in your diet with healthy foods like nuts, avocados, and whole grains.",
            "Focus on strength training to build muscle mass.",
            "Consider consulting a nutritionist for a personalized diet plan."
        ],
        "Normal weight": [
            "Maintain a balanced diet and regular exercise to stay fit.",
            "Drink plenty of water to keep yourself hydrated.",
            "Incorporate stress management techniques like meditation or yoga."
        ],
        "Overweight": [
            "Incorporate more vegetables and lean protein into your meals.",
            "Try at least 30 minutes of physical activity daily, such as walking or jogging.",
            "Avoid sugary drinks and focus on drinking water or herbal teas."
        ],
        "Obesity": [
            "Seek guidance from a healthcare provider for a structured weight loss plan.",
            "Start with low-impact exercises like swimming or cycling.",
            "Focus on small, achievable changes in your diet and lifestyle."
        ]
    }
    return random.choice(tips[category])

def get_motivational_quote():
    """
    Provide a random motivational quote.
    """
    quotes = [
        "Take care of your body. It's the only place you have to live. – Jim Rohn",
        "Your health is an investment, not an expense.",
        "Fitness is not about being better than someone else. It’s about being better than you used to be.",
        "Small steps every day lead to big changes over time.",
        "Your journey to health begins with a single step."
    ]
    return random.choice(quotes)

def calculate_bmi():
    """
    Function to calculate BMI and provide health tips and motivation.
    """
    while True:
        print("\n--- Personalized BMI Calculator ---")
        print("Enter your details to calculate your BMI and get health tips.")
        print("Type 'exit' anytime to quit.\n")

        try:
            # Get user input for weight and height
            weight_input = input("Enter your weight in kilograms (e.g., 70): ").strip()
            if weight_input.lower() == 'exit':
                break
            weight = float(weight_input)

            height_input = input("Enter your height in meters (e.g., 1.75): ").strip()
            if height_input.lower() == 'exit':
                break
            height = float(height_input)

            # Calculate BMI
            bmi = weight / (height ** 2)

            # Determine BMI category
            if bmi < 18.5:
                category = "Underweight"
            elif 18.5 <= bmi < 24.9:
                category = "Normal weight"
            elif 25 <= bmi < 29.9:
                category = "Overweight"
            else:
                category = "Obesity"

            # Display results
            print(f"\nYour BMI is: {bmi:.2f}")
            print(f"You are classified as: {category}")

            # Provide health tip and motivation
            print("\nHealth Tip:")
            print(get_health_tip(category))

            print("\nMotivational Quote:")
            print(get_motivational_quote())

        except ValueError:
            print("\nInvalid input! Please enter numerical values for weight and height.\n")
        except ZeroDivisionError:
            print("\nHeight cannot be zero. Please enter a valid height.\n")

        # Ask if the user wants to calculate again
        print("\nDo you want to calculate again?")
        choice = input("Type 'yes' to continue or 'no' to exit: ").strip().lower()
        if choice == 'no':
            print("\nThank you for using the BMI Calculator. Stay healthy!")
            break


# Run the BMI calculator
if __name__ == "__main__":
    calculate_bmi()
