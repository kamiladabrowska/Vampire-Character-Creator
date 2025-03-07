import pytest
import os
import json
from project import load_characters, find_character, delete_character

TEST_FILE = "test_characters.json"

@pytest.fixture
def setup_test_file():
    """Creates a test JSON file with dummy characters before each test."""
    test_data = {
        "Alice": {
            "name": "Alice",
            "clan": "Brujah",
            "attributes": {"Strength": 3, "Dexterity": 2},
            "skills": {"Athletics": 2, "Brawl": 3}
        },
        "Bob": {
            "name": "Bob",
            "clan": "Tremere",
            "attributes": {"Strength": 2, "Dexterity": 3},
            "skills": {"Academics": 3, "Occult": 2}
        }
    }
    with open(TEST_FILE, "w", encoding="utf-8") as file:
        json.dump(test_data, file, indent=4)
    yield
    os.remove(TEST_FILE)


def test_delete_character(setup_test_file):
    """Tests if delete_character() removes a character from JSON file."""
    delete_character("Alice", TEST_FILE)

    # Check if Alice is deleted
    with open(TEST_FILE, "r", encoding="utf-8") as file:
        characters = json.load(file)

    assert "Alice" not in characters
    assert "Bob" in characters

def test_load_characters(setup_test_file):
    """Tests if load_characters() returns a list of character names."""
    character_list = load_characters(TEST_FILE)

    assert isinstance(character_list, list)
    assert len(character_list) == 2
    assert "Alice" in character_list
    assert "Bob" in character_list

def test_find_character(setup_test_file):
    """Tests if find_character() retrieves correct character data."""
    character = find_character("Bob", TEST_FILE)

    assert character is not None
    assert character["name"] == "Bob"
    assert character["clan"] == "Tremere"
    assert character["attributes"]["Strength"] == 2
