import os
from app import create_app, db

app = create_app(os.environ['APP_SETTINGS'])

if __name__ == "__main__":
    app.run(host="0.0.0.0")
