from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from sqlalchemy.orm.session import Session
from sqlalchemy.sql import func
from sqlalchemy import desc,asc
from sqlalchemy.sql.expression import true

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = '674114312311aac1d81cf363a2c8a2bcbce3e31c9f098e3f0643ce2ea1d28f44'


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productName = db.Column(db.String(80), nullable=False)
    productQuantity = db.Column(db.Integer,default=0)

class SoldItems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productName = db.Column(db.String(80), nullable=False)
    productQuantity = db.Column(db.Integer,default=0)
    description = db.Column(db.String(80),nullable=true)

class BoughtItems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productName = db.Column(db.String(80), nullable=False)
    productQuantity = db.Column(db.Integer,default=0)
    description = db.Column(db.String(80),nullable=true)



@app.route("/addproduct",methods=["POST"])
def addProduct():
    if request.method == "POST":
        productName = request.form.get("productName")
        productQuantity = request.form.get("productQuantity")

        product = Products(
            productName=productName,
            productQuantity=productQuantity
        )

        db.session.add(product)
        db.session.commit()

        return redirect(url_for("index"))

@app.route("/delproduct/<id>",methods=["POST","GET"])
def deleteProduct(id):
    toBeDeleted = Products.query.filter(id == id).first()
    db.session.delete(toBeDeleted)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/boughtitem",methods=["POST"])
def boughtItem():
    if request.method == "POST":
        productName = request.form.get("productName")
        productQuantity = request.form.get("productQuantity")
        description = request.form.get("description")
        product = Products.query.filter(productName == productName).first()
        product.productQuantity = int(product.productQuantity) + int(productQuantity)
        boughtItem = BoughtItems(
            productName = productName,
            productQuantity = productQuantity,
            description = description
        )
        db.session.add(boughtItem)
        db.session.commit()
        return redirect(url_for("index"))


@app.route("/solditem",methods=["POST"])
def soldItem():
    if request.method == "POST":
        productName = request.form.get("productName")
        productQuantity = request.form.get("productQuantity")
        description = request.form.get("description")
        product = Products.query.filter(productName == productName).first()
        product.productQuantity = int(product.productQuantity) - int(productQuantity)
        soldItem = SoldItems(
            productName = productName,
            productQuantity = productQuantity,
            description = description
        )
        db.session.add(soldItem)
        db.session.commit()
        return redirect(url_for("index"))


@app.route("/")
def index():
    boughtData = BoughtItems.query.filter().all()
    soldData = SoldItems.query.filter().all()
    productsData = Products.query.filter().all()

    return render_template("index.html",
    boughtData=boughtData,
    soldData=soldData,
    productsData=productsData)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=true,host='0.0.0.0')