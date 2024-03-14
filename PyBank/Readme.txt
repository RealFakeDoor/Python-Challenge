PYBANK README:

Python script that analyses financial records of an excel spreadsheet.
The financial dataset called budget_data.csv and will be located in the folder 
resources in the same directory as this script.

The dataset is composed of two columns: "Date" and "Profit/Losses".

Date		-The month and year corresponding to the recroded profit/loss.
Profit/Losses 	- The profit or loss of the month leading up to the corresponding date.


The Python script will pull the following from the datasheet:

The total number of months included in the dataset.
The net total amount of "Profit/Losses" over the entire period.
The changes in "Profit/Losses" over the entire period, and then the average of those changes.
The greatest increase in profits (date and amount) over the entire period.
The greatest decrease in profits (date and amount) over the entire period.

The Script will then output a text file into the Analysis folder in the same directory as the script, aswell as print the result to the terminal.

LOGIC:

Create a list to capture each dataset we need for out calculations and results from those calculations.

Date List, Profit/Losses List, Change in profit loss List.

Loop through the spreadsheet to populate the Date List and Profit/Loss List.
The index will correspond to the correct profit/loss and date for the two lists.

Populate the changes list:

Create a Loop that iterates through the list of profits and losses.
Calculates the changes in profits and losses between months,
     i.e.  	negative value representing a decrease in profit.
          	positive representing an increase in profit.

Change vector- Postive = Profit, Negative = loss.

Change Vector = Profit_Loss(This Month) - Profit_Loss(Last Month)

Add each vector to the changes list.

Note:
    We cannot calculate the change on the first month as there is no data prior to that month, Therefore the loop must start at the second value within the list.

"Profit/Losses" over the entire period and then the average of those changes:
Then we sum all the changes, and divide it by the how many datapoints in the changes list, i.e. length of changes list.

The greatest increase and decrease in profits, is found using the max and min function on the changes list.



