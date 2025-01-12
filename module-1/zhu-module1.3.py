"""
Name: Dan Zhu
Date: 1/12/2025
Assignment: Module 1.3
Description: 
Ask the user how many bottles of beer are on the wall.
Pass that input to a function that manages the countdown.
The function should take the input and count backwards to 1 while displaying the number of remaining bottles of beer on the wall.
Once the count is down to 1, change lyrics to show "1 bottle of beer..."
At the end of the countdown, get back to the main program and remind the user to buy more beer.
"""
def countDownBottles(numberOfBottles):
    while numberOfBottles > 0:
        if numberOfBottles > 1:
            print(f"{numberOfBottles} bottles of beer on the wall, {numberOfBottles} bottles of beer.")
            print(f"Take one down and pass it around, {numberOfBottles - 1} bottle(s) of beer on the wall.")
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print(f"Take one down and pass it around, no more bottles of beer on the wall.")
        numberOfBottles -= 1
    print(f"Time to buy more bottles of beer.")

def main(): 
    # get how many bottles on the wall
    numberOfBottles = int(input("Enter bottles on the wall: "))
    countDownBottles(numberOfBottles)
   
# Call the main function
if __name__ == "__main__":
    main()


