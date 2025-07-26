from flask import Flask, request
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

# Replace with your email and app password
EMAIL_ADDRESS = "youremail@gmail.com"
EMAIL_PASSWORD = "your_app_password_here"

@app.route("/submit", methods=["POST"])
def submit():
    fav_colour = request.form.get("fav_colour")

    # Save to file
    with open("submissions.txt", "a") as file:
        file.write(f"{fav_colour}\n")

    # Email setup
    msg = EmailMessage()
    msg["Subject"] = "New Color Submission"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_ADDRESS  # Send to yourself
    msg.set_content(f"New color submitted: {fav_colour}")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        return "Thanks for submitting!"
    except Exception as e:
        return f"Error sending email: {e}"

if __name__ == "__main__":
    app.run()

