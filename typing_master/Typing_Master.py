#!/usr/bin/env python
# coding: utf-8

# In[9]:


import json
import random
import time

# Constants
WORDS_JSON_FILE = "words.json"
LEADERBOARD_JSON_FILE = "leaderboard.json"

# Load words from a JSON file into a Python dictionary
def load_words_from_json(json_file):
    with open(json_file, "r") as file:
        words_data = json.load(file)
    return words_data

# Update and sort the leaderboard stored in a JSON file
def update_leaderboard(username, wpm, category):
    leaderboard_data = load_words_from_json(LEADERBOARD_JSON_FILE)
    leaderboard = leaderboard_data.get("leaderboard", [])

    leaderboard.append({"username": username, "wpm": wpm, "category": category})
    leaderboard.sort(key=lambda x: x["wpm"], reverse=True)

    leaderboard_data["leaderboard"] = leaderboard
    with open(LEADERBOARD_JSON_FILE, "w") as file:
        json.dump(leaderboard_data, file, indent=4)
# Show the leaderboard from the JSON file
def show_leaderboard():
    leaderboard = load_leaderboard()
    print("\nLeaderboard:")
    for index, entry in enumerate(leaderboard, start=1):
        print(f"{index}. {entry['username']} - {entry['wpm']} WPM ({entry['category']})")

# Get user input from the terminal
def get_user_input(prompt):
    return input(prompt)

# Main game logic
def main():
    while True:
        print("\nWelcome to the Typing Test Game!")
        username = get_user_input("Enter your username: ")

        while True:
            option = get_user_input("Choose a programming language (C/Python/Java/...), or type 'exit' to exit: ").capitalize()

            if option == "Exit":
                print("Goodbye!")
                return
            elif option in words_data:
                words = random.choice(words_data[option])
                print("\nType the following keywords:")
                print(words)

                start_time = time.time()
                user_input = get_user_input("Start typing (separate keywords with spaces): ")
                end_time = time.time()
                time_taken = end_time - start_time

                # Calculate words per minute
                words_typed = len(user_input.split())
                wpm = words_typed / (time_taken / 60)

                print(f"Keywords Typed: {words_typed}")
                print(f"Time Taken: {time_taken} seconds")
                print(f"Words Per Minute (WPM): {wpm}")

                # Update leaderboard
                update_leaderboard(username, wpm, option)

            else:
                print("Invalid programming language. Please choose a valid language or 'exit'.")

if __name__ == "__main__":
    words_data = load_words_from_json(WORDS_JSON_FILE)
    main()


# In[ ]:





# In[ ]:




