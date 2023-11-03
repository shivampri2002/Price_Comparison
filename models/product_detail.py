from Backend/app.py import db

class ProductDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    prod_detail = db.Column(db.String(300), nullable=False)
    features = db.Column(db.Text)
    img_url = db.Column(db.Text)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    def __repr__(self):
        return f'<ProductDetail {self.name}>'