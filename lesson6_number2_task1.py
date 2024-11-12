# User Input Data Processor

def validate_name_length(name, name_type):
    if len(name) < 2:
        print(f"Error: {name_type} name mustbe at least 2 characters long.")
        return False
    return True

def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    is_first_name_valid = validate_name_length(first_name, "First")
    is_last_name_valid = validate_name_length(last_name, "Last")

    if is_first_name_valif and is_last_name_valid:
        print("Both names are valid. ")
    else:
        print("Please enter valid names. ")

if __name__ == "__main__":
    main()