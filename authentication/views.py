from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .db.db_ops import is_existing_user, check_login_details
from .service import register_user
from .utils.logging import logger
from .exception.custom_exception import IncorrectCreds, DoesNotExists


from .serializer import UserSerializer, LoginSerializer
# Create your views here.



@api_view(["POST"])
def user_registration(request):

    user_data = UserSerializer(data=request.data)
    if user_data.is_valid():
        if is_existing_user(user_data):
            return Response("An account with provided username or email already exists. Please use different email/username.", status=status.HTTP_400_BAD_REQUEST)
        else:
            register_user(user_data)
            return Response("Successfully registered the user.", status=status.HTTP_201_CREATED)
    else:
        logger.debug("Error while registering user: ", user_data.errors)
    return Response("Some error occurred.", status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def user_login(request):
    login_data = LoginSerializer(data=request.data)

    if login_data.is_valid():
        user = check_login_details(login_data)
        try:
            return Response(data=f"{user.name}'s login completed.", status=status.HTTP_201_CREATED)
        except DoesNotExists as err:
            return Response(data=err, status=status.HTTP_404_NOT_FOUND)
        except IncorrectCreds as err:
            return Response(data=err, status=status.HTTP_400_BAD_REQUEST)