from flask import Flask, request, render_template_string

app = Flask(__name__)

payments = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Fee System - V1</title>
</head>

<body>

<h1>College Fee System</h1>
<h2>Version 1 - Add Payment</h2>

<form method="POST">

    <label>Student ID:</label><br>
    <input type="text" name="student_id" required>
    <br><br>

    <label>Student Name:</label><br>
    <input type="text" name="student_name" required>
    <br><br>

    <label>Fee Type:</label><br>
    <select name="fee_type">
        <option>Tuition Fee</option>
        <option>Exam Fee</option>
        <option>Hostel Fee</option>
        <option>Library Fee</option>
    </select>
    <br><br>

    <label>Amount:</label><br>
    <input type="number" name="amount" required>
    <br><br>

    <button type="submit">Add Payment</button>

</form>

{% if message %}
<h3>{{ message }}</h3>
{% endif %}

{% if payments %}

<h2>Payment Records</h2>

<table border="1" cellpadding="10">

<tr>
    <th>Student ID</th>
    <th>Student Name</th>
    <th>Fee Type</th>
    <th>Amount</th>
</tr>

{% for payment in payments %}

<tr>
    <td>{{ payment.student_id }}</td>
    <td>{{ payment.student_name }}</td>
    <td>{{ payment.fee_type }}</td>
    <td>₹{{ payment.amount }}</td>
</tr>

{% endfor %}

</table>

{% endif %}

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():

    message = ""

    if request.method == "POST":

        payment = {
            "student_id": request.form["student_id"],
            "student_name": request.form["student_name"],
            "fee_type": request.form["fee_type"],
            "amount": request.form["amount"]
        }

        payments.append(payment)

        message = "Payment added successfully!"

    return render_template_string(
        HTML,
        payments=payments,
        message=message
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)