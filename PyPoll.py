# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The total number of votes each candidate received
# 4. The percentage of votes each candidate won
# 4. The winner of the election based on popular vote.

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Inititalize a total vote counter
total_votes = 0
# initialize list of unique candidates
candidate_options = []
# initialize dictionary of votes per candidate
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes = total_votes + 1
        # access the name of candidate at each row
        candidate_name = row[2]
        # create the list of unique candidates
        if candidate_name not in candidate_options:
            # add to list only if candidate name does not match any existing candidate
            candidate_options.append(candidate_name)
        # begin tracking that candidates' vote count.
            candidate_votes[candidate_name] = 0
        # add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = ( f"\nElection Results\n" f"-------------------------\n" f"Total Votes: {total_votes:,}\n" f"-------------------------\n")
    print(election_results, end="")
    # After printing the final vote count to the terminal save the final vote count to the text file
    txt_file.write(election_results)
#Determine the percentage of votes for each candidate by looping through the counts
# 1. Iterate through the candidate list
    for candidate_name in candidate_votes:
        #2. Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #3. Calculate the percentage of votes
        vote_percentage = float(votes)/float(total_votes)*100
        #To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
    #    print(f"{candidate_name}: {vote_percentage:.1f}%  ({votes:,})\n")
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #Print each candidate's voter count and percentage to the terminal
        print(candidate_results)
        # Save the candidate results to our txt file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #If true then set winning_count = votes and winning_percentage= vote_percentage
            winning_count = votes
            #And, set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
            
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)

