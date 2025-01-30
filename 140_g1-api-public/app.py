from flask import Flask

# Importer les Blueprints
from controllers import account_bp

app = Flask(__name__)

# Enregistrer les Blueprintss
app.register_blueprint(account_bp)

if __name__ == "__main__":
    app.run(debug=True)