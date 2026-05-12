
#!/usr/bin/env python3
"""
BMI and Heart Rate Zones Calculator

This script calculates:
- Body Mass Index (BMI) from weight (kg) and height (m)
- Heart rate zones based on age, using max HR = 220 - age
"""

def calculate_bmi(weight_kg, height_m):
    """Calculate BMI and return the value and category."""
    bmi = weight_kg / (height_m ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    return bmi, category

def calculate_heart_rate_zones(age):
    """Calculate heart rate zones based on age."""
    max_hr = 220 - age
    
    # General intensity zones (percentage of max HR)
    moderate_low = int(max_hr * 0.50)
    moderate_high = int(max_hr * 0.70)
    vigorous_low = int(max_hr * 0.70)
    vigorous_high = int(max_hr * 0.85)
    
    # Detailed training zones (Zone 1 to 5)
    zone1 = (int(max_hr * 0.50), int(max_hr * 0.60))  # Very light
    zone2 = (int(max_hr * 0.60), int(max_hr * 0.70))  # Light
    zone3 = (int(max_hr * 0.70), int(max_hr * 0.80))  # Moderate
    zone4 = (int(max_hr * 0.80), int(max_hr * 0.90))  # Hard
    zone5 = (int(max_hr * 0.90), int(max_hr))          # Maximum
    
    return max_hr, (moderate_low, moderate_high), (vigorous_low, vigorous_high), \
           (zone1, zone2, zone3, zone4, zone5)

def get_positive_float(prompt):
    """Get a positive float from user input with validation."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    print("=" * 50)
    print("BMI & HEART RATE ZONES CALCULATOR")
    print("=" * 50)
    
    # Input
    print("\n--- BMI Calculation ---")
    weight = get_positive_float("Enter your weight (kg): ")
    height = get_positive_float("Enter your height (m): ")
    
    print("\n--- Heart Rate Zones ---")
    age = int(get_positive_float("Enter your age (years): "))
    
    # Calculate BMI
    bmi, category = calculate_bmi(weight, height)
    
    # Calculate heart rate zones
    max_hr, moderate_zone, vigorous_zone, zones = calculate_heart_rate_zones(age)
    zone1, zone2, zone3, zone4, zone5 = zones
    
    # Display results
    print("\n" + "=" * 50)
    print("RESULTS")
    print("=" * 50)
    
    print(f"\nBMI: {bmi:.2f} ({category})")
    
    print(f"\nMaximum Heart Rate (based on age): {max_hr} bpm")
    
    print("\n--- General Heart Rate Zones ---")
    print(f"Moderate intensity (50-70% of max): {moderate_zone[0]} - {moderate_zone[1]} bpm")
    print(f"Vigorous intensity (70-85% of max): {vigorous_zone[0]} - {vigorous_zone[1]} bpm")
    
    print("\n--- Detailed Training Zones (5 Zones) ---")
    print(f"Zone 1 (Very light, 50-60%):     {zone1[0]} - {zone1[1]} bpm")
    print(f"Zone 2 (Light, 60-70%):          {zone2[0]} - {zone2[1]} bpm")
    print(f"Zone 3 (Moderate, 70-80%):       {zone3[0]} - {zone3[1]} bpm")
    print(f"Zone 4 (Hard, 80-90%):           {zone4[0]} - {zone4[1]} bpm")
    print(f"Zone 5 (Maximum, 90-100%):       {zone5[0]} - {zone5[1]} bpm")
    
    print("\nNote: These are estimates. For medical advice, consult a professional.")

if __name__ == "__main__":
    main()