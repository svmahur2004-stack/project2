from app import check_voting_eligibility

def test_eligible_voter():
    assert check_voting_eligibility("anu", "Voting", 20) == "anu is eligible to vote"

def test_not_eligible_voter():
    assert check_voting_eligibility("Ravi", "Voting", 16) == "Ravi is not eligible to vote"
