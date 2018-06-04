# Import CSV and JSON libraries
import csv
import json
import os

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
def create_teams():
    with open(json_filename, 'r') as soccer:
        players = json.load(soccer)
        if ((len(players) % 3) == 0):
            for player in players:
                if player["Soccer Experience"] == "YES":
                    experienced.append(player)
                else:
                    inexperienced.append(player)

            team_one.extend(experienced[:TEAMS])
            team_one.extend(inexperienced[:TEAMS])
            team_two.extend(experienced[TEAMS:TEAMS * 2])
            team_two.extend(inexperienced[TEAMS:TEAMS * 2])
            team_three.extend(experienced[TEAMS * 2:TEAMS * 3])
            team_three.extend(inexperienced[TEAMS * 2:TEAMS * 3])
        else:
            print("You have provided a file with unequal amount of players to be sufficient for {} teams".format(TEAMS))

# Function for writing the teams into the file
# Tuple of teams
# Creating dictionary from names and teams
def list_of_teams(*args):
    teams = args
    team_name_list = [TEAM_ONE_NAME, TEAM_TWO_NAME, TEAM_THREE_NAME]
    team_dict = {}
    for i in range(0, len(team_name_list)):
        team_dict[team_name_list[i]] = teams[i]
    with open("teams.txt", "w") as file:
        for key, values in team_dict.items():
            file.write("=" * 41 + "\n")
            file.write(key + "\n")
            for player in values:
                file.write(player["Name"] + ", ")
                file.write(player["Soccer Experience"] + ", ")
                file.write(player["Guardian Name(s)"] + "\n")
            file.write("=" * 41 + "\n\n")

# Function for writing a letter to each player
def letter_to_player(*args):
    teams = args
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)
    for i in range(0, len(teams)):
        for player in teams[i]:
            filename = player["Name"].replace(' ', '_').lower() + ".txt"
            with open(DIRECTORY + "/" + filename, "w") as file:
                file.write(LETTER.format(player["Name"]))

# Script doesn't execute when imported
if __name__ == '__main__':
    # Specifying the Instance Variables / Defaults
    # Specify the file where to read the players data from
    # Converting data from CSV to JSON
    csv_filename = input("Specify the filename that you wish to process: ")
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
    TEAM_ONE_NAME = input("Pick a name for team 1: ")
    TEAM_TWO_NAME = input("Pick a name for team 2: ")
    TEAM_THREE_NAME = input("Pick a name for team 3: ")

    DIRECTORY = "letters"
    LETTER = """Dear {},
    

    """

    # Converting data CSV to JSON
    csv_to_json()

    # Create teams based on experience level
    create_teams()

    # Write list of teams to teams.txt file
    list_of_teams(team_one, team_two, team_three)

    # Write a letter to each player
    letter_to_player(team_one, team_two, team_three)
