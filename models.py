from stamps_api import db

class Stamp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    origin = db.Column(db.String(100))
    rarity = db.Column(db.String(100))

    def __repr__(self):
        return '<Stamp %r>' % (self.name)
