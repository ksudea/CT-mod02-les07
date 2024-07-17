# Task 1

temperature = input("Enter temperature in Fahrenheit: ")

# Task 2 and 3

def temperature_conversion(temperature_input):
    try:
        if temperature_input.find(".") == -1: #cast the input appropriately: int or float
            temp_f = int(temperature_input)
        else:
            temp_f = float(temperature_input)
        temp_c = (temp_f - 32) * (5/9)
        temp_c = round(temp_c, 2)
    except ValueError:
        print("Please enter a valid integer or float.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print(f"{temp_f} degrees Fahrenheit is {temp_c} degrees Celsius.")
    finally:
        print("Thank you for using our weather forecast application!")

temperature_conversion(temperature)