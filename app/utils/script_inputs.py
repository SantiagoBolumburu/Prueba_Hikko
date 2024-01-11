import os, json, sys
import constants as c


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
print(__file__)
print(__location__)

def get_users_dir_path() -> str:
    users_dir_path = ''

    if sys.argv[1:]:
        users_dir_path = sys.argv[1]
    else:
        config = None
        with open(os.path.join(__location__, c.CONFIG_FILE_PATH_FROM_UTILS)) as config_file:
            config = json.load(config_file)
        users_relative_path = config[c.CONFIG_USERS_DIR_PATH_PROPERTY_NAME]
        combined_paths = os.path.join(__location__, users_relative_path)
        users_dir_path = os.path.abspath(combined_paths)
    
    return users_dir_path