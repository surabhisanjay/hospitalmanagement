import mysql.connector

# MySQL Database Configuration
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "welcome1234",
    "database": "hptldb"
}

def get_connection():
    """Establish and return a connection to the MySQL database."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def get_all_patients():
    """Retrieve all patients using the stored procedure GetAllPatients()."""
    query = "CALL GetAllPatients()"
    
    try:
        conn = get_connection()
        if conn is None:
            return
        
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)

        # Fetch and display results
        patients = cursor.fetchall()
        for patient in patients:
            print(f"Patient ID: {patient['Patient_ID']}, "
                  f"Name: {patient['Patient_Name']}, "
                  f"Building: {patient['Building']}, "
                  f"Room: {patient['Room_Number']}")

        # Close resources
        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"SQL Error: {err}")

if __name__ == "__main__":
    get_all_patients()  # Fetching all patients using the stored procedure
