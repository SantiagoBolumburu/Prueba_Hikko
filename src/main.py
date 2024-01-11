from flask import Flask, jsonify
import os, json, random, sys
import constants as c
import usershandler as uh

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

app = Flask(__name__)
user_handler = None

@app.route("/users")
def get_all_user_from_json():
    return jsonify(user_handler.get_users_from_json_in_id_followers_format())

@app.route("/users/leastfollowed")
def get_least_followed_user_from_json():
    users = user_handler.get_users_from_json_in_id_followers_format()

    users_with_least_followers = user_handler.get_users_with_least_followers(users)

    return jsonify(random.choice(users_with_least_followers))

def get_users_dir_path() -> str:
    users_dir_path = ''

    if sys.argv[1:]:
        users_dir_path = sys.argv[1]
    else:
        config = None
        with open(os.path.join(__location__, c.CONFIG_FILE_PATH)) as config_file:
            config = json.load(config_file)

        users_dir_path = os.path.join(__location__, config[c.CONFIG_USERS_DIR_PATH])
    
    return users_dir_path



if __name__ == "__main__":
    users_dir_path = get_users_dir_path()
    user_handler = uh.Users_Handler(users_dir_path)

    app.run(debug=True)




















# se asume que todos valores de "users_following" se corresponden a un "user_id" que si existe
# se asume que todos los archivos .json tiene usuarios en el formato dado, y solo un suaurio por archivo









