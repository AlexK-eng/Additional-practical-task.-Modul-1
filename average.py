# This is Additional practical task.

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3],[4, 5, 5, 2],
          [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
# The first option is boring and tedious.
dic_students = {students[0] : sum(grades[0], 0) / len(grades[0]),
                students[1] : sum(grades[1], 0) / len(grades[1]),
                students[2] : sum(grades[2], 0) / len(grades[2]),
                students[3] : sum(grades[3], 0) / len(grades[3]),
                students[4] : sum(grades[4], 0) / len(grades[4])
                }
print(dic_students)
# The second option is convenient with a cycle
dict_students = {}
for i in range(len(students)):
    dict_students.update({students[i] : sum(grades[i], 0) / len(grades[i])})
print(dict_students)