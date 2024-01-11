import os, json, sys
import constants as c


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


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