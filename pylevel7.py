import csv
import os

# Define the path to the directory containing the system folders
base_path = "Semester_projekt/Pythonlevel7/pylevel7.py"
# Define dictionaries to store the progress datasdafafafafaf
weekly_system_progress = {}
weekly_access_progress = {"Identity Management": 0, "Central Auth System": 0, "Two-Factor Auth": 0, "Strong Password": 0, "Admin Privileges": 0}
total_system_progress = {}
total_access_progress = {"Identity Management": 0, "Central Auth System": 0, "Two-Factor Auth": 0, "Strong Password": 0, "Admin Privileges": 0}

# Loop through each system folder
for system_folder in os.listdir(base_path):
    # Define the path to the system folder
    system_folder_path = os.path.join(base_path, system_folder)
    
    # Initialize the progress data for this system
    weekly_system_progress[system_folder] = {"Week 1": 0, "Week 2": 0, "Week 3": 0}
    total_system_progress[system_folder] = 0
    
    # Loop through each week's CSV file in the system folder
    for week_file in os.listdir(system_folder_path):
        # Define the path to the week's CSV file
        week_file_path = os.path.join(system_folder_path, week_file)
        
        # Open the CSV file and read its contents
        with open(week_file_path, "r") as f:
            reader = csv.DictReader(f)
            # Loop through each row in the CSV file
            for row in reader:
                # Update the weekly system progress
                weekly_system_progress[system_folder]["Week " + row["week"]] += sum([int(row[k]) for k in row if k != "system_name" and k != "week"])
                
                # Update the weekly access compliance progress
                for k in row:
                    if k != "system_name" and k != "week":
                        weekly_access_progress[k] += int(row[k])
                
                # Update the total system progress
                total_system_progress[system_folder] += sum([int(row[k]) for k in row if k != "system_name" and k != "week"])
                
                # Update the total access compliance progress
                for k in row:
                    if k != "system_name" and k != "week":
                        total_access_progress[k] += int(row[k])

# Print the weekly system progress
print("Weekly System Progress:")
for system in weekly_system_progress:
    print(system)
    for week in weekly_system_progress[system]:
        print("\t" + week + ": " + str(weekly_system_progress[system][week]))

# Print the weekly access compliance progress
print("\nWeekly Access Compliance Progress:")
for k in weekly_access_progress:
    print(k + ": " + str(weekly_access_progress[k]))

# Print the total system progress
print("\nTotal System Progress:")
for system in total_system_progress:
    print(system + ": " + str(total_system_progress[system]))

# Print the total access compliance progress
print("\nTotal Access Compliance Progress:")
for k in total_access_progress:
    print(k + ": " + str(total_access_progress[k]))


