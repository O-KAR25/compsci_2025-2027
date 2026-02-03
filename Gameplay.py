# Implement a dictionary by typing dictionary name, using curly braces {}, and then adding KEYS and VALUES separated by a colon (:).
# Each key-value pair is separated by a comma.
# Example: my_dict = {"key1": "value1", "key2": "value2"}# Access values by referencing their keys inside square brackets [].
# Example: value = my_dict["key1"]
# Creating a dictionary
# {} for dictionaries, [] for lists

student_grades = {
    student_list = ["Myesha", "Julia", "Alicja", "Gwanho", "Oskar"]

    subject_list = ["Math", "English", "Science"]
    
    grades_list =  [76, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67]
}


grade_index = 0

for student in student_list:
    student_grades[student] = {}
    for subject in subject_list:
        student_grades[student][subject] = grades_list[grade_index]
        grade_index += 1
