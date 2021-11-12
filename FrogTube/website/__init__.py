from flask import Flask
from website.routes import video_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(video_blueprint)
    return app