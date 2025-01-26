import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

def plot_data(dates, temperatures, color, ylabel): 
    # Plot the high temperatures.
    #plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, temperatures, c=color)

    # Format plot.
    plt.title("Daily " + ylabel + " Temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

def main():
    fileName = "sitka_weather_2018_simple.csv"

    with open(fileName) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        dates, highs, lows = [], [], []

        for row in reader:
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
            dates.append(current_date)
            high = int(row[5])
            highs.append(high)
            low = int(row[6])
            lows.append(low)

    while True:
        print(f"Menu: Highs, Lows, or Exit")
        userInput = input("Please enter the options from menu: ")

        if userInput.lower() == "Highs".lower():
            plot_data(dates, highs, "red", "High")
        elif userInput.lower() == "Lows".lower():
            plot_data(dates, lows, "blue", "Low")
        elif userInput.lower() == "Exit".lower():
            print("Exit the program!")
            sys.exit()
        else:
            print("Invalid input, please type Higns, Lows, or Exit!")

main()