def email_slicer(email):
    
    try:
        username, domain = email.split('@')
        return username, domain
    except ValueError:
        return None, None

def email_slicer_program():
    while True:
        email = input("Enter your email address: ")
        
        username, domain = email_slicer(email)
        
        if username and domain:
            print(f"\nUsername: {username}")
            print(f"Domain: {domain}")
        else:
            print("Invalid email format. Please try again.")

        use_again = input("\nDo you want to slice another email? (yes/y or no): ").lower()
        if use_again not in ['yes', 'y']:
            print("Thanks for using the Email Slicer! Goodbye!")
            break

email_slicer_program()
