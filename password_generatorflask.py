import random
from flask import Flask, render_template, request

app = Flask(__name__)

def generate_password(word):
    # Define the desired password length
    password_length = 8

    # Convert the input word into a list of characters
    word_chars = list(word)

    # Shuffle the characters to create a scrambled version
    random.shuffle(word_chars)

    # Ensure the password contains at least one uppercase letter and one digit
    if not any(char.isupper() for char in word):
        word_chars.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if not any(char.isdigit() for char in word):
        word_chars.append(random.choice('0123456789'))

    # Fill the password with random characters if it's shorter than the desired length
    while len(word_chars) < password_length:
        word_chars.append(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&'))

    # Combine the characters to create the final password
    password = ''.join(word_chars)
    
    return password

@app.route("/", methods=["GET", "POST"]) #Define the route for the url("/") that accepts GET and POST request
def password_generator():
    if request.method == "POST": #form submission
        input_word = request.form.get("input_word")
        password = generate_password(input_word)
        return render_template("result.html", password=password) #Renders the "result.html" template with the generated password
    return render_template("index.html") #If the request is GET, render the "index.html" template

if __name__ == "__main__":
    app.run(debug=True)
