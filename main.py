from voter_system import User, Candidate, Election, VoterDB, CandidateDB

# Setup
voter_db = VoterDB()
candidate_db = CandidateDB()

# Add Candidates
candidate1 = Candidate("Alice", "Party A", "C001")
candidate2 = Candidate("Bob", "Party B", "C002")
candidate_db.add_candidate(candidate1)
candidate_db.add_candidate(candidate2)

# Add Voters
voter1 = User("John", 25, "V001")
voter2 = User("Jane", 17, "V002")  # Underage
voter3 = User("Emma", 30, "V003")
voter_db.add_voter(voter1)
voter_db.add_voter(voter2)
voter_db.add_voter(voter3)

# Activate Election
election = Election("General Election 2025", [candidate1, candidate2], "2025-01-01", "2025-01-05")
election.activate_election()

# Voting
candidate_db.list_candidates()
voter1.cast_vote(candidate_db, "C001")
voter2.cast_vote(candidate_db, "C002")
voter3.cast_vote(candidate_db, "C002")

# Show Results
election.get_results()
