from django.contrib.auth.hashers import make_password
from .utils.logging import logger


def register_user(user_data):
    try:
        user_data.validated_data["password"] = make_password(user_data.validated_data["password"])
        user_data.save()
        logger.info("User data saved.")
    except Exception as err:
        logger.error(f"Error occurred while registering the user. Log: {err}")
