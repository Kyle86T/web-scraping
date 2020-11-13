from flask import Flask, render_template, redirect
from flask_pymongo import pymongo
import scrape_mars

app = Flask(__name__)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# ceeate the db
db=client.mars_db

@app.route("/")
def home():
    mars_data = db.mars_data.find()
    return render_template("index.html", mars_data=mars_data)

@app.route("/scrape")
def scraper():
    #clear out old results
    db.mars_data.drop()
    mars_data = scrape_mars.scrape()
    #inserts the data scraped from the mars site
    db.mars_data.insert_one(mars_data)
    
    #Sends the user back to the homepage
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)