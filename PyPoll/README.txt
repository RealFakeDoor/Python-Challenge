PYPOLL README

Python script that analyzes the votes recorded on an excel spreadsheet.
The spreadsheet is composed of three columns: "Voter ID", "County", and "Candidate".

Candidates names repeat numerous times, i.e. once for each vote.


 
Script calculates each of the following values:
# The total number of votes cast.
# A complete list of candidates who received votes
# The percentage of votes each candidate won.
# The total number of votes each candidate won.
# The winner of the election based on popular vote.

LOGIC:

Loop through dataset to:
Populate a list of names each name representing one vote for each candidate.
Count the total number of votes for the election.

Create a candidate list with each candidate name appearing only once.
create a votes list, with index correspeonding to the candidates list and populated with zero values for each candidate.

Create a nested loop with an IF statement, that counts how many votes each candidate recieved then counts those votes within the votes list.

Loops through spreadsheet rows, whilst on each row,
loops through the candidates list and checks which name in the candidates list equals the name on that row of the spreadsheet.

Adds a vote to the corresponding position of that candidate in the votes list.

Assuming no two candidates received the same number of votes, find the value of the maximum votes stored as Winner_Votes.

# To find the name of the winner, create a dictionary,
# Keys     - Number of votes.
# Values   - Name of candidate.

Use Winner_Votes with the dictionary to find the winner.

Percentage votes list, loop through votes list and calculate percentage of total votes for each candidate using a simple calculation:

Percentage of total votes = 100 x Votes_List(Candidate)/Total Votes.


