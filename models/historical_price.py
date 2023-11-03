from Backend/app.py import db

class HistoricalPrice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db., primary_key=True, nullable=False)
    low_price = db.Column(db.Float)

    def __repr__(self):
        return f'<HistoricalPrice {self.name}>'