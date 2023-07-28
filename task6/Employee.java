public class Employee {
    private String name;
    private Date dob;
    private int baseSalary;

    public Employee(String name, Date dob, int baseSalary) {
        this.name = name;
        this.dob = dob;
        this.baseSalary = baseSalary;
    }

    public String getEmpInfo() {
        return "name - " + name + " , dob - " + dob.toString();
    }

    // Moved the salary calculation to a separate class
    public int calculateNetSalary() {
        return new SalaryCalculator().calculateNetSalary(baseSalary);
    }
}

public class SalaryCalculator {
    public int calculateNetSalary(int baseSalary) {
        int tax = (int) (baseSalary * 0.25);
        return baseSalary - tax;
    }
}