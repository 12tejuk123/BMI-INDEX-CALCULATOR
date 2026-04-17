def calculate_bmi(weight, height, unit='metric'):
    """
    Calculate BMI based on weight and height.

    Parameters:
        weight (float): The weight of the person.
        height (float): The height of the person.
        unit (str): The unit of measurement ('metric' or 'imperial').

    Returns:
        float: The calculated BMI.
    """
    if unit == 'imperial':
        # Convert height from inches to meters and weight from pounds to kilograms
        height = height * 0.0254
        weight = weight * 0.453592
    return weight / (height ** 2)

def input_validation(value):
    """
    Validate if the input value is a positive number.

    Parameters:
        value (str): The input value as a string.

    Returns:
        float: The validated float value.
    Raises:
        ValueError: If the input is not a positive number.
    """
    try:
        value = float(value)
        if value <= 0:
            raise ValueError("Value must be positive.")
        return value
    except ValueError:
        print("Invalid input. Please enter a positive number.")
        return None

def classify_bmi(bmi):
    """
    Classify BMI into categories.

    Parameters:
        bmi (float): The calculated BMI.

    Returns:
        str: The BMI category.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def health_recommendations(bmi):
    """
    Provide health recommendations based on BMI.

    Parameters:
        bmi (float): The calculated BMI.

    Returns:
        str: Health recommendations.
    """
    if bmi < 18.5:
        return "Consider a balanced diet to gain weight gradually."
    elif 18.5 <= bmi < 24.9:
        return "Maintain your weight through a healthy diet and exercise."
    elif 25 <= bmi < 29.9:
        return "Consider a balanced diet and increased physical activity to lose weight."
    else:
        return "Consult with a healthcare provider for weight management options."

def unit_conversion(weight, height, unit):
    """
    Convert units if necessary.

    Parameters:
        weight (float): Weight of the person.
        height (float): Height of the person.
        unit (str): Current unit of measurement.

    Returns:
        (float, float): Converted weight and height.
    """
    if unit == 'imperial':
        weight = weight * 0.453592 # To kg
        height = height * 0.0254 # To m
    return weight, height

# Example usage
if __name__ == '__main__':
    weight = input("Enter your weight: ")
    height = input("Enter your height: ")
    unit = input("Enter unit (metric/imperial): ").strip().lower()
    weight = input_validation(weight)
    height = input_validation(height)
    if weight and height:
        weight, height = unit_conversion(weight, height, unit)
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        recommendation = health_recommendations(bmi)
        print(f"Your BMI is: {bmi:.2f}")
        print(f"BMI Category: {category}")
        print(f"Health Recommendation: {recommendation}")