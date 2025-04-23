def main():
    # Providing choices for each prompt
    print("Choose a noun from the options:")
    noun = input("1. Dragon\n2. Pizza\n3. Car\nEnter the number of your choice: ")

    print("\nChoose an adjective from the options:")
    adj = input("1. Bizarre\n2. Super cool\n3. Mysterious\nEnter the number of your choice: ")

    print("\nChoose a verb from the options:")
    verb = input("1. Dance\n2. Jump\n3. Fly\nEnter the number of your choice: ")

    print("\nChoose a person's name:")
    person_name = input("1. Alex\n2. Jamie\n3. Sam\nEnter the number of your choice: ")

    # Assigning selected values to the choices
    if noun == "1":
        noun = "Dragon"
    elif noun == "2":
        noun = "Pizza"
    elif noun == "3":
        noun = "Car"

    if adj == "1":
        adj = "Bizarre"
    elif adj == "2":
        adj = "Super cool"
    elif adj == "3":
        adj = "Mysterious"

    if verb == "1":
        verb = "Dance"
    elif verb == "2":
        verb = "Jump"
    elif verb == "3":
        verb = "Fly"

    if person_name == "1":
        person_name = "Alex"
    elif person_name == "2":
        person_name = "Jamie"
    elif person_name == "3":
        person_name = "Sam"

    # Creating the Madlib story
    story = f" \nOne fine morning, {person_name} woke up with a {adj} idea to {verb} a giant {noun}. \
Everyone in the town thought it was crazy, but {person_name} was determined to make it happen! \
By noon, they had the whole city {verb}ing in excitement over the {noun}.\n"

    print("\n\t\tHere is your Madlib story:")
    print(story)

# Call the main function to run the game
main()
