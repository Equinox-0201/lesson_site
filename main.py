from flask import Flask, request

app = Flask(__name__)

@app.route("/submit", methods=["POST"])
def submit():
    fav_colour = request.form.get("fav_colour")
    with open("submissions.txt", "a") as file:
        file.write(f"{fav_colour}\n")
    return "Thanks for submitting!"

if __name__ == "__main__":
    app.run()
