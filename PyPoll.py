#from typing import cast

#Add our depencies.
import csv
import os
#Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#1. Initialize a total vote counter
total_votes = 0
# Candidate options and candidate votes
candidate_options = []

#Declare the empty dictionary
candidate_votes = {}

#Winning Candidate and Winning Count Trakcer
winning_candidate = ""
winning_count = 0
winning_percentage = 0


#open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read and print the header row.
    headers = next(file_reader)
    #print(headers)

 #Print each row in teh CSV file.
    for row in file_reader:
         total_votes += 1

         #Print the candidate name from each row.
         candidate_name = row [2]

         #If the candidate does not match any existin candidate....
         if candidate_name not in candidate_options:
             #add it to the list of canidates
             candidate_options.append(candidate_name)

             #beging tracking that candidate's vote count.
             candidate_votes[candidate_name] = 0

            #Add a vot to that candidate's count.
         candidate_votes[candidate_name] += 1

#Determine the percentage of votes for each candidate by looping through the counts.
#1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    #2. Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    #3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    #4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage: .2f}% of the vote.")

#Determine the percentage of votes for each candidate by looping through the counts
#Iterate through the candidate list.
for candidate_name in candidate_votes:
    #retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    #calculate the percentages of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    #To do: print out each candidates name, vote count, and percentage of votes to the terminal
    print(f"{candidate_name}: {vote_percentage: .1f}%({votes:,})\n")

    #Determine winning vote count and candidate
    #Determine if the votes is greater than the winning count.
    if (votes> winning_count) and (vote_percentage > winning_percentage):
        #If true then set winning_count = votes and winning_percentage= vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        #And, set teh winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

# winning candidate summary
winning_candidate_summary = (
    f"------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage: .1f}%\n"
    f"------------------------\n")
print(winning_candidate_summary)


    # To do: print out the winning candidate, vote count and percentage to terminal.

#Print the candidate vote dictionary.
#print(candidate_votes)









