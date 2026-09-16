import json

# Load missions from file
def load_missions(filename="data/missions.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save missions to file
def save_missions(missions, filename="data/missions.json"):
    with open(filename, "w") as f:
        json.dump(missions, f, indent=4)

# Add a new mission
def add_mission(missions, title, description, status="Pending"):
    mission = {
        "title": title,
        "description": description,
        "status": status
    }
    missions.append(mission)
    save_missions(missions)
    print(f"Mission '{title}' added successfully!")

# List all missions
def list_missions(missions):
    if not missions:
        print("No missions found.")
        return
    for i, mission in enumerate(missions, start=1):
        print(f"{i}. {mission['title']} - {mission['status']}")

# Update mission status
def update_status(missions, index, new_status):
    if 0 <= index < len(missions):
        missions[index]["status"] = new_status
        save_missions(missions)
        print(f"Mission '{missions[index]['title']}' updated to {new_status}.")
    else:
        print("Invalid mission index.")

# Main program loop
def main():
    missions = load_missions()
    while True:
        print("\n--- Dhurandhar Mission Tracker ---")
        print("1. Add Mission")
        print("2. List Missions")
        print("3. Update Mission Status")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Mission Title: ")
            description = input("Mission Description: ")
            add_mission(missions, title, description)
        elif choice == "2":
            list_missions(missions)
        elif choice == "3":
            list_missions(missions)
            index = int(input("Enter mission number to update: ")) - 1
            new_status = input("Enter new status (Pending/Ongoing/Completed): ")
            update_status(missions, index, new_status)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

