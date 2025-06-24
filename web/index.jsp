<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <title>Patient List</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid black; padding: 10px; text-align: left; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>

    <h2>Hospital Patient List</h2>

    <button onclick="fetchPatients()">Load Patients</button>

    <table id="patientTable">
        <thead>
            <tr>
                <th>Patient ID</th>
                <th>Name</th>
                <th>Building</th>
                <th>Room Number</th>
            </tr>
        </thead>
        <tbody>
        </tbody>
    </table>

    <script>
        function fetchPatients() {
            fetch('PatientServlet')
                .then(response => response.json())
                .then(data => {
                    let tableBody = document.querySelector("#patientTable tbody");
                    tableBody.innerHTML = "";
                    data.forEach(patient => {
                        let row = `<tr>
                            <td>${patient.id}</td>
                            <td>${patient.name}</td>
                            <td>${patient.building}</td>
                            <td>${patient.room}</td>
                        </tr>`;
                        tableBody.innerHTML += row;
                    });
                })
                .catch(error => console.error('Error:', error));
        }
    </script>

</body>
</html>
