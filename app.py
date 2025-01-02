from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/rsvp", methods=["POST"])
def save_rsvp():
    # Extract data from the form
    name = request.form.get("name")
    attendance = request.form.get("attendance")
    guests = request.form.get("guests")

    # Load or create the Excel file
    file_path = "rsvp_data.xlsx"
    try:
        df = pd.read_excel(file_path)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Name", "Attendance", "Guests"])

    # Add the new RSVP entry
    new_data = {"Name": name, "Attendance": attendance, "Guests": guests}
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)

    # Save the updated data to the Excel file
    df.to_excel(file_path, index=False)

    return "Thank you for your RSVP! We look forward to seeing you."

if __name__ == "__main__":
    app.run(debug=True)