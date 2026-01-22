

## grade_calculator.py

def calculate_grade(marks):
    """Returns grade and message based on marks"""
    if marks >= 90:
        return "A", "Excellent work! You are a star 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good job! You can do even better 😊"
    elif marks >= 60:
        return "D", "You passed! Keep practicing 💪"
    else:
        return "F", "Don't give up! Try harder next time 🌈"


def get_valid_marks():
    """Ensures marks are between 0 and 100"""
    while True:
        try:
            marks = int(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("❌ Marks must be between 0 and 100. Try again.")
        except ValueError:
            print("❌ Invalid input! Please enter a number.")


def main():
    print("🎓 STUDENT GRADE CALCULATOR 🎓")
    student_name = input("Enter student name: ").strip()

    marks = get_valid_marks()
    grade, message = calculate_grade(marks)

    print("\n📊 RESULT FOR", student_name.upper() + ":")
    print(f"Marks: {marks}/100")
    print(f"Grade: {grade}")
    print(f"Message: {message}")


# Run program
main()
