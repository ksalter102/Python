student_scores = {
    "Vader": 81,
    "Palpatine" : 78,
    "Luke" : 99,
    "Han" : 74,
    "Chewbacca" : 62,
}


student_grades = {}

for grades in student_scores:
    if student_scores[grades] < 100 and student_scores[grades] > 91:
        student_grades[grades] = "Outstanding"
    elif student_scores[grades] < 90 and student_scores[grades] > 81:
        student_grades[grades] = "Exceeds Expectations"
    elif student_scores[grades] < 80 and student_scores[grades] > 71:
        student_grades[grades] = "Acceptable"
    else:
        student_grades[grades] = "Fail"




print(student_grades)
