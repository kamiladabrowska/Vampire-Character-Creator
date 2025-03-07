import json
import os
from prettytable import PrettyTable


class Character:
    """Represents a Vampire: The Masquerade 5th Edition character."""

    clans = ["Nosferatu", "Gangrel", "Tremere", "Torreador", "Ventrue", "Brujah", "Malkavian"]

    def __init__(self, name, clan, attributes=None, skills=None):
        """Initialize a character with attributes and skills.

        Args:
            name (str): Character's name.
            clan (str): Character's clan.
            attributes (dict, optional): Attribute values. Defaults to base attributes.
            skills (dict, optional): Skill values. Defaults to base skills.
        """

        self.name = name  # Character's name
        self.clan = clan  # Character's clan from the main handbook
        self.attributes = attributes or {
            "Strength": 0, "Dexterity": 0, "Stamina": 0,
            "Charisma": 0, "Manipulation": 0, "Composure": 0,
            "Intelligence": 0, "Wits": 0, "Resolve": 0,
            "Health": 3, "Willpower": 0
        }
        self.skills = skills or {"Athletics": 0, "Brawl": 0, "Craft": 0, "Drive": 0, "Firearms": 0,
                                 "Larceny": 0, "Melee": 0, "Stealth": 0, "Survival": 0, "Animal Ken": 0,
                                 "Etiquette": 0, "Insight": 0, "Intimidation": 0, "Leadership": 0,
                                 "Performance": 0, "Persuasion": 0, "Streetwise": 0, "Subterfuge": 0,
                                 "Academics": 0, "Awareness": 0, "Finance": 0, "Investigation": 0, "Medicine": 0,
                                 "Occult": 0, "Politics": 0, "Science": 0, "Technology": 0
                                 }

    def __str__(self):
        """Returns a quick summary of the character."""
        return f"{self.name} - Clan: {self.clan}\nAttributes: {self.attributes}"

    @classmethod
    def from_dict(cls, data):
        """Creates a class instance from dict loaded from JSON file, ex via find_character()"""
        return cls(name=data["name"], clan=data["clan"], attributes=data["attributes"], skills=data["skills"])

    @classmethod
    def create(cls):
        """Method prompts the user for character details and initiates a character instance"""

        name = input("What's the name of your character?: ")

        # CLAN SELECTION
        for i, clan in enumerate(cls.clans, 1):
            print(f"{i}. {clan}")

        while True:
            try:
                clan_choice = int(input(f"\nEnter the number of your character's clan: "))
                if 1 <= clan_choice <= len(cls.clans):
                    selected_clan = cls.clans[clan_choice - 1]
                    break
                else:
                    print("Invalid choice. Please enter a number from the list.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # ATTRIBUTE ALLOCATION
        expected_attribute_distribution = {4: 1, 3: 3, 2: 4, 1: 1}  # Official VTM 5e distribution
        remaining_attributes = expected_attribute_distribution.copy()  # Dict for tracking remaining points
        temp_attributes = {}  # Temporary dict for validation

        print("\nPlease allocate numbers for attributes as instructed below:\n"
              "- Take your best Attribute at 4\n- Take your worst Attribute at 1\n"
              "- Take three Attributes at 3\n- Take the rest of your Attributes at 2")

        attribute_names = ["Strength", "Dexterity", "Stamina",
                           "Charisma", "Manipulation", "Composure",
                           "Intelligence", "Wits", "Resolve"]

        for attribute in attribute_names:
            while True:
                try:
                    value = int(input(f"{attribute}: "))

                    # Ensure valid allocation (user must follow 4-3-3-2-2-2-2-1)
                    if value not in remaining_attributes or remaining_attributes[value] <= 0:
                        print(f"Invalid choice! You have no remaining slots for attribute level {value}.")
                        continue  # Ask again

                    # Track assignment
                    temp_attributes[attribute] = value
                    remaining_attributes[value] -= 1  # Reduce available slots
                    break  # Move to next attribute
                except ValueError:
                    print("Invalid input! Please enter a number.")

        # Validation check
        if any(v != 0 for v in remaining_attributes.values()):
            print("Invalid attribute allocation. Please follow the rules and try again.")
            return None

        # Secondary Attributes
        temp_attributes["Health"] = temp_attributes["Stamina"] + 3
        temp_attributes["Willpower"] = temp_attributes["Composure"] + temp_attributes["Resolve"]

        # SKILL ALLOCATION
        skill_names = [
            "Athletics", "Brawl", "Craft", "Drive", "Firearms", "Larceny", "Melee", "Stealth", "Survival",  # Physical
            "Animal Ken", "Etiquette", "Insight", "Intimidation", "Leadership", "Performance", "Persuasion",
            "Streetwise", "Subterfuge",  # Social
            "Academics", "Awareness", "Finance", "Investigation", "Medicine", "Occult", "Politics",
            "Science", "Technology"  # Mental
        ]

        print("\nNow you need to pick the skill distribution type (number) from the below list:\n"
              "1. Jack of All Trades: One Skill at 3; eight Skills at 2; ten Skills at 1\n"
              "2. Balanced: Three Skills at 3; five Skills at 2; seven Skills at 1\n"
              "3. Specialist: One Skill at 4; three Skills at 3; three Skills at 2; three Skills at 1")

        # Get user choice for skill distribution
        while True:
            skill_distribution_choice = input("What is your choice?: ")
            if skill_distribution_choice == "1":
                expected_skill_distribution = {3: 1, 2: 8, 1: 10, 0: 8}
                break
            elif skill_distribution_choice == "2":
                expected_skill_distribution = {3: 3, 2: 5, 1: 7, 0: 12}
                break
            elif skill_distribution_choice == "3":
                expected_skill_distribution = {4: 1, 3: 3, 2: 3, 1: 3, 0: 17}
                break
            else:
                print("Invalid input. Please enter a number between 1-3.")

        # Get user skill points
        character_skills = {}
        remaining_skills = expected_skill_distribution.copy()  # Track available slots

        print(f"\nNow input your values. For skills you've not chosen, type '0'.")

        for skill in skill_names:
            while True:
                try:
                    value = int(input(f"{skill}: "))

                    # Ensure valid value
                    if value not in remaining_skills or remaining_skills[value] <= 0:
                        print(f"Invalid choice! You have no remaining slots for skill level {value}.")
                        continue  # Ask again

                    # Track assignment
                    character_skills[skill] = value
                    remaining_skills[value] -= 1  # Reduce available slots
                    break  # Move to next skill

                except ValueError:
                    print("Invalid input. Please enter a number.")

        # Check skill point distribution
        if any(v != 0 for v in remaining_skills.values()):
            print("\nSkill allocation is incorrect. Review the issues below:")
            for skill_level, remaining in remaining_skills.items():
                if remaining > 0:
                    print(f"You have {remaining} unused slots for skill level {skill_level}.")
                elif remaining < 0:
                    print(f"You assigned {abs(remaining)} too many points to skill level {skill_level}.")
            return None  # Restart input

        return cls(name, selected_clan, temp_attributes, character_skills)

    def display(self):
        """Displays character attributes and skills in a formatted table."""

        def format_points(value, max_points=5):
            filled = "●" * value
            empty = "○" * (max_points - value)
            return filled + empty + "   "

        column_type = ["Physical", "Social", "Mental"]

        # title
        print(f"Character: {self.name} (Clan: {self.clan})")
        # attributes
        table_attributes = PrettyTable()
        table_attributes.title = "Attributes"
        table_attributes.field_names = ["Physical", "Social", "Mental"]
        attributes_order = [
            ("Strength", "Charisma", "Intelligence"),
            ("Dexterity", "Manipulation", "Wits"),
            ("Stamina", "Composure", "Resolve")
        ]

        for col in column_type:
            table_attributes.min_width[col] = 27
            table_attributes.align[col] = "r"

        for physical, social, mental in attributes_order:
            table_attributes.add_row([
                physical + "     " + format_points(self.attributes[physical]),
                social + "     " + format_points(self.attributes[social]),
                mental + "     " + format_points(self.attributes[mental])
            ])

        print(table_attributes)

        # skills
        table_skills = PrettyTable()
        table_skills.title = "Skills"
        table_skills.field_names = ["Physical", "Social", "Mental"]
        skills_order = [
            ("Athletics", "Animal Ken", "Academics"),
            ("Brawl", "Etiquette", "Awareness"),
            ("Craft", "Insight", "Finance"),
            ("Drive", "Intimidation", "Investigation"),
            ("Firearms", "Leadership", "Medicine"),
            ("Larceny", "Performance", "Occult"),
            ("Melee", "Persuasion", "Politics"),
            ("Stealth", "Streetwise", "Science"),
            ("Survival", "Subterfuge", "Technology")
        ]

        for col in column_type:
            table_skills.min_width[col] = 27
            table_skills.align[col] = "r"

        for physical, social, mental in skills_order:
            table_skills.add_row([
                physical + "     " + format_points(self.skills[physical]),
                social + "     " + format_points(self.skills[social]),
                mental + "     " + format_points(self.skills[mental])
            ])

        print(table_skills)

        # secondary attributes
        table_secondary_attributes = PrettyTable()
        table_secondary_attributes.field_names = ["Health", "Willpower"]
        table_secondary_attributes.min_width["Health"] = 20
        table_secondary_attributes.min_width["Willpower"] = 20

        table_secondary_attributes.add_row([
            format_points(self.attributes["Health"], max_points=10),
            format_points(self.attributes["Willpower"], max_points=10)
        ])
        print(table_secondary_attributes)

    def save(self, filename="characters.json"):
        """Saves character data to a JSON file"""

        # create a dict with character data
        character_data = {
            self.name: {
                "name": self.name,
                "clan": self.clan,
                "attributes": self.attributes,
                "skills": self.skills
            }
        }

        # check if file exists
        if os.path.exists(filename):
            try:
                with open(filename, "r", encoding="utf8") as file:
                    characters = json.load(file)  # load existing characters from file
                    if not isinstance(characters, dict):  # If it's a list, replace with dict
                        characters = {}
            except json.JSONDecodeError:
                characters = {}  # if file is empty
        else:
            characters = {}  # create a new dict otherwise

        characters.update(character_data)  # add character dict to characters list

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(characters, file, indent=4)  # load updated characters data to json file

        print(f"Character: '{self.name}' has been saved successfully.")  # confirmation message

    @classmethod
    def find_by_name(cls):
        ...

    @classmethod
    def load_all(cls):
        ...
