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

        self.name = name                # Character's name
        self.clan = clan                # Character's clan from the main handbook
        self.attributes = attributes or {
                        "Strength": 0, "Dexterity": 0, "Stamina": 0,
                        "Charisma": 0, "Manipulation": 0, "Composure": 0,
                        "Intelligence": 0, "Wits": 0, "Resolve": 0,
                        "Health": 3, "Willpower": 0
        }
        self.skills = skills or {"Athletics": 0, "Brawl": 0, "Craft": 0, "Drive": 0, "Firearms": 0,
                        "Larceny": 0, "Melee": 0, "Stealth": 0, "Survival": 0, "Animal Ken": 0,
                        "Etiquette": 0, "Insight": 0, "Intimidation": 0, "Leadership": 0,
                        "Performance": 0,  "Persuasion": 0, "Streetwise": 0, "Subterfuge": 0,
                        "Academics": 0, "Awareness": 0, "Finance": 0, "Investigation": 0, "Medicine": 0,
                        "Occult": 0, "Politics": 0, "Science": 0
        }

    def __str__(self):
        """Returns a quick summary of the character."""
        return f"{self.name} - Clan: {self.clan}\nAttributes: {self.attributes}"

    @classmethod
    def create(cls):
        """Method prompts the user for character details and initiates a character instance"""

        name = input("What's the name of your character?: ")

        # CLAN SELECTION
        for i, clan in enumerate(cls.clans, 1):
            print(f"{i}. {clan}")
        print()     # Spacing for readability

        while True:
            try:
                clan_choice = int(input(f"Enter the number of your character's clan: "))
                if 1 <= clan_choice <= len(cls.clans):
                    selected_clan = cls.clans[clan_choice - 1]
                    break
                else:
                    print("Invalid choice. Please enter a number from the list.")
            except ValueError:
                    print("Invalid input. Please enter a number.")

        #ATTRIBUTE ALLOCATION
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
            "Academics", "Awareness", "Finance", "Investigation", "Medicine", "Occult", "Politics", "Science"  # Mental
        ]

        print("\nNow you need to pick the skill distribution type (number) from the below list:\n"
        "1. Jack of All Trades: One Skill at 3; eight Skills at 2; ten Skills at 1\n"
        "2. Balanced: Three Skills at 3; five Skills at 2; seven Skills at 1\n"
        "3. Specialist: One Skill at 4; three Skills at 3; three Skills at 2; three Skills at 1")

        #Get user choice for skill distribution
        while True:
            skill_distribution_choice = input("What is your choice?: ")
            if skill_distribution_choice == "1":
                expected_skill_distribution = {3: 1, 2: 8, 1: 10, 0: 7}
                break
            elif skill_distribution_choice == "2":
                expected_skill_distribution = {3: 3, 2: 5, 1: 7, 0: 11}
                break
            elif skill_distribution_choice == "3":
                expected_skill_distribution = {4: 1, 3: 3, 2: 3, 1: 3, 0: 16}
                break
            else:
                print("Invalid input. Please enter a number between 1-3.")

        #Get user skill points
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

        #Check skill point distribution
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

        table = PrettyTable()
        table.title = f"Character: {self.name} (Clan: {self.clan})"
        table.field_names = ["Attribute", "Value"]

        for key, value in self.attributes.items():
            table.add_row([key, value])

        print(table)

        table_skills = PrettyTable()
        table_skills.title = "Skills"
        table_skills.field_names = ["Skill", "Value"]

        for key, value in self.skills.items():
            table_skills.add_row([key, value])

        print(table_skills)

    def save(self, filename="characters.json"):
        """Saves the character in a JSON file"""
        ...

    @classmethod
    def load_all(cls):
        ...

    @classmethod
    def find_by_name(cls):
        ...


def main():
    character = Character.create()
    print(character)

    character.display()


if __name__ == "__main__":
    main()