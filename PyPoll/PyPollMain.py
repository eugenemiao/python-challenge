import os
import csv

pypoll_path = os.path.join(".", "raw_data", "election_data_1.csv")
file_to_output = os.path.join("txt_file.txt")

total_votes = 0

candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0

with open(pypoll_path) as csvfile:
    reader = csv.DictReader(csvfile)
    print(reader)
    reader_list = list(reader)
    total_votes = len(reader_list)

    #print("Election Results")
    #print("-------------------------")

    #print("Total Votes: " + str(total_votes))
    #print("-------------------------")

    #identify unique candidates
    for row in reader:
        candidate_name = row["Candidate"]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1


with open(file_to_output, "w") as txt_file:
    election_results = (
        f"\n\nElection Results\n"
        f"------------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"------------------------------\n")
    print(election_results, end="")
    
    txt_file.write(election_results)

    #determine winner by looping through the counts
    for candidate in candidate_votes:

        #retrieve vote count and percentage
        votes = candidate_votes["candidate_name"]
        vote_percentage = float(votes) / float(total_votes) * 100

        #determine winning vote count and candidate
        if(votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
        
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        txt_file.write(voter_output)
    
    winning_candidate_summary = (
        f"-------------------------------\n"
        f"Winner: {winning_candidate} \n"
        f"-------------------------------\n")
    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)


    

