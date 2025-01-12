"""
Name: Dan Zhu
Date: 11/10/2024
Assignment: Module 3.2
Description: Write a program that uses a while loop to determine how long it takes for an investment to double at a given interest rate. The input will be an annualized interest rate and the initial investment amount, and the output is the number of years it takes an investment to double.
"""
# function calculate how many years to double investment
def calculate_investment_years(principal, apr):
    # initial total and and years of investment
    total = principal
    years = 0

    # while loop to get years when investment is doubled
    while total <= 2 * principal:
        total += total * (apr/100)
        years += 1

    # years take to double investment
    return years, total
     
def main():
    # Get principal and apr
    principal = float(input("Please enter the amount you want to invest: "))
    apr = int(input("Please enter the interest rate (as a whole number): "))

    # Years to bouble investment
    years, total = calculate_investment_years(principal, apr)

    # Display results
    print(f"Princial: ${principal: .2f}")
    print(f"APR: {apr}%")
    print(f"It will take {years} years to double your investment. Your final amount will be ${total: .2f}")

# Call the main function
if __name__ == "__main__":
    main()


