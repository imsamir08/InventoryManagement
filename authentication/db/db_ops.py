from ..models import User
from django.contrib.auth.hashers import check_password
from ..exception.custom_exception import DoesNotExists, IncorrectCreds
from ..utils.logging import logger

def is_existing_user(user_data):
    user_name = user_data.validated_data["user_name"]
    email = user_data.validated_data["email"]
    return User.objects.filter(user_name=user_name).exists() or User.objects.filter(email=email).exists()


def check_login_details(login_data):
    username = login_data.validated_data["user_name"]
    password = login_data.validated_data["password"]

    try:
        user = User.objects.get(user_name = username)
        if check_password(password, user.password):
            return user
        else:
            raise IncorrectCreds()
    except Exception as err:
        logger.debug(f"Error while logging the user: {err}")
        raise DoesNotExists()
