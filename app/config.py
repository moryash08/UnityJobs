import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """The class creates a connection to the database"""

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
