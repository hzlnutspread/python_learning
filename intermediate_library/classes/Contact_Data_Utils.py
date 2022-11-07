class Contact_Data_Utils:
    def __init__(self):
        pass


def search_user_email(keyword, data):
    x = data.get(keyword)
    if x:
        print(x['email'])


def search_user_phone(keyword, data):
    x = data.get(keyword)
    if x:
        print(x['phone'])