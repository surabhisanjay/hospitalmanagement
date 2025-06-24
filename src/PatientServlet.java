
import java.io.IOException;
import java.io.PrintWriter;
import java.sql.*;
import java.util.ArrayList;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import com.google.gson.Gson;

@WebServlet("/PatientServlet")
public class PatientServlet extends HttpServlet {
    private static final String URL = "jdbc:mysql://localhost:3306/hptldb";
    private static final String USER = "root";
    private static final String PASSWORD = "welcome1234";

    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("application/json");
        PrintWriter out = response.getWriter();

        ArrayList<Patient> patientList = new ArrayList<>();

        try (Connection conn = DriverManager.getConnection(URL, USER, PASSWORD);
             CallableStatement stmt = conn.prepareCall("{CALL GetAllPatients()}")) {

            ResultSet rs = stmt.executeQuery();
            while (rs.next()) {
                patientList.add(new Patient(
                    rs.getInt("Patient_ID"),
                    rs.getString("Patient_Name"),
                    rs.getString("Building"),
                    rs.getInt("Room_Number")
                ));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        Gson gson = new Gson();
        out.print(gson.toJson(patientList));
        out.flush();
    }
}

class Patient {
    int id;
    String name;
    String building;
    int room;

    public Patient(int id, String name, String building, int room) {
        this.id = id;
        this.name = name;
        this.building = building;
        this.room = room;
    }
}
