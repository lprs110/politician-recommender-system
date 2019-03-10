from app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True, nullable=False)
    full_name = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String, nullable=False)

    areas_rating = db.relationship("Area", secondary="user_areas")

    candidates_rating = db.relationship("Candidate", secondary="user_candidates")

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

    def __init__(self, username, fullname, password):
        self.username = username
        self.full_name = fullname
        self.password = password

    def __repr__(self):
        return "<User %r>" % self.username


class Area(db.Model):
    __tablename__ = "areas"

    id = db.Column(db.Integer, primary_key=True)
    area_name = db.Column(db.String, nullable=False)
    label = db.Column(db.String, nullable=False)

    users_rating = db.relationship("User", secondary="user_areas")

    candidates_tfidf = db.relationship("Candidate", secondary="candidate_areas")

    def __init__(self, area_name, label):
        self.area_name = area_name
        self.label = label

    def __repr__(self):
        return "Area <%r>" % self.area_name


class Candidate(db.Model):
    __tablename__ = "candidates"

    id = db.Column(db.Integer, primary_key=True)
    candname = db.Column(db.String, nullable=False)
    label = db.Column(db.String, nullable=False)

    users_rating = db.relationship("User", secondary="user_candidates")

    areas_tfidf = db.relationship("Area", secondary="candidate_areas")

    def __init__(self, candname, label):
        self.candname = candname
        self.label = label

    def __repr__(self):
        return "Candidate <%r>" % self.candname


class User_Areas(db.Model):
    __tablename__ = "user_areas"
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    area_id = db.Column(db.Integer, db.ForeignKey('areas.id'), primary_key=True)
    rate = db.Column(db.Integer, nullable=False)
    user = db.relationship("User", backref=db.backref("areas_ratings"))
    area = db.relationship("Area", backref=db.backref("users_area_ratings"))


class User_Candidates(db.Model):
    __tablename__ = "user_candidates"
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.id'), primary_key=True)
    rate = db.Column(db.Integer, nullable=False)
    user = db.relationship("User", backref=db.backref("candidates_ratings"))
    candidate = db.relationship("Candidate", backref=db.backref("users_cand_ratings"))


class Candidate_Areas(db.Model):
    __tablename__ = "candidate_areas"
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.id'), primary_key=True)
    area_id = db.Column(db.Integer, db.ForeignKey('areas.id'), primary_key=True)
    tfidf = db.Column(db.Float, nullable=False)
    candidate = db.relationship("Candidate", backref=db.backref("areas_cand_tfidf"))
    area = db.relationship("Area", backref=db.backref("cand_areas_tfidf"))
