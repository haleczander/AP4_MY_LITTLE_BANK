from flask import Flask
from controllers import account_bp, currency_bp, transaction_bp
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)


SWAGGER_URL="/swagger"
API_URL="/static/swagger.yaml"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Access API'
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

app.register_blueprint(account_bp)
app.register_blueprint(currency_bp)
app.register_blueprint(transaction_bp)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
