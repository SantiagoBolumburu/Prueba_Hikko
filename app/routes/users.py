import random
from flask import Blueprint, jsonify
from data_access.users import JsonUsersLoader
import utils.users as users_utils


users_bp = Blueprint('users', __name__)
users_loader = JsonUsersLoader()


@users_bp.route("/users", methods=['GET'])
def get_all_user_from_json():
    return jsonify(users_loader.get_users_with_followers_ids()), 200


@users_bp.route("/users/leastfollowed", methods=['GET'])
def get_least_followed_user_from_json():
    users = users_loader.get_users_with_followers_ids()
    least_followed_users = users_utils.get_users_with_least_followers(users)
    return jsonify(random.choice(least_followed_users)), 200