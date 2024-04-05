import logging
from flask import g
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint

from utils.decorators import access_pass
from schemas.user import UpdatePersonalDetailsSchema
from controllers.user.profile_controller import ProfileController


blp = Blueprint("profile", __name__, description="Update profile")

logger = logging.getLogger(__name__)


@blp.route("/my-profile")
class MyProfile(MethodView):

    def __init__(self) -> None:
        self.profile = ProfileController()

    # @access_pass(["Employee", "Admin"])
    @jwt_required()
    @blp.arguments(UpdatePersonalDetailsSchema)
    def put(self, user_profile_info):
        """Updates the profile info of an employee"""

        logger.info("[{g.request_id}] hits /my-profile put method endpoint")
        return self.profile.update_profile(user_profile_info)
    
    @jwt_required()
    # @access_pass(["Employee", "Admin"])
    def get(self):
        """Retreives the profile info of an employee"""

        logger.info("[{g.request_id}] hits /my-profile get method endpoint")
        return self.profile.show_profile()
