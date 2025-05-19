from flask import Flask
from routes.complaint_routes import complaint_bp
from routes.user_routes import user_bp

app = Flask(__name__)
app.register_blueprint(complaint_bp)
app.register_blueprint(user_bp)

if __name__ == "__main__":
    app.run(debug=True)
