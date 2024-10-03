def create_acronym(phrase):
    words = phrase.split()
    
    acronym = ''.join([word[0].upper() for word in words])
    
    return acronym

def acronym_creator():
    while True:
        phrase = input("Enter a phrase to create an acronym: ")

        acronym = create_acronym(phrase)

        print(f"The acronym for '{phrase}' is: {acronym}")
        
        use_again = input("\nDo you want to create another acronym? (yes or no): ").lower()
        if use_again not in ['yes', 'y']:
            print("Thanks for using the Acronym Creator! Goodbye!")
            break

acronym_creator()
