import requests
import json
from replit import db

def get_random_joke():
    result = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
    return result.json()

def print_joke(joke):
    print(joke["joke"])

def main():
    while True:
        user_choice = input("Choose an option:\n (n)ew joke, (s)aved joke, or (q)uit: ").lower()

        if user_choice == 'q':
            break

        if user_choice == 'n':
            joke = get_random_joke()
            print_joke(joke)

            save_joke = input("Do you want to save this joke? (yes/no): ").lower()

            if save_joke == "yes":
                saved_jokes = db["saved_jokes"] if "saved_jokes" in db.keys() else []
                saved_jokes.append(joke["id"])
                db["saved_jokes"] = saved_jokes

        elif user_choice == 's':
            saved_jokes = db["saved_jokes"] if "saved_jokes" in db.keys() else []

            if saved_jokes:
                print("Your saved jokes:")
                for saved_joke_id in saved_jokes:
                    saved_joke = requests.get(f"https://icanhazdadjoke.com/j/{saved_joke_id}", headers={"Accept": "application/json"}).json()
                    print_joke(saved_joke)
            else:
                print("No saved jokes available.")

        else:
            print("Invalid choice. Please enter 'n', 's', or 'q'.")

if __name__ == "__main__":
    main()