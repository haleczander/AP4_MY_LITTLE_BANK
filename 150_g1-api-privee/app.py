from flask import Flask
from controllers import account_bp, currency_bp, transaction_bp

app = Flask(__name__)

app.register_blueprint(account_bp)
app.register_blueprint(currency_bp)
app.register_blueprint(transaction_bp)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
