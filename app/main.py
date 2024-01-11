from flask import Flask
import utils.script_inputs as script_inputs
from data_access.users import JsonUsersLoader
from routes.users import users_bp


app = Flask(__name__)
app.register_blueprint(users_bp, url_prefix='/api')


def main():
    users_dir_path = script_inputs.get_users_dir_path()
    JsonUsersLoader.users_dir_file_path = users_dir_path

    app.run(debug=True)


if __name__ == "__main__":
    main()

