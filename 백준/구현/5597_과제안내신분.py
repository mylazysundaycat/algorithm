
student = set(range(1,31))


for _ in range(28):
    student.remove(int(input()))

student = sorted(student,reverse=False)
print(student[0])
print(student[1])