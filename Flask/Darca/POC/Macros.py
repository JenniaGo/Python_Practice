def submit_ticket(class_name, computer_number, issue_description):
  ticket_data = {
    "class_name": class_name,
    "computer_number": computer_number,
    "issue_description": issue_description
  }
  
  # Store the ticket data in a database or file
  # For example, you could use a JSON file to store the tickets
  with open("tickets.json", "a") as f:
    json.dump(ticket_data, f)
    f.write("\n")

# Example usage of the submit_ticket function
submit_ticket("Math 101", "C4", "Computer is not turning on")
submit_ticket("English 201", "A2", "Keyboard is not working")
