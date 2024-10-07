students = {
"Alice": [85, 78, 92],
"Bob": [79, 74, 81],
"Charlie": [91, 82, 85],
"David": [76, 85, 83],
"Eve": [88, 79, 92]
}

# 1. Calculate and print the average score for each student.

print("============================================== First ===========================================================")

for i in students.keys():
  total = sum(students[i])
  n = len(students[i])
  print(round(total/n))

# 2. Find and print the name of the student with the highest average score.

print("============================================== Second ===========================================================")

def high():
  highest_avg = 0
  top_student = ""

  for name, scores in students.items():
    avg = sum(scores) / len(scores)
    if avg > highest_avg:
        highest_avg = avg
        top_student = name
        
  return top_student
      
print(high())



# 3. Find and print the name of the student with the lowest average score.

print("============================================== Third ===========================================================")

def lowest():
  lowest_avg = 100
  not_so_top_student = ""

  for name, scores in students.items():
    avg = sum(scores) / len(scores)
    if lowest_avg > avg:
        lowest_avg = avg
        not_so_top_student = name
        
  return not_so_top_student
      
print(lowest())
        


#  Add a new student "Frank" with scores [80, 90, 85] to the dictionary and print the updated dictionary. 

print("============================================== Fourth ===========================================================")

students["Frank"] = [80, 90, 85]

print(students)