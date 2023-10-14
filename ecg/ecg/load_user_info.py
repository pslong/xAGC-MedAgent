
def getMatPath(user_name):
    """
    This function is used to load the mat files path for the user
    """

    user_map = {
        "张三": "/home/ubuntu/aimodel/ecg/dev-N.json",
        "李四": "/home/ubuntu/aimodel/ecg/dev-A.json",
        "王五": "/home/ubuntu/aimodel/ecg/dev-O.json",
        "其他人": "/home/ubuntu/aimodel/ecg/dev-N.json",
    }

    user_data_path = user_map.get(user_name)

    if not user_data_path:
        return user_map.get("其他人")
    else:
        return user_data_path

