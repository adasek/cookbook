from flask import Flask

from cookbook.api import api_blueprint

if __name__ == "__main__":

    flask_app = Flask(__name__)

    # Register the blueprint
    flask_app.register_blueprint(api_blueprint)

    flask_app.run(host='0.0.0.0', port=5000, debug=True)
