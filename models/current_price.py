from Backend/app.py import db

class CurrentPrice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    gem_price = db.Column(db.Float)
    amazon_price = db.Column(db.Float)
    flipkart_price = db.Column(db.Float)
    snapdeal_price = db.Column(db.Float)
    tatacliq_price = db.Column(db.Float)

    def __repr__(self):
        return f'<CurrentPrice {self.name}>'