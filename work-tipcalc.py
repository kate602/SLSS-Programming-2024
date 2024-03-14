# Tip Calc
# Kate Jiang
# 2/29/2024

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent

    # Note: This is one way to round a number to two decimal places
    print(f"Leave ${round(tip, 2)}")

def dollars_to_float(d):
    # Converts string dollars to a decimal float
    # Returns the result
    # TODO
    d = float(d)
    return d
    

def percent_to_float(p):
    # Converts percent to a decimal float
    # Returns the result
    # TODO
    p = float(p)
    return p/100

main()