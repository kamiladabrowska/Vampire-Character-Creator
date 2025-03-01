class Character:
    clans = ["Nosferatu", "Gangrel", "Tremere", "Torreador", "Vantrue", "Brujah", "Malkavian"]
    attributes = {
        "Strength": 0, "Dexterity": 0, "Stamina": 0,
        "Charisma": 0, "Manipulation": 0, "Composure": 0,
        "Intelligence": 0, "Wits": 0, "Resolve": 0
    }

    def __init__(self, name, clan, attributes=None, skills=None):
        self.name = name                #character
        self.clan = clan                #character's clan from the main handbook
        self.attributes = attributes    #dict
        self.skills = skills            #dict

    def __str__(self):
        return f"{self.name} - Clan: {self.clan}\n{self.attributes}"

    @classmethod
    def create(cls):
        """Method prompts the user for character details and initiates a character instance"""

        name = input("What's the name of your character?: ")
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

        print(f"Please allocate numbers for attributes as instructed below:\n"
              f"- Take your best Attribute at 4\n- Take your worst Attribute at 1\n- Take three Attributes at 3\n"
              f"- Take the rest of your Attributes at 2")

        character_attributes = {}

        try:
            for attribute in cls.attributes.keys():
                value = input(f"{attribute}: ")
                character_attributes.update({attribute: int(value)})
        except ValueError:
            pass

        #skills = input("What are your character's skills?: ")

        return cls(name, selected_clan, character_attributes)

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