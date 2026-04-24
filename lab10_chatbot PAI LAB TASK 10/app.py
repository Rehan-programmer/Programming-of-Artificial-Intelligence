from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_bot_response(user_input):
    user_input = user_input.lower()

    if "admission" in user_input:
        return "Admissions are open. Requirements include previous transcripts and entry test."
    elif "deadline" in user_input:
        return "The admission deadline is 30th September."
    elif "programs" in user_input:
        return "We offer BSCS, BBA, and Engineering programs."
    elif "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you?"
    else:
        return "Sorry, I don't understand. Please ask about admissions, deadlines, or programs."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.form["msg"]
    return get_bot_response(user_input)

if __name__ == "__main__":
    app.run(debug=True)
