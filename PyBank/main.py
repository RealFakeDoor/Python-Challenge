# Python script that analyses financial records of an excel spreadsheet.
# The Python script will pull the following from the datasheet:

# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The changes in "Profit/Losses" over the entire period, 
# and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period

import csv

# Path to excel spreadsheet.
File_Path = "./Resources/budget_data.csv"

#Initialise Variables:

Date_List = []      # List of all dates included in the dataset.
Profit_Loss = []    # List of all profit Losses in the dataset.
Changes = []        # List of changes in profit/losses between dates in dataset.

# Open and read data from excel spreadsheet.
with open(File_Path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Store the first row (header) as a List.
    # The first row contains headers- Skip in order to just get dates in Date_List.
    Header = next(csv_reader)
      
    # Create a loop that captures all the data in each row as an individual value,
    # Date_List - A list of all the dates in row 'Dates'
    # Profit_Loss - A List of all the profits and losses in the column 'Profit/losses'
    for row in csv_reader:
        Date_List.append(row[0])
        Profit_Loss.append(float(row[1]))

# Since we are asked to find the total months,
# We want to make sure that the list has no repeat values
Date_List_Clean = list(set(Date_List))

#The total number of months included in the dataset.
Total_Months = len(Date_List_Clean)

#The total number of months included in the dataset.
Total_Months = len(Date_List_Clean)

#The net total amount of "Profit/Losses" over the entire period.
Net_PL = sum(Profit_Loss)

#The changes in "Profit/Losses" over the entire period, and then the average of those changes:

# Create a Loop that iterates through the list of profits and losses
# Calculates the vector changes in profits and losses between datapoints,
    # i.e.  negative representing a decrease in profit.
    #       positive representing an increase in profit.
# Adds the changes as a vector(+/-), to a new list 'Changes'. 
    # Note:
    # We cannot calculate the change on the first month as there is no data prior to that month,
    # Therefore the loop must start at the second value within the list.

for i in range(1, len(Profit_Loss)):
    # Calculates the vector changes in profits and losses between datapoints
    change = Profit_Loss[int(i)] - Profit_Loss[int(i-1)]
    # Adds the changes as a vector(+/-), to a new list 'Changes'.
    Changes.append(change)
    
# Calculate the average of those changes.
Changes_Total = sum(Changes)
Average_PL = sum(Changes)/len(Changes)

# Format to reflect required output.
Average_PL = round(Average_PL,2)

# Find the greatest increase in profits (date and amount) over the entire period.
# First find the greatest increase in Profits from List Changes[].
Greatest_Increase_Profits = max(Changes)

# Find The greatest decrease in profits (date and amount) over the entire period.
# First find the greatest decrease in Profits from List Changes[].
Greatest_Decrease_Profits = min(Changes)

# We need to be able to get the corresponding dates to the greatest decrease/increase in profits.
# Create a dictionary with the changes as the key corresponding to the dates as the value.

# The changes list is missing the first date as we cannot calculate a change for that due to no prior data. Remove first value from dates.
Date_List = Date_List[1:]

# Create a dictionary with the Key values set as the changes in profit/loss and their corresponding dates as the value.
result_dict = dict(zip(Changes, Date_List))

# Print results in required format.
print("Financial Analysis")
print(" ")
print("----------------------------------")
print(" ")
print(f'Total Months:  {Total_Months}')
print(f'Total: ${int(Net_PL)}')
print(f'Average Change: ${Average_PL}')
print(f'Greatest Increase in Profits: {result_dict[Greatest_Increase_Profits]} (${int(Greatest_Increase_Profits)})')
print(f'Greatest Decrease in Profits: {result_dict[Greatest_Decrease_Profits]} (${int(Greatest_Decrease_Profits)})')

# Output results in required format to a .txt file.
with open('./Analysis/Financial Analysis.txt', 'w') as file:
    # Redirect print statements to the file
    file.write(f'Financial Analysis\n')
    file.write(" \n")
    file.write("----------------------------------\n")
    file.write(" \n")
    file.write(f'Total Months:  {Total_Months}\n')
    file.write(f'Total: ${int(Net_PL)}\n')
    file.write(f'Average Change: ${Average_PL}\n')
    file.write(f'Greatest Increase in Profits: {result_dict[Greatest_Increase_Profits]} (${int(Greatest_Increase_Profits)})\n')
    file.write(f'Greatest Decrease in Profits: {result_dict[Greatest_Decrease_Profits]} (${int(Greatest_Decrease_Profits)})\n')