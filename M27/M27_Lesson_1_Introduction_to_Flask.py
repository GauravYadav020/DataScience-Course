# M27 Lesson 1 – Introduction to Flask
# Short Description: Getting started with Flask, a lightweight Python web framework for building web applications.
# index.html ========================.

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>⚡ Electricity Bill Estimator</title>
#     <link rel="stylesheet" href="/static/style.css">
# </head>
# <body>

#     <h1>⚡ Electricity Bill Estimator</h1>
#     <p>Enter your monthly units to find out your bill!</p>

#     <form action="/calculate" method="POST">
#         <label>🔌 Units Consumed:</label>
#         <input type="number" name="units" placeholder="e.g. 150" required>
#         <button type="submit">Calculate 💡</button>
#     </form>

#     {% if bill %}
#     <div class="result">
#         <h2>Units Used: {{ units }} kWh</h2>
#         <h2>Total Bill: ₹ {{ bill }}</h2>
#         <p>{{ message }}</p>
#     </div>
#     {% endif %}

# </body>
# </html>

# app.py ================================================
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    units = int(request.form["units"])
    bill = units * 5

    if units <= 100:
        message = "Great! You are an energy saver! 🌱"
    elif units <= 200:
        message = "Not bad! Try saving a little more! 👍"
    else:
        message = "Whoa! Time to switch off some lights! 💡"

    return render_template("index.html", units=units, bill=bill, message=message)

if __name__ == "__main__":
    app.run(debug=True)


# style.css =========================================>

# body {
#   font-family: Arial, sans-serif;
#   background-color: #e0f7fa;
#   color: #003344;
#   text-align: center;
# }
 
# .container {
#   width: 500px;
#   background-color: white;
#   border: 3px solid #00acc1;
#   border-radius: 18px;
#   margin: 40px auto;
#   padding: 25px;
# }
 
# h1 {
#   color: #00838f;
# }
 
# form {
#   text-align: left;
# }
 
# label {
#   display: block;
#   font-weight: bold;
#   margin-top: 15px;
# }
 
# input {
#   width: 95%;
#   padding: 10px;
#   margin-top: 6px;
#   border: 2px solid #80deea;
#   border-radius: 8px;
# }
 
# button {
#   background-color: #00acc1;
#   color: white;
#   border: none;
#   border-radius: 20px;
#   padding: 12px 22px;
#   font-size: 16px;
#   font-weight: bold;
#   margin-top: 20px;
#   cursor: pointer;
# }
 
# button:hover {
#   background-color: #00838f;
# }
 
# .result {
#   background-color: #e0f2f1;
#   border: 2px dashed #00acc1;
#   border-radius: 12px;
#   margin-top: 25px;
#   padding: 15px;
#   text-align: left;
# }
 
# .result h2,
# .result h3 {
#   color: #006064;
# }
