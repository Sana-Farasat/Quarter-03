# Function to get the user input and generate the Mad Libs story
def generate_story():
    # Collect inputs from the user
    name = input("Enter your name: ")
    
    print("\nSelect a country from the following options:")
    countries = ["USA", "India", "Canada", "Australia", "Germany"]
    for idx, country in enumerate(countries, 1):
        print(f"{idx}. {country}")
    country_index = int(input("Enter the number of the country: ")) - 1
    country = countries[country_index]
    
    print("\nSelect a verb from the following options:")
    verbs = ["run", "jump", "swim", "dance", "fly"]
    for idx, verb in enumerate(verbs, 1):
        print(f"{idx}. {verb}")
    verb_index = int(input("Enter the number of the verb: ")) - 1
    verb = verbs[verb_index]
    
    print("\nSelect an adjective from the following options:")
    adjectives = ["beautiful", "sparkling", "huge", "colorful", "breezy"]
    for idx, adj in enumerate(adjectives, 1):
        print(f"{idx}. {adj}")
    adj_index = int(input("Enter the number of the adjective: ")) - 1
    adjective = adjectives[adj_index]
    
    print("\nSelect an animal from the following options:")
    animals = ["lion", "elephant", "giraffe", "panda", "zebra"]
    for idx, animal in enumerate(animals, 1):
        print(f"{idx}. {animal}")
    animal_index = int(input("Enter the number of the animal: ")) - 1
    animal = animals[animal_index]
    
    # Generate and print the story
    story = f"One day, {name} from {country} decided to {verb} near the {adjective} river. " \
            f"While walking, {name} saw a {animal} playing in the water. " \
            f"It was the most {adjective} thing {name} had ever seen!"
    
    print("\nHere's your Mad Libs story:")
    print(story)

# Run the function to get inputs and generate the story
generate_story()
