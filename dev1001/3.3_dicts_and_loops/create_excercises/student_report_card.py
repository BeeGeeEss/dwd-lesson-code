student_data = {
    "Wayne Campbell": {"Math": 70, "Science": 85, "Literature": 92},
    "Garth Algar": {"Math": 90, "Science": 75, "Music": 95},
    "Benjamin Kane": {"Math": 80, "English": 80, "Business": 60}
    }


for student, subjects in student_data.items():
    print(f"Report for: {student}")

    for subject, grade in subjects.items():
        print(f"  {subject}: {grade}")

    grades = subjects.values()
    average = sum(grades) / len(grades)
    print(f"  Average Grade: {average:.2f}")

    highest_subject = max(subjects, key=subjects.get)
    lowest_subject = min(subjects, key=subjects.get)

    print(f"  Highest Scoring Subject: {highest_subject} ({subjects[highest_subject]})")
    print(f"  Lowest Scoring Subject: {lowest_subject} ({subjects[lowest_subject]})")