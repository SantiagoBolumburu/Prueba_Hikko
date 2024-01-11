import os, json
import constants as c
from utils.custom_decorators import singleton
import utils.users as user_utils

@singleton
class JsonUsersLoader:
    users_dir_file_path = None

    """ Este metodo carga los usuarios directamente como estan el en el
      JSON. Como los 2 endpoints requieren los seguidores de los 
      usuarios, pero no los seguidos, se usa la otra funcion. 
      Aun asi, considere relevante mostrarla
    """
    def get_users(self) -> list:
        users = []
        for user_json_file in [file for file in os.listdir(JsonUsersLoader.users_dir_file_path) if file.endswith('.json')]:
            with open(os.path.join(JsonUsersLoader.users_dir_file_path, user_json_file)) as user_json_file_path:
                users.append(json.load(user_json_file_path))
        return users


    """ Este metodo, toma cada usuario de los JSON, e itera sobre su 
     lista de seguidos, creando por cada id un usuario (si no existia
     ya) que tiene una lista de los usuarios que lo siguen, en la que 
     se coloca el id usuario del “for” principal
    """
    def get_users_with_followers_ids(self) -> list:
        users_dict = {}

        for user_json_file in [file for file in os.listdir(JsonUsersLoader.users_dir_file_path) if file.endswith('.json')]:
            json_user = None
            
            with open(os.path.join(JsonUsersLoader.users_dir_file_path, user_json_file)) as user_json_file_path:
                json_user = json.load(user_json_file_path)
            
            for user_id in json_user[c.JSON_USER_USERS_FOLLOWING_PROPERTY]:
                users_dict.setdefault(user_id, user_utils.create_user_with_followers_ids(user_id))

                users_dict[user_id][c.USER_FOLLOWERS_PROPERTY].append(json_user[c.JSON_USER_ID_PROPERTY])
                
        return list(users_dict.values())


    

