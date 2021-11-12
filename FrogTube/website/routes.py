from flask import Blueprint, render_template
from .vid_generator import generate_video

video_blueprint = Blueprint("video", __name__)

@video_blueprint.route("/")
@video_blueprint.route("/home")
def video():
    return(render_template("home.html", video_id = generate_video()))
