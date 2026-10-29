from flask import Flask, request, render_template_string

app = Flask(__name__)

payments = []


TOTAL_FEE = 50000

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Fee System - V2</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f6f8;
            margin: 0;
            padding: 30px;
        }

        .container {
            max-width: 900px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
        }

        h1 {
            text-align: center;
        }

        .version {
            text-align: center;
            color: #555;
        }

        .section {
            margin-top: 30px;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 8px;
        }

        input, select {
            width: 100%;
            padding: 10px;
            margin-top: 5px;
            margin-bottom: 15px;
            box-sizing: border-box;
        }

        button {
            padding: 10px 20px;
            cursor: pointer;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 15px;
        }

        th, td {
            border: 1px solid #ccc;
            padding: 10px;
            text-align: center;
        }

        th {
            background-color: #eee;
        }

        .success {
            color: green;
            font-weight: bold;
        }

        .due {
            color: red;
            font-weight: bold;
        }
    </style>
</head>

<body>

<div class="container">

    <h1>College Fee System</h1>

    <p class="version">Version 2 - Add Payment & View Dues</p>


    <!-- ADD PAYMENT -->

    <div class="section">

        <h2>Add Payment</h2>

        <form method="POST">

            <label>Student ID:</label>
            <input type="text" name="student_id" required>

            <label>Student Name:</label>
            <input type="text" name="student_name" required>

            <label>Fee Type:</label>

            <select name="fee_type">

                <option>Tuition Fee</option>
                <option>Exam Fee</option>
                <option>Hostel Fee</option>
                <option>Library Fee</option>

            </select>

            <label>Amount:</label>
            <input type="number" name="amount" required>

            <button type="submit">
                Add Payment
            </button>

        </form>

        {% if message %}
            <p class="success">{{ message }}</p>
        {% endif %}

    </div>


    <!-- PAYMENT RECORDS -->

    <div class="section">

        <h2>Payment Records</h2>

        {% if payments %}

        <table>

            <tr>
                <th>Student ID</th>
                <th>Student Name</th>
                <th>Fee Type</th>
                <th>Amount Paid</th>
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

        {% else %}

        <p>No payments recorded yet.</p>

        {% endif %}

    </div>


    <!-- VIEW DUES -->

    <div class="section">

        <h2>View Dues</h2>

        <form method="GET">

            <label>Enter Student ID:</label>

            <input type="text" name="due_student_id" required>

            <button type="submit">
                Check Dues
            </button>

        </form>


        {% if due_student_id %}

            <h3>Fee Details for Student {{ due_student_id }}</h3>

            <table>

                <tr>
                    <th>Total Fee</th>
                    <th>Total Paid</th>
                    <th>Pending Fee</th>
                </tr>

                <tr>

                    <td>₹{{ total_fee }}</td>

                    <td>₹{{ total_paid }}</td>

                    <td class="due">
                        ₹{{ pending_fee }}
                    </td>

                </tr>

            </table>

        {% endif %}

    </div>

</div>

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
            "amount": int(request.form["amount"])
        }

        payments.append(payment)

        message = "Payment added successfully!"


    # View Dues
    due_student_id = request.args.get("due_student_id")

    total_paid = 0
    total_fee = TOTAL_FEE
    pending_fee = 0

    if due_student_id:

        for payment in payments:

            if payment["student_id"] == due_student_id:

                total_paid += payment["amount"]

        pending_fee = total_fee - total_paid

        if pending_fee < 0:
            pending_fee = 0


    return render_template_string(

        HTML,

        payments=payments,

        message=message,

        due_student_id=due_student_id,

        total_fee=total_fee,

        total_paid=total_paid,

        pending_fee=pending_fee

    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",port=5000,
        debug=True
    )