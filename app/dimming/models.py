from app.params.models import Base
from app import db


class Dimming(Base):
    __tablename__ = "dimming_curves"

    name = db.Column("name", db.String(128), unique=True, nullable=False)
    color_type = db.Column("color_type", db.String(128), nullable=False)
    filename = db.Column("filename", db.String(256), unique=True, nullable=False)
