# Import CSV and JSON libraries
import csv
import json

# Specifying the Instance Variables / Defaults
# Specify the file where to read the players data from
# Converting data from CSV to JSON
csv_filename = input("Specify the file that you wish to process: ")
json_filename = csv_filename.split(".")[0] + ".json"

# Experienced and Inexperienced groups / lists inits
experienced = []
inexperienced = []

# Instance Variables for 3 teams / lists
# Setting number of Teams
TEAMS = 3
team_one = []
team_two = []
team_three = []
TEAM_ONE_NAME = "Sharks"
TEAM_TWO_NAME = "Dragons"
TEAM_THREE_NAME = "Raptors"

# Function for CSV to JSON conversion
def csv_to_json():
    try:
        with open(csv_filename, 'r') as csvfile:
            soccer_reader = csv.DictReader(csvfile, delimiter=",")
            rows = list(soccer_reader)
            with open(json_filename, 'w') as soccerfile:
                json.dump(rows, soccerfile)
    except:
        print("The file that you have specified has not been found, please try again.")

# Function for dividing experienced and inexperienced players
def experience_level():
    try:
        with open(json_filename, 'r') as soccer:
            players = json.load(soccer)
            for player in players:
                if player["Soccer Experience"] == "YES":
                    experienced.append(player)
                else:
                    inexperienced.append(player)
    except:
        print("The file that you have specified has not been found, please try again.")

# Function for creating 3 teams based on experience
def create_teams_based_on_experience(experienced, inexperienced):
    team_one.extend(experienced[:TEAMS])
    team_one.extend(inexperienced[:TEAMS])
    team_two.extend(experienced[TEAMS:TEAMS*2])
    team_two.extend(inexperienced[TEAMS:TEAMS*2])
    team_three.extend(experienced[TEAMS*2:TEAMS*3])
    team_three.extend(inexperienced[TEAMS*2:TEAMS*3])

# Function for writing the teams into the file
def list_of_teams(team_one, team_two, team_three):
    with open("teams.txt", "w") as file:
        file.write(TEAM_ONE_NAME + "\n")
        for player in team_one:
            file.write(player["Name"] + ", ")
            file.write(player["Soccer Experience"] + ", ")
            file.write(player["Guardian Name(s)"] + "\n")

# Converting data CSV to JSON
csv_to_json()

# Dividing experienced and inexperienced players
experience_level()

# Creating 3 teams based on same experience level
create_teams_based_on_experience(experienced, inexperienced)

# Write list of teams to teams.txt file
list_of_teams(team_one, team_two, team_three)

# Checking the results
for i in range(0, len(team_one)):
    print(team_one[i]['Name'] + " " + team_one[i]['Soccer Experience'] + " " + team_one[i]['Guardian Name(s)'])