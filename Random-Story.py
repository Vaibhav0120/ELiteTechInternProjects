import random

names = ["Alice", "Bob", "Charlie", "Dave", "Eva", "Luna", "Sam", "John", "Lily", "Mark"]
places = ["forest", "city", "mountain", "beach", "castle", "desert", "village", "space station"]
adjectives = ["brave", "smart", "kind", "mysterious", "funny", "adventurous", "curious", "bold"]
actions = ["found a hidden treasure", "rescued a friend", "fought a dragon", "discovered a secret passage", 
           "made a new invention", "defeated an evil sorcerer", "solved a great mystery", "escaped from a dungeon"]
companions = ["a talking cat", "an old wizard", "a friendly robot", "a magical unicorn", "a fearless knight"]
obstacles = ["a storm", "a fierce battle", "a sudden earthquake", "a trap", "a dark cave", "an evil villain"]
times = ["A long time ago", "Yesterday", "Last week", "In the future", "Once upon a time", "Many years ago"]

def generate_story():
    name = random.choice(names)
    place = random.choice(places)
    adjective = random.choice(adjectives)
    action = random.choice(actions)
    companion = random.choice(companions)
    obstacle = random.choice(obstacles)
    time = random.choice(times)

    story = (f"{time}, {name}, a {adjective} adventurer, set out on a journey to the {place}. "
             f"Along the way, {name} met {companion}, and together they {action}. "
             f"But their journey was not easy. They encountered {obstacle}, which tested their courage and wits. "
             f"In the end, they triumphed, and the {place} was never the same again.")
    return story

def story_generator():
    print("Welcome to the Random Story Generator!")

    while True:
        print("\n" + generate_story())
        use_again = input("\nDo you want to generate another story? (yes/y or no): ").lower()
        if use_again not in ['yes', 'y']:
            print("Thanks for using the Random Story Generator! Goodbye!")
            break

story_generator()
