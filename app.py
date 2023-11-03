import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


#models
class ProductDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    prod_detail = db.Column(db.Text(), nullable=False)
    features = db.Column(db.Text())
    img_url = db.Column(db.Text())
    category = db.Column(db.String(30))		#add gem_url
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now(), onupdate=func.current_timestamp())

    def __repr__(self):
        return f'<ProductDetail {self.name}>'


class CurrentPrice(db.Model):
    id = db.Column(db.Integer, db.ForeignKey(ProductDetail.id), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    gem_price = db.Column(db.Float)
    amazon_price = db.Column(db.Float)
    flipkart_price = db.Column(db.Float)
    snapdeal_price = db.Column(db.Float)
    tatacliq_price = db.Column(db.Float)

    product = db.relationship('ProductDetail', foreign_keys='CurrentPrice.id')

    def __repr__(self):
        return f'<CurrentPrice {self.name}>'



class HistoricalPrice(db.Model):
    id = db.Column(db.Integer, db.ForeignKey(ProductDetail.id), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime(timezone=True), primary_key=True, nullable=False)
    low_price = db.Column(db.Float)

    product_det = db.relationship('ProductDetail', foreign_keys='HistoricalPrice.id', primaryjoin='HistoricalPrice.id == ProductDetail.id')

    def __repr__(self):
        return f'<HistoricalPrice {self.name}>'





#views and routes

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
	return render_template('index.html')


@app.route('/productlist/<prodname>')
def productList(prodname):
	return render_template('productList.html')


@app.route('/productdetail/<prodname>/<int:id>')
def productDetail(prodname, id):
	return render_template('productDetail.html')




if __name__ == "__main__":
    app.run(debug=True)