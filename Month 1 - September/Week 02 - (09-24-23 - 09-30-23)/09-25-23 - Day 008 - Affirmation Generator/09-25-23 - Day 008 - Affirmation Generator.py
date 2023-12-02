name = input("What's your name? ")
day = input("What day of the week is it? ").lower()
age = None

while age is None:
    age_input = input("How old are you? ")

    try:
        age = int(age_input)
    except ValueError:
        print("Please enter a valid number for your age.")

food = input("What's your go-to comfort food when you're feeling down? ").lower() 
sleep_type = input("Are you a morning person or a night owl? ").lower()

affirmations = []

age_group = None
if age < 18:
    age_group = "under 18"
elif age >= 18 and age <= 30:
    age_group = "18 to 30"
elif age > 30:
    age_group = "over 30"

if age_group == "under 18" and day == "monday" and sleep_type == "morning person":
    affirmations.append(f"Hey {name}! You're young, it's Monday, and you're a morning person. Keep that energy going!")
elif age_group == "under 18" and day == "monday" and sleep_type == "night owl":
    affirmations.append(f"{name}, you're young and a night owl on a Monday. Embrace your unique style!")
elif age_group == "under 18" and day == "friday" and sleep_type == "morning person":
    affirmations.append(f"Happy Friday, {name}! You're young, enjoy the end of the week!")
elif age_group == "under 18" and day == "friday" and sleep_type == "night owl":
    affirmations.append(f"{name}, it's Friday, and you're young and a night owl. Celebrate the weekend your way!")

elif age_group == "18 to 30" and day == "monday" and sleep_type == "morning person":
    affirmations.append(f"Hello {name}! You're in the prime of your life, and it's Monday. Make the most of the week!")
elif age_group == "18 to 30" and day == "monday" and sleep_type == "night owl":
    affirmations.append(f"{name}, you're in the prime of your life, you should charge into this week it make it yours!.")
elif age_group == "18 to 30" and day == "friday" and sleep_type == "morning person":
    affirmations.append(f"Happy Friday, {name}! You're in the prime of your life, and it's time to unwind!")
elif age_group == "18 to 30" and day == "friday" and sleep_type == "night owl":
    affirmations.append(f"{name}, it's Friday, and your youthful night owl spirit is ready for the weekend!")

elif age_group == "over 30" and day == "monday" and sleep_type == "morning person":
    affirmations.append(f"Welcome, {name}! your a morning person so you should be off to a great start to your week!")
elif age_group == "over 30" and day == "monday" and sleep_type == "night owl":
    affirmations.append(f"{name}, your {age} years bring wisdom to tackle this new week!")
elif age_group == "over 30" and day == "friday" and sleep_type == "morning person":
    affirmations.append(f"Happy Friday, {name}! Your {age} years are a treasure, and it's time to relax.")
elif age_group == "over 30" and day == "friday" and sleep_type == "night owl":
    affirmations.append(f"{name}, it's Friday, and your {age} years young, go out and let your night owl spirit shine!")

default_affirmation = f"Hello, {name}! Remember, every day is a new opportunity to learn and grow. Stay positive and keep moving forward."

selected_affirmation = affirmations[0] if affirmations else default_affirmation
print()
print("Here's your affirmation for today:")
print(selected_affirmation)