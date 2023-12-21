import uuid
import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy.dialects.sqlite import JSON
from artist_app import db


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True, index=True)
    contents = db.Column(JSON)

    # id: so.Mapped[int] = so.mapped_column(primary_key=True)
    # public_id: so.Mapped[str] = so.mapped_column(sa.String(50), unique=True)
    # contents: so.Mapped[JSON] = so.mapped_column(sa.JSON)

    def __init__(self):
        self.public_id = str(uuid.uuid4())

    def __repr__(self):
        return '<Cart {}>'.format(self.public_id)