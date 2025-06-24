import java.sql.*;
import java.util.ArrayList;

public class DataBaseManager {
    private static final String URL = "jdbc:mysql://localhost:3306/hptldb";
    private static final String USER = "root";
    private static final String PASSWORD = "welcome1234";

    public static Connection getConnection() throws SQLException {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver"); // Load MySQL Driver
        } catch (ClassNotFoundException e) {
            System.out.println("MySQL JDBC Driver not found. Ensure it's added to the classpath.");
            e.printStackTrace();
        }
        return DriverManager.getConnection(URL, USER, PASSWORD);
    }

    // Retrieve all patients using the stored procedure
    public static void getAllPatients() {
        String query = "{CALL GetAllPatients()}";  // Call the stored procedure

        try (Connection conn = getConnection(); CallableStatement stmt = conn.prepareCall(query)) {
            ResultSet rs = stmt.executeQuery();
            while (rs.next()) {
                System.out.println("Patient ID: " + rs.getInt("Patient_ID") + 
                                   ", Name: " + rs.getString("Patient_Name") + 
                                   ", Building: " + rs.getString("Building") + 
                                   ", Room: " + rs.getInt("Room_Number"));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
    




    public static void main(String[] args) {
        getAllPatients(); // Fetching all patients using the stored procedure
    }
}
