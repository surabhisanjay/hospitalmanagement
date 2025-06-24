from flask import Flask, request, jsonify, CORS
import mysql.connector

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Requests for React

# MySQL Configuration
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "welcome1234",
    "database": "hptldb"
}

def get_connection():
    """Establish a connection to MySQL database."""
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except mysql.connector.Error as err:
        print(f"Database Connection Error: {err}")
        return None

@app.route("/patients", methods=["GET"])
def get_patients():
    """Fetch all patients."""
    conn = get_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("CALL GetAllPatients()")  # Stored procedure call
        patients = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(patients)
    return jsonify([]), 500

@app.route("/add_patient", methods=["POST"])
def add_patient():
    """Insert new patient into the database."""
    data = request.json
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        query = "INSERT INTO patients (Patient_Name, Building, Room_Number) VALUES (%s, %s, %s)"
        cursor.execute(query, (data["name"], data["building"], data["room"]))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Patient added"}), 201
    return jsonify({"error": "Database error"}), 500

@app.route("/delete_patient/<int:patient_id>", methods=["DELETE"])
def delete_patient(patient_id):
    """Delete patient from the database."""
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        query = "DELETE FROM patients WHERE Patient_ID = %s"
        cursor.execute(query, (patient_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Patient deleted"}), 200
    return jsonify({"error": "Database error"}), 500

if __name__ == "__main__":
    app.run(debug=True)
