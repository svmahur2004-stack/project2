from app import check_voting_eligibility

def test_eligible_voter():
    assert check_voting_eligibility("anu", 20) == "Anu is eligible to vote"

def test_not_eligible_voter():
    assert check_voting_eligibility("Ravi", 16) == "Ravi is not eligible to vote"
