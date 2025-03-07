# **Vampire: The Masquerade 5E Character Manager**

## **Project Overview**

This project is a **Vampire: The Masquerade 5th Edition** (**VtM 5E**) **character manager** that allows players to **create, save, load, display, and manage** their characters. It follows the official VtM 5E character creation rules and provides an intuitive way to allocate attributes and skills, while also offering a visually formatted display of the character sheet.

The project is implemented in **Python** and includes functions for file handling with **JSON storage**, allowing users to **save and retrieve characters** at any time. The program is structured with **object-oriented programming (OOP)** principles and is designed for **CLI (Command Line Interface) interaction**.

---

## **Project Files**

This project consists of the following main files:

- **`character.py`**  
    Contains the `Character` class, which is responsible for creating, managing, saving, and displaying characters. This file includes all the logic for character attributes, skills, and file storage.
    
- **`project.py`**  
    The main script that interacts with the user. It includes:
    
    - The `main()` function, which serves as the program entry point.
    - Three standalone functions:`load_characters()`, `find_character(name)` and `delete_character(name)`.
    
- **`test_project.py`**  
    A test suite for validating critical functions using **pytest**. It includes tests for **loading, searching, and deleting characters** to ensure the program works as expected.
    
- **`requirements.txt`**  
    A list of external dependencies required to run the project.

---

## **Character Class**

The `Character` class is the core component of the project. It represents a **VtM 5E character**, including attributes, skills, and functionality for character creation and management.

### **Functionality of the Character Class**

- **Initialization (`__init__`)**  
    The class initializes a character with the following properties:
    
    - `name`: The character's name
    - `clan`: The character's chosen clan
    - `attributes`: A dictionary storing character attributes (e.g., Strength, Dexterity)
    - `skills`: A dictionary storing character skills (e.g., Stealth, Melee)
    
- **`create()` (Class Method)**  
    A **step-by-step interactive process** that prompts the user to:
    
    - Enter their **character name**
    - Select a **clan** from predefined options
    - Allocate **attribute points** based on official VtM 5E rules
    - Allocate **skill points** using a distribution system
    - Automatically calculate **secondary attributes** (Health, Willpower)
    
- **`display()`**  
    Uses the `PrettyTable` library to **format and display** the character's attributes and skills in an easy-to-read table. The character's **attribute and skill dots** are visually represented with **● (filled) and ○ (empty) markers**, mimicking the official character sheet style.
    
- **`save()`**  
    Saves the character’s information to a **JSON file** in a structured dictionary format. The character name serves as the **key**, allowing efficient lookup.
    
- **`from_dict()` (Class Method)**  
    Loads an existing character **from JSON data** and returns a `Character` instance.
    

---

## **Main Functions**

Apart from the `Character` class, the project includes **three additional functions** that work with saved characters:

### **1. `load_characters()`**

This function retrieves all stored character names from the **JSON file** and returns a list of available characters.

### **2. `find_character(name)`**

This function searches for a character **by name** in the JSON file and returns their **full character data** as a dictionary if found, or `None` if the character does not exist.

### **3. `delete_character(name)`**

This function allows the user to **permanently delete a character** from storage. It ensures that the file is properly updated and confirms deletion.

---

## **Design Choices**

- **Data Storage Format:**
    
    - The decision to use **JSON storage** instead of SQL was made for simplicity and ease of access. JSON allows **human-readable** data and is ideal for small-scale project like this.
    
- **Object-Oriented Design (OOP):**
    
    - The `Character` class encapsulates **all character-related actions**, ensuring a clean, modular design.
    - Methods like `from_dict()` ensure **easy reconstruction** of character instances from storage.
    
- **Validation & Error Handling:**
    
    - Input validation is enforced **at every step** to prevent incorrect attribute and skill allocation.
    - The **point distribution system** strictly follows VtM 5E rules, ensuring **game-accurate** character creation.
    
- **Visual Representation:**
    
    - The use of **PrettyTable** allows a structured, **table-like display** of characters.
    - **Dot markers (●, ○)** improve readability and provide a more immersive representation of stats.

---

## **How to Use**

1. **Run `project.py`**
2. **Create a new character** by following the on-screen prompts.
3. **View saved characters** using `load_characters()`.
4. **Find a specific character** using `find_character(name)`.
5. **Delete a character** if no longer needed with `delete_character(name)`.

---

## **Future Improvements**

This project is designed to be **expanded and improved**. Possible enhancements include:

- **GUI Implementation** using Tkinter or PyQt for a **graphical character sheet**.
- **SQL Database Support** for better scalability.
- **More Features** like **experience point allocation**, **disciplines manager** and **clan-specific abilities**.
- **Random generator** for player characters and for NPCs.

---

## **Final Thoughts**

This project was developed as a **CS50P final project** and serves as a **Vampire: The Masquerade 5E** character manager. It combines **OOP principles, file handling, input validation, and structured output** to create an efficient and game-accurate tool.

**Thank you for checking out this project!** 🦇🔥 If you have any feedback or suggestions, feel free to share.

---

## **Author**

- **Kamila Dąbrowska**
- **CS50P Final Project - 2025**

---

### **Technologies Used**

- **Python 3**
- **JSON**
- **PrettyTable (for formatted display)**
- **pytest (for unit testing)**

---

### **Installation**

To install dependencies, run:

`pip install -r requirements.txt`

---

## **License**

This project is released under the **MIT License**. Feel free to use and modify it as needed.

---

### 🎭 _"The night belongs to us."_ – Vampire: The Masquerade 🦇

---