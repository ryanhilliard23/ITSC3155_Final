from . import models

from ..dependencies.database import engine


def index():
    models.Base.metadata.create_all(engine)