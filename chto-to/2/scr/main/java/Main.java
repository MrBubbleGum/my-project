import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Random;

/**
 * Класс, представляющий студента.
 */
class Student {
    private String name;
    private boolean isBudget;
    private double averageGrade;
    private Date examDate;

    public Student(String name, boolean isBudget, double averageGrade, Date examDate) {
        this.name = name;
        this.isBudget = isBudget;
        this.averageGrade = averageGrade;
        this.examDate = examDate;
    }

    public String getName() { return name; }
    public boolean isBudget() { return isBudget; }
    public double getAverageGrade() { return averageGrade; }
    public Date getExamDate() { return examDate; }

    public boolean isExamOnTime(Session session) {
        return session.isOnTime(this.examDate);
    }

    public Scholarship.ScholarshipType calculateScholarship() {
        return Scholarship.calculateScholarship(this.averageGrade);
    }

    @Override
    public String toString() {
        return "Student{name='" + name + "', isBudget=" + isBudget + ", averageGrade=" + averageGrade + ", examDate=" + examDate + "}"; 
    }
}

/**
 * Класс для расчета стипендии.
 */
class Scholarship {
    public enum ScholarshipType {
        NONE, MINIMAL, INCREASED_25, INCREASED_50
    }

    public static ScholarshipType calculateScholarship(double averageGrade) {
        if (averageGrade < 5) {
            return ScholarshipType.NONE;
        } else if (averageGrade >= 5 && averageGrade < 6) {
            return ScholarshipType.MINIMAL;
        } else if (averageGrade >= 6 && averageGrade < 8) {
            return ScholarshipType.INCREASED_25;
        } else if (averageGrade >= 8 && averageGrade <= 10) {
            return ScholarshipType.INCREASED_50;
        }
        return ScholarshipType.NONE;
    }
}

/**
 * Класс для управления экзаменационной сессией.
 */
class Session {
    private Date examDeadline;

    public Session(Date examDeadline) {
        this.examDeadline = examDeadline;
    }

    public boolean isOnTime(Date examDate) {
        return !examDate.after(examDeadline);
    }

    public Date getExamDeadline() {
        return examDeadline;
    }
}

/**
 * Класс для управления университетом.
 */
class University {
    private List<Student> students;

    public University() {
        students = new ArrayList<>();
    }

    public void addStudent(Student student) {
        students.add(student);
    }

    public void printStudentsOnPaidBasis() {
        for (Student student : students) {
            if (!student.isBudget()) {
                System.out.println(student);
            }
        }
    }

    public double calculateAverageGrade() {
        double sum = 0;
        for (Student student : students) {
            sum += student.getAverageGrade();
        }
        return sum / students.size();
    }

    public void printStudentsWithIncreasedScholarship() {
        for (Student student : students) {
            if (student.calculateScholarship() == Scholarship.ScholarshipType.INCREASED_25) {
                System.out.println(student);
            }
        }
    }

    public List<Student> getStudents() {
        return students;
    }
}

/**
 * Основной класс для демонстрации работы стипендиальной системы.
 */
public class Main {
    public static void main(String[] args) {
        try {
            // Создание формата даты
            SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
            
            // Дата крайнего срока сдачи экзаменов
            Date examDeadline = sdf.parse("2024-06-01");

            // Создание сессии
            Session session = new Session(examDeadline);

            // Создание университета
            University university = new University();

            // Генерация 10 случайных студентов
            Random random = new Random();
            String[] names = {"Иванов И.И.", "Петров П.П.", "Сидоров С.С.", "Кузнецов К.К.", "Попов А.А.", 
                              "Васильев В.В.", "Григорьев Г.Г.", "Морозов М.М.", "Тимофеев Т.Т.", "Чернов Ч.Ч."};

            for (int i = 0; i < 10; i++) {
                // Случайный выбор данных
                String name = names[i];
                boolean isBudget = random.nextBoolean();  // Случайно выбираем, бюджет или платная основа
                double averageGrade = 3 + (7 * random.nextDouble());  // Генерация среднего балла от 3.0 до 10.0

                // Случайная дата экзамена в пределах 2024 года
                int year = 2024;
                int month = random.nextInt(12);  // Месяц от 0 до 11
                int day = random.nextInt(28) + 1;  // День от 1 до 28 (для простоты, не учитываем длину месяцев)
                String dateStr = String.format("%d-%02d-%02d", year, month + 1, day);
                Date examDate = sdf.parse(dateStr);

                // Добавление студента в университет
                university.addStudent(new Student(name, isBudget, averageGrade, examDate));
            }

            // Вывод студентов, обучающихся на платной основе
            System.out.println("Студенты на платной основе:");
            university.printStudentsOnPaidBasis();

            // Вывод студентов с увеличенной стипендией на 25%
            System.out.println("\nСтуденты с увеличенной стипендией на 25%:");
            university.printStudentsWithIncreasedScholarship();

            // Вывод студентов, сдавших экзамен вовремя или с опозданием
            System.out.println("\nСтуденты, сдавшие экзамен вовремя:");
            for (Student student : university.getStudents()) {
                if (student.isExamOnTime(session)) {
                    System.out.println(student.getName() + " сдал экзамен вовремя.");
                } else {
                    System.out.println(student.getName() + " сдал экзамен с опозданием.");
                }
            }

            // Вывод среднего балла по всем студентам
            System.out.println("\nСредний балл по всем студентам: " + university.calculateAverageGrade());

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
