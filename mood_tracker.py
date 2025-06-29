import csv
from datetime import datetime

# Function to log mood
def log_mood():
    mood = input("How are you feeling today? (e.g., Happy, Sad, Excited): ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open("moods.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, mood])
    
    print(f"Mood '{mood}' saved for {date}!\n")

# Function to view past moods
def view_moods():
    try:
        with open("moods.csv", "r") as file:
            reader = csv.reader(file)
            print("\n--- Mood History ---")
            for row in reader:
                print(f"{row[0]} - {row[1]}")
            print()
    except FileNotFoundError:
        print("No mood history found yet.\n")

from collections import Counter

def mood_stats():
    try:
        with open("moods.csv", "r") as file:
            reader = csv.reader(file)
            moods = [row[1] for row in reader]
            
            if not moods:
                print("No mood data to analyze.\n")
                return
            
            mood_counts = Counter(moods)
            most_common = mood_counts.most_common(1)[0]

            print("\n--- Mood Statistics ---")
            print(f"Total entries: {len(moods)}")
            print(f"Unique moods: {len(mood_counts)}")
            print("Mood counts:")
            for mood, count in mood_counts.items():
                print(f"  {mood}: {count}")
            print(f"Most common mood: {most_common[0]} ({most_common[1]} times)\n")

    except FileNotFoundError:
        print("No mood history found yet.\n")

# Main menu loop
def main_menu():
    while True:
        print("📘 Mood Tracker")
        print("1. Log today's mood")
        print("2. View mood history")
        print("3. View mood stats")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            log_mood()
        elif choice == "2":
            view_moods()
        elif choice == "3":
            mood_stats()
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main_menu()