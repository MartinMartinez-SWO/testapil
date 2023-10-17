from flask import Flask

from routes import cron_blueprint


app = Flask(__name__)

FLASK_API_PREFIX = '/api'


# Blueprints
app.register_blueprint(cron_blueprint, url_prefix=FLASK_API_PREFIX + '/cron')

if __name__ == "__main__":
    app.run(port=5001)