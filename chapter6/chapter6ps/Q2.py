marks1 = int(input("Enter marks of subject 1: "))
marks2 = int(input("Enter marks of subject 2: "))
marks3 = int(input("Enter marks of subject 3: "))

average_marks = (marks1 + marks2 + marks3) / 300 * 100
print(f"Average Marks: {average_marks:.2f}%")

# Check each subject
failed_subjects = []
if marks1 < 33:
    failed_subjects.append("Subject 1")
if marks2 < 33:
    failed_subjects.append("Subject 2")
if marks3 < 33:
    failed_subjects.append("Subject 3")

# Final result
if (average_marks >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
    print("Student has passed.")
else:
    print("Student has failed.")
    if failed_subjects:
        print("Failed in:", ", ".join(failed_subjects))