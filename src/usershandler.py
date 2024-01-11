import constants as c
import os, json

def create_user(user_id:str) -> dict:
    return {c.USER_ID_PROPERTY : user_id, c.USER_FOLLOWERS_PROPERTY:[] }

def create_user_follower_count_format(user_id:str, amount_of_followers:str) -> dict:
    return {c.USER_ID_PROPERTY: user_id, c.USER_FOLLOWER_AMOUNT_PROPERTY: amount_of_followers}

class Users_Handler:
    def __init__(self, users_dir_file_path):
        self.users_dir_file_path = users_dir_file_path

    def get_users_from_json_in_id_followers_format(self) -> list:
        users_dict = {}

        for user_json_file in [file for file in os.listdir(self.users_dir_file_path) if file.endswith('.json')]:
            json_user = None
            
            with open(os.path.join(self.users_dir_file_path, user_json_file)) as user_json_file_path:
                json_user = json.load(user_json_file_path)
            
            for user_id in json_user[c.JSON_USER_USERS_FOLLOWING_PROPERTY]:
                users_dict.setdefault(user_id, create_user(user_id))

                users_dict[user_id][c.USER_FOLLOWERS_PROPERTY].append(json_user[c.JSON_USER_ID_PROPERTY])
                
        return list(users_dict.values())
    
    def get_users_with_least_followers(self, users:list) -> list:

        if not users:
            return []

        min_followers_amount = len(users[0][c.USER_FOLLOWERS_PROPERTY])
        least_followed_users = [create_user_follower_count_format(users[0][c.USER_ID_PROPERTY], min_followers_amount)]

        for user in users[1:]:
            followers_amount = len(user[c.USER_FOLLOWERS_PROPERTY])

            if followers_amount < min_followers_amount:
                min_followers_amount = followers_amount
                least_followed_users = [create_user_follower_count_format(user[c.USER_ID_PROPERTY], min_followers_amount)]
            
            elif followers_amount == min_followers_amount:
                least_followed_users.append(create_user_follower_count_format(user[c.USER_ID_PROPERTY], min_followers_amount))

        return least_followed_users