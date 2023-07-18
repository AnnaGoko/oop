
import java.util.*;

public class StudentSteam implements Iterable<StudentGroup> {
    private int streamNumber;
    private List<StudentGroup> groups;

    public StudentSteam(int streamNumber, List<StudentGroup> groups) {
        this.streamNumber = streamNumber;
        this.groups = groups;
    }

    public int getStreamNumber() {
        return streamNumber;
    }

    public void setStreamNumber(int streamNumber) {
        this.streamNumber = streamNumber;
    }

    public List<StudentGroup> getGroups() {
        return groups;
    }

    public void setGroups(List<StudentGroup> groups) {
        this.groups = groups;
    }

    @Override
    public Iterator<StudentGroup> iterator() {
        return groups.iterator();
    }

    public static void main(String[] args) {
        // создание групп со студентами
        List<String> students1 = Arrays.asList("Иванов", "Петров", "Сидоров");
        List<String> students2 = Arrays.asList("Смирнов", "Иванов", "Кузнецов", "Попов");
        List<String> students3 = Arrays.asList("Лебедев", "Соколов", "Козлов");

        // создание учебных групп
        StudentGroup group1 = new StudentGroup(1, students1);
        StudentGroup group2 = new StudentGroup(2, students2);
        StudentGroup group3 = new StudentGroup(3, students3);

        // создание потока студентов и добавление групп
        StudentSteam steam = new StudentSteam(1, Arrays.asList(group1, group2, group3));

        // вывод групп на консоль
        System.out.println("Группы в потоке:");
        for (StudentGroup group : steam) {
            System.out.println("Группа #" + group.getGroupNumber() + ": " + group.getStudents());
        }

        // сортировка групп по количеству студентов и вывод на консоль
        Collections.sort(steam.getGroups());
        System.out.println("Отсортированные группы:");
        for (StudentGroup group : steam) {
            System.out.println("Группа #" + group.getGroupNumber() + ": " + group.getStudents());
        }
    }
}

class StudentGroup implements Comparable<StudentGroup> {
    private int groupNumber;
    private List<String> students;

    public StudentGroup(int groupNumber, List<String> students) {
        this.groupNumber = groupNumber;
        this.students = students;
    }

    public int getGroupNumber() {
        return groupNumber;
    }

    public void setGroupNumber(int groupNumber) {
        this.groupNumber = groupNumber;
    }

    public List<String> getStudents() {
        return students;
    }

    public void setStudents(List<String> students) {
        this.students = students;
    }

    @Override
    public int compareTo(StudentGroup other) {
        return Integer.compare(students.size(), other.getStudents().size());
    }
} 