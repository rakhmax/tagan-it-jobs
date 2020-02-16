from . import app
from . import views
from . import db
import os
from .api import __init__

app.config['SECRET_KEY'] = os.urandom(12)

if __name__ == "__main__":
    app.run()
