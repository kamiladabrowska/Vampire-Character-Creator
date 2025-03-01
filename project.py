class Character:

    clans = ["Nosferatu", "Gangrel", "Tremere", "Torreador", "Vantrue", "Brujah", "Malkavian"]

    def __init__(self, name, clan, attributes=None, skills=None):
        self.name = name                #character's name
        self.clan = clan                #character's clan from the main handbook
        self.attributes = attributes or {
                                         "Strength": 0, "Dexterity": 0, "Stamina": 0,
                                        "Charisma": 0, "Manipulation": 0, "Composure": 0,
                                        "Intelligence": 0, "Wits": 0, "Resolve": 0
                                        }
        self.skills = skills or {}           #dict

    def __str__(self):
        return f"{self.name} - Clan: {self.clan}\n{self.attributes}"

    @classmethod
    def create(cls):
        """Method prompts the user for character details and initiates a character instance"""

        name = input("What's the name of your character?: ")

        #Clan selection
        for i, clan in enumerate(cls.clans, 1):
            print(f"{i}. {clan}")

        while True:
            clan_num = input(f"What's your character clan's number?: ")
            try:
                if 1 <= int(clan_num) <= len(cls.clans):
                    break
            except ValueError:
                print("Please provide a number")
                continue

        selected_clan = cls.clans[(int(clan_num)) - 1]

        #Defining possible points allocation
        expected_distribution = {4: 1, 3: 3, 2: 4, 1: 1}  # Number of attributes per value
        user_distribution = {}  # Store counts of assigned values

        #Asking user to attribute points
        print(f"Please allocate numbers for attributes as instructed below:\n"
              f"- Take your best Attribute at 4\n- Take your worst Attribute at 1\n- Take three Attributes at 3\n"
              f"- Take the rest of your Attributes at 2")

        attribute_names = ["Strength", "Dexterity", "Stamina",
                           "Charisma", "Manipulation", "Composure",
                           "Intelligence", "Wits", "Resolve"]

        character_attributes = {}
        for attribute in attribute_names:
            while True:
                try:
                    value = int(input(f"{attribute}: "))
                    user_distribution[value] = user_distribution.get(value, 0) + 1  # Count occurrences
                    character_attributes[attribute] = value     #add each attribute+points to a dict
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")

        #Skills

        #Validate if the points distribution matches the one from VtM5e rules
        if user_distribution == expected_distribution:
            return cls(name, selected_clan, character_attributes)
        else:
            print("Invalid attribute allocation. Please follow the rules and try again.")
            return None






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