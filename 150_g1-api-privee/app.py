from flask import Flask

# Importer les Blueprints
from controllers import account_bp, currency_bp, transaction_bp

app = Flask(__name__)

# Enregistrer les Blueprintss
app.register_blueprint(account_bp)
app.register_blueprint(currency_bp)
app.register_blueprint(transaction_bp)

if __name__ == "__main__":
    app.run(debug=True)
