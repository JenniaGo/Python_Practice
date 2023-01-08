from flask import Flask, request

app = Flask(__name__)

@app.route("/submit_ticket", methods=["POST"])
def submit_ticket():
  # Retrieve the form data from the request
  class_name = request.form["class_name"]
  computer_number = request.form["computer_number"]
  issue_description = request.form["issue_description"]
  
  # Store the ticket data in a database or file
  ticket_data = {
    "class_name": class_name,
    "computer_number": computer_number,
    "issue_description": issue_description
  }
  with open("tickets.json", "a") as f:
    json.dump(ticket_data, f)
    f.write("\n")
    
  return "Ticket submitted successfully"
