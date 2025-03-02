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

        self.name = name                #character's name
        self.clan = clan                #character's clan from the main handbook
        self.attributes = attributes or {
                                         "Strength": 0, "Dexterity": 0, "Stamina": 0,
                                        "Charisma": 0, "Manipulation": 0, "Composure": 0,
                                        "Intelligence": 0, "Wits": 0, "Resolve": 0,
                                        "Health": 3, "Willpower": 0
                                        }
        self.skills = skills or     {"Athletics": 0, "Brawl": 0, "Craft": 0, "Drive": 0, "Firearms": 0,
                                     "Larceny": 0, "Melee": 0, "Stealth": 0, "Survival": 0, "Animal Ken": 0,
                                     "Etiquette": 0, "Insight": 0, "Intimidation": 0, "Leadership": 0,
                                     "Performance": 0,  "Persuasion": 0, "Streetwise": 0, "Subterfuge": 0,
                                     "Academics": 0, "Awareness": 0, "Finance": 0, "Investigation": 0, "Medicine": 0,
                                     "Occult": 0, "Politics": 0, "Science": 0
                                     }

    def __str__(self):
        return f"{self.name} - Clan: {self.clan}\n{self.attributes}"

    @classmethod
    def create(cls):
        """Method prompts the user for character details and initiates a character instance"""

        name = input("What's the name of your character?: ")

        #CLAN

        #Print the possible clan selections
        for i, clan in enumerate(cls.clans, 1):
            print(f"{i}. {clan}")

        #Select clan and validate user input
        while True:
            clan_num = input(f"What's your character clan's number?: ")
            try:
                if 1 <= int(clan_num) <= len(cls.clans):
                    selected_clan = cls.clans[(int(clan_num)) - 1]
                    break
                else:
                    print("Invalid choice. Please enter a number from the list.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        #ATTRIBUTES

        #Defining possible points allocation
        expected_attribute_distribution = {4: 1, 3: 3, 2: 4, 1: 1}  # Number of attributes per value
        user_attribute_distribution = {}  # Store counts of assigned values

        #Asking user to attribute points
        print(f"Please allocate numbers for attributes as instructed below:\n"
              f"- Take your best Attribute at 4\n- Take your worst Attribute at 1\n- Take three Attributes at 3\n"
              f"- Take the rest of your Attributes at 2")

        attribute_names = ["Strength", "Dexterity", "Stamina",
                           "Charisma", "Manipulation", "Composure",
                           "Intelligence", "Wits", "Resolve"]

        temp_attributes = {}  # Temporary dict for validation
        remaining_attributes = expected_attribute_distribution.copy()   # Dict for tracking remaining points

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

        # Validate if the points distribution matches VtM5e rules
        if user_attribute_distribution != expected_attribute_distribution:
            print("Invalid attribute allocation. Please follow the rules and try again.")
            return None

        # If valid, store in final attributes dictionary
        character_attributes = temp_attributes

        # Secondary Attributes
        character_attributes["Health"] = character_attributes["Stamina"] + 3
        character_attributes["Willpower"] = character_attributes["Composure"] + character_attributes["Resolve"]

        #Skills
        skill_names = [
            "Athletics", "Brawl", "Craft", "Drive", "Firearms", "Larceny", "Melee", "Stealth", "Survival",  # Physical
            "Animal Ken", "Etiquette", "Insight", "Intimidation", "Leadership", "Performance", "Persuasion",
            "Streetwise", "Subterfuge",  # Social
            "Academics", "Awareness", "Finance", "Investigation", "Medicine", "Occult", "Politics", "Science"  # Mental
        ]

        print(f"""Now you need to pick the skill distribution type (number) from the below list:
        1. Jack of All Trades: One Skill at 3; eight Skills at 2; ten Skills at 1
        2. Balanced: Three Skills at 3; five Skills at 2; seven Skills at 1"
        3. Specialist: One Skill at 4; three Skills at 3; three Skills at 2; three Skills at 1""")

        #Get user choice for skill distribution
        while True:
            skill_dist_type = input("What is your choice?: ")
            if skill_dist_type == "1":
                expected_skill_distribution = {3:1, 2:8, 1:10, 0:5}
                break
            elif skill_dist_type == "2":
                expected_skill_distribution = {3:3, 2:5, 1:7, 0:9}
                break
            elif skill_dist_type == "3":
                expected_skill_distribution = {4:1, 3:3, 2:3, 1:3, 0:14}
                break
            else:
                print("Invalid input. Please enter a number between 1-3.")
                continue

        #Get user skill points
        character_skills = {}
        user_skill_distribution = {}
        remaining_skills = expected_skill_distribution.copy()  # Track available slots

        print(f"Now input your values. For skills you've not chosen, type '0'.")
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
            print("Skill allocation is incorrect. Please follow the rules.")

            # Show user their mistakes
            for skill_level, remaining in remaining_skills.items():
                if remaining > 0:
                    print(f"You have {remaining} unused slots for skill level {skill_level}.")
                elif remaining < 0:
                    print(f"You assigned {abs(remaining)} too many points to skill level {skill_level}.")

            return None  # Restart input

        return cls(name, selected_clan, character_attributes, character_skills)


    def display(self):
        """Displays character information in a formated way"""
        ...

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


if __name__ == "__main__":
    main()