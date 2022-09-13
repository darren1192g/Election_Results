# The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

# Add our dependencies.
import csv
import os 

#Assign a variable to load a file from a path.
file_to_load = os.path.join("resources","election_results.csv")
#Assign a variable to save the file to path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
winning_count = 0
winning_percentage = 0

# candidate options 
Candidate_options = []
# Dictionary of candidates
Candidate_votes = {}
#Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    #print(headers)
    #Print each row in the CVS file.
    for row in file_reader:
        # add to the total vote count.
        total_votes += 1
        # Print the candidate name from each row
        Candidate_name = row [2]
        #If the candidate does not match any existing canidate...
        if Candidate_name not in Candidate_options:
            # Add candidate name to the candidate list
            Candidate_options.append(Candidate_name)
            # Tracking candidate's vote count.
            Candidate_votes[Candidate_name] = 0
        # Add a vote to that canidate"d count
        Candidate_votes[Candidate_name] +=1
        # Determin the percentage of votes for each candiate by looping through the counts
        # iterate through the cadidate list
        for Candidate_name in Candidate_votes:
            # Retrive vote count of candidate.
            votes = Candidate_votes[Candidate_name]
            # Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100
            # print the canidate name and percentage of votes
            print(f"{Candidate_name}: received {vote_percentage}% of the vote.")
            # Determine winning vote count and candidate
            # Determine if the votes are greater than the winning count
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # if true then set winning_count = votes and winning_percent = vote_percentage
                winning_count = votes
                winning_percentage = vote_percentage
                # set the winning_candidate equal to the candidate"s name
                winning_candidate = Candidate_name
#print out each canidate"s name, vote count and percentage of votes to the terminal
#print(f"{Candidate_name}: {vote_percentage: 1f}% ({votes:,})\n")      
        winning_candidate_summary =(
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)          


