import os
import json
from character import Character

def main():
    # Load character data from JSON file
    #print(load_characters())

    #nina = find_character("Nina")
    #character = Character.from_dict(nina)

    # Display character details
    #character.display()

    delete_character("Nina2")


def load_characters(filename="characters.json"):
    """Returns a list of characters from JSON file"""

    # open json file - handle cases if it doesn't exist or is empty
    if not os.path.exists(filename):
        print("The file doesn't exist.")
        return []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            characters = json.load(file)
    except json.JSONDecodeError:
        print("There are no saved characters.")
        return []

    return list(characters.keys())

def find_character(name, filename="characters.json"):
    """Returns character data in a dict if it is saved in JSON file, else returns None"""

    if not os.path.exists(filename):
        return None

    try:
        with open(filename, "r", encoding="utf-8") as file:
            characters = json.load(file)
            if not isinstance(characters, dict):  # Ensure it's a dictionary
                return None
    except json.JSONDecodeError:
        return None

    # if name in the file return the character dict
    return characters.get(name)

def delete_character(name, filename="characters.json"):
    """Deletes a character from JSON file"""

    if not os.path.exists(filename):
        print("The file doesn't exist.")
        return None

    try:
        with open(filename, "r", encoding="utf-8") as file:
            characters = json.load(file)
    except json.JSONDecodeError:
        print("File is empty or corrupted.")

    if name not in characters:
        print(f"Character {name} not found.")
        return None

    characters.pop(name)

    with open(filename, "w", encoding="utf-8") as file:
            json.dump(characters, file, indent=4)

    print(f"Character {name} has been deleted.")


def export_character(name, filename="characters.json"):
    ...


if __name__ == "__main__":
    main()
