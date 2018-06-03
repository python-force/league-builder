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

# Converting data CSV to JSON
csv_to_json()

# Dividing experienced and inexperienced players
experience_level()