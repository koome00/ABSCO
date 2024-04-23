from flask import Flask, jsonify
from app.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)

@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def not_authorized(error) -> str:
    """
    Not authorized
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """
    User forbidden
    """
    return jsonify({"error": "Forbidden"}), 403

if __name__ == "__main__":
    app.run()