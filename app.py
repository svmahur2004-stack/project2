def check_voting_eligibility(name, enquiry_type, age):
    result = (
        f"Name: {name}\n"
        f"Enquiry Type: {enquiry_type}\n"
        f"Age: {age}\n"
    )

    if age >= 18:
        result += "Status: Eligible to vote"
    else:
        result += "Status: Not eligible to vote"

    return result


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("Usage: python app.py <name> <enquiry_type> <age>")
        sys.exit(1)

    name = sys.argv[1]
    enquiry_type = sys.argv[2]
    age = int(sys.argv[3])

    print(check_voting_eligibility(name, enquiry_type, age))
