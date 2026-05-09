# Hospital Management System

A full-stack Hospital Management System designed to manage hospital operations efficiently using a React frontend and SQL database backend. The system enables management of patients, doctors, departments, diagnoses, room assignments, and hospital records through an interactive web interface.

---

## Features

### Patient Management

* Add new patients
* Update patient details
* Delete patient records
* View patient history

### Doctor Management

* Manage doctor information
* Store specialization and department details
* Track doctor salary information

### Department Management

* Maintain hospital departments
* Assign doctors to departments

### Room Assignment

* Allocate rooms to patients
* Manage assigned room records

### Diagnosis Management

* Store diagnosis details
* Track patient treatment records

### Database Operations

* CRUD operations using SQL
* Relational database schema
* Efficient querying and data retrieval

---

# Tech Stack

## Frontend

* React.js
* JavaScript
* HTML5
* CSS3
* Axios

## Backend / Database

* SQL
* MySQL / PostgreSQL

---

# Project Structure

```bash
hospital-management-system/
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── App.js
│   │   └── index.js
│   └── package.json
│
├── database/
│   ├── schema.sql
│   ├── queries.sql
│   └── sample_data.sql
│
└── README.md
```

---

# Database Tables

The system includes the following tables:

| Table Name        | Description                     |
| ----------------- | ------------------------------- |
| patients          | Stores patient details          |
| doctors           | Stores doctor information       |
| diagnosis         | Patient diagnosis records       |
| assigned_room     | Room allocation details         |
| hptldept          | Hospital department information |
| old_salary_doctor | Historical salary records       |

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/your-username/hospital-management-system.git
cd hospital-management-system
```

---

# Frontend Setup

Navigate to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the React development server:

```bash
npm start
```

Frontend runs on:

```bash
http://localhost:3000
```

---

# Database Setup

## MySQL

1. Create a database:

```sql
CREATE DATABASE hospital_management;
```

2. Import schema:

```bash
mysql -u root -p hospital_management < schema.sql
```

3. Insert sample data:

```bash
mysql -u root -p hospital_management < sample_data.sql
```

---

# Example SQL Queries

## Retrieve All Patients

```sql
SELECT * FROM patients;
```

## Get Doctors by Department

```sql
SELECT d.name, h.department_name
FROM doctors d
JOIN hptldept h
ON d.department_id = h.department_id;
```

## Calculate Total Prescription Cost per Patient

```sql
SELECT patient_id, SUM(cost) AS total_cost
FROM diagnosis
GROUP BY patient_id;
```

---

# Screenshots

* Dashboard
* Patient Management Page
* Doctor Records Page
* Room Allocation Interface
* Diagnosis Tracking Module

---

# Future Enhancements

* Authentication and role-based access
* Appointment booking system
* Prescription management
* Billing and payment integration
* Report generation
* AI-based disease prediction modules

---

# Learning Outcomes

* React component-based frontend development
* SQL database design and normalization
* CRUD operation implementation
* Relational database management
* API integration concepts
* State management in React

---

# Contributors

* Surabhi Sanjay

---

# License

This project is developed for educational and academic purposes.
