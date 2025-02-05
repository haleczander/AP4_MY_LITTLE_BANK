from flask import Flask
from controllers import account_bp
from config import CONFIG

app = Flask(__name__)

app.register_blueprint(account_bp)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
