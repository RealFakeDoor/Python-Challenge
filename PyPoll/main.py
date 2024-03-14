import csv

# Path to excel spreadsheet.
File_Path = "./Resources/election_data.csv"

# Python script that analyzes the votes recorded on an excel spreadsheet, 
# and calculates each of the following values:

# The total number of votes cast.

# A complete list of candidates who received votes

# The percentage of votes each candidate won.

# The total number of votes each candidate won.

# The winner of the election based on popular vote.


# Create a list of all Votes via candidates names.
VOTES_Candidates = []

# Tally the total votes of the election.
Total_Votes = 0

# Open and read data from excel spreadsheet.
with open(File_Path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Store the first row (header) as a List.
    # The first row contains headers- Skip in order to just get dates in Date_List.
    Header = next(csv_reader)
    
    # Create a loop that captures all the names of the candidates who recieved votes,
    # and counts the total number of votes in the election.
    for row in csv_reader:
        #Add every candidate name to a the Candidate List.
        VOTES_Candidates.append(row[2])
        
        # Count how many votes have been cast in the election.
        Total_Votes += 1

# As there is many votes for a singular candidate, 
# we want to delete any repeat values stored in the candidates list,
# to ensure our candidates list equals the actual candidates in the list.

# Create a candidate list
Candidates_List = []

# Adds unique values of candidate vote names into candidate list,
# Doesn't allow repeat values in list.
[Candidates_List.append(candidate) for candidate in VOTES_Candidates if candidate not in Candidates_List] 

# Now we must create another list to store the number of votes each Candidate received starting with zero.
# The length of list list must be equal to the length of the candidate list.
Votes = [0 for _ in range(len(Candidates_List))]

# Open and read data from excel spreadsheet.
with open(File_Path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Create a loop that counts how many votes each candidate recieved:
    
    # Loops through spreadsheet rows,
        # for each row loops through the candidates list and checks if the name
        # in the spreadsheet equals the name on the candidate list.
        # If so, Adds a vote to the corresponding position in the votes list.
    
    #Loop through spreadsheet rows,
    for row in csv_reader:
        #loop through candidates list in each during each row.
        for i in range(len(Candidates_List)):
            # checks name in spreadsheet equals name in the candidate list.
            if Candidates_List[i] == row[2]:
                #Add 1 vote to the corresponding vote index for the matching candidate.
                Votes[i] += 1


# Assuming no two candidates received the same number of votes,
# We must find the value of the maximum votes stored as Winner_Votes.
Winner_Votes = max(Votes)

# To find the name of the winner, create a dictionary,
# Keys     - Number of votes.
# Values   - Name of candidate.
Votes_dict = dict(zip(Votes,Candidates_List))

# Calculate the percentage votes for the output, 
# append to a list correpsonding to index of candidates list.
Percentage_Votes = []

#Loop through candidates list,
for i in range(len(Candidates_List)):
    # index votes list, calculate percentage of total votes using Total_Votes.
    Percentage_Votes.append(Votes[i]*100/Total_Votes)

# Print output in given format.
print(f'Election Results')
print(" ")
print(f'-------------------------')
print(" ")
print(f'Total Votes: {Total_Votes}')
print(" ")
print(f'-------------------------')
print(" ")
for i in range(len(Candidates_List)):
    print(f'{Candidates_List[i]}: {round(Percentage_Votes[i],3)}% ({Votes[i]})')
    print(" ")
print(" ")
print(f'-------------------------')
print(" ")
print(f'Winner: {Votes_dict[Winner_Votes]}')
print(" ")
print(f'-------------------------')
print(" ")

# Output results in required format to a .txt file.
with open('./Analysis/Election Results.txt', 'w') as file:
    # Redirect file.write statements to the file.
    file.write(f'Election Results\n')
    file.write(" \n")
    file.write(f'------------------------\n')
    file.write(" \n")
    file.write(f'Total Votes: {Total_Votes}\n')
    file.write(" \n")
    file.write(f'------------------------\n')
    file.write(" \n")
    for i in range(len(Candidates_List)):
        file.write(f'{Candidates_List[i]}: {round(Percentage_Votes[i],3)}% ({Votes[i]})\n')
        file.write(" \n")
    file.write(f'------------------------\n')
    file.write(" \n")
    file.write(f'Winner: {Votes_dict[Winner_Votes]}\n')
    file.write(" \n")
    file.write(f'------------------------\n')
    file.write(" \n")