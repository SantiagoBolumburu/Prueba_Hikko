import constants as c


def create_user_with_followers_ids(user_id:str) -> dict:
    return {c.USER_ID_PROPERTY : user_id, c.USER_FOLLOWERS_PROPERTY:[] }


def create_user_with_follower_count(user_id:str, amount_of_followers:str) -> dict:
    user_id_key = c.USER_ID_PROPERTY
    user_follow_amt_key = c.USER_FOLLOWER_AMOUNT_PROPERTY
    return {user_id_key: user_id, user_follow_amt_key: amount_of_followers}


def get_users_with_least_followers(users:list) -> list:
    if not users:
        return []
    
    min_followers_amount = len(users[0][c.USER_FOLLOWERS_PROPERTY])
    user_id = users[0][c.USER_ID_PROPERTY]
    least_followed_user = create_user_with_follower_count(user_id, min_followers_amount)
    least_followed_users = [least_followed_user]

    for user in users[1:]:
        followers_amount = len(user[c.USER_FOLLOWERS_PROPERTY])
        user_id = user[c.USER_ID_PROPERTY]
        if followers_amount < min_followers_amount:
            min_followers_amount = followers_amount
            least_followed_user = create_user_with_follower_count(user_id, min_followers_amount)
            least_followed_users = [least_followed_user]
        elif followers_amount == min_followers_amount:
            least_followed_user = create_user_with_follower_count(user_id, min_followers_amount)
            least_followed_users.append(least_followed_user)

    return least_followed_users