import json
from flask import Flask, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Connect to the MongoDB database
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]

# Define the route for submitting tickets
@app.route("/submit_ticket", methods=["POST"])
def submit_ticket():
  # Retrieve the form data from the request
  class_name = request.form["class_name"]
  computer_number = request.form["computer_number"]
  issue_description = request.form["issue_description"]
  
  # Store the ticket data in the MongoDB database
  ticket_data = {
    "class_name": class_name,
    "computer_number": computer_number,
    "issue_description": issue_description
  }
  result = db.tickets.insert_one(ticket_data)
  print(result.inserted_id)
  
  return "Ticket submitted successfully"

# Define the route for displaying the form
@app.route("/")
def show_form():
  return render_template("form.html")

# Run the app
if __name__ == "__main__":
  app.run()
