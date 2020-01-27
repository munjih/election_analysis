# Retrieve data
# 1. Total number of votes cast
# 2. Complet list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import os

# Assign a variable for the file to load
file_to_load = os.path.join("resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize variable for total votes
total_votes = 0

# Candidate list
candidate_options = []

# Candidate votes dictionary
candidate_votes = {}

# Define variables for winner, winning count and winning percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the file
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(file_reader)
    
    # For each row in the CSV file
    for row in file_reader:
        # Count total votes
        total_votes += 1

        # Candidate name from each row 
        candidate_name = row[2]

        # Check if candidate name does not match existing candidates
        if candidate_name not in candidate_options:
            # Add candidate name to list
            candidate_options.append(candidate_name)

            # Initialize new candidate vote count
            candidate_votes[candidate_name] = 0
        
        # Increment candidate vote count
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Write total votes for the election
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine percentage of votes for each candidate
    # Iterate through the candidate list
    for candidate in candidate_votes:
        # Retrieve vote for each candidate
        votes = candidate_votes[candidate]
        
        # Calculate vote percentage 
        vote_percentage = int(votes) / int(total_votes) * 100
        
        # Print candidates vote count and percentage to txt file
        candidate_results = f"{candidate}: {vote_percentage:.1f}% ({votes})\n"       
        print(candidate_results)
        txt_file.write(candidate_results)

        # Check if candidates vote is greater than winning count
        if(votes > winning_count):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate

    # Print candidate, vote percentage (one decimal) and votes      
    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Wiining Vote Count: {winning_count}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n")
    
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
    
        
