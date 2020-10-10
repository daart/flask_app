from app import app
import os

@app.route("/")
def index():

    # Use os.getenv("key") to get environment variables
    app_name = os.getenv("APP_NAME")

    if app_name:
        return "Hello from {app_name} running in a Docker container behind Nginx!"

    return "Hello from Flask"

@app.route("/products", methods=["GET", "POST"])
def getpost():
    
    temp = app.db.products.find({})
    return str(list(temp))

@app.route("/products/<id>", methods=["GET", "PUT", "DELETE"])
def getputdelete(id):
    return 'single product with id: {}'.format(id)