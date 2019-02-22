from app import db

user_areas = db.Table('user_areas',
                      db.Column('rate', db.Integer, nullable=False),
                      db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
                      db.Column('area_id', db.Integer, db.ForeignKey('areas.id'), primary_key=True))

user_candidates = db.Table('user_candidates',
                           db.Column('rate', db.Integer, nullable=False),
                           db.Column('user_id', db.Integer, db.ForeignKey(
                               'users.id'), primary_key=True),
                           db.Column('candidate_id', db.Integer, db.ForeignKey('candidates.id'), primary_key=True))

candidate_areas = db.Table('candidate_areas',
                           db.Column('rate', db.Float, nullable=False),
                           db.Column('candidate_id', db.Integer, db.ForeignKey(
                               'candidates.id'), primary_key=True),
                           db.Column('area_id', db.Integer, db.ForeignKey('areas.id'), primary_key=True))


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    areas = db.relationship('Area', secondary=user_areas, lazy='subquery',
                            backref=db.backref('users', lazy=True))

    candidates = db.relationship('Candidate', secondary=user_candidates, lazy='subquery',
                                 backref=db.backref('users', lazy=True))

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return "<User %r>" % self.username


class Area(db.Model):
    __tablename__ = "areas"

    id = db.Column(db.Integer, primary_key=True)
    area_name = db.Column(db.String, nullable=False)

    def __init__(self, area_name):
        self.area_name = area_name

    def __repr__(self):
        return "Area <%r>" % self.area_name


class Candidate(db.Model):
    __tablename__ = "candidates"

    id = db.Column(db.Integer, primary_key=True)
    candname = db.Column(db.String, nullable=False)

    areas = db.relationship('Area', secondary=candidate_areas, lazy='subquery',
                            backref=db.backref('candidates', lazy=True))

    def __init__(self, candname):
        self.candname = candname

    def __repr__(self):
        return "Candidate <%r>" % self.candname
