from app import db
# Define a base model for other database tables to inherit


class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())


class User(Base):
    __tablename__ = 'auth_user'
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False,
                      unique=True)
    password = db.Column(db.String(512), nullable=False)
    role = db.Column(db.SmallInteger)
    status = db.Column(db.SmallInteger)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User {}>'.format(self.name)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
