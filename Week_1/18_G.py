"""Grades"""
'''Rules:
1. Max marks is 100 in each subject
2. Pass mark is 35
'''
marks_1 = int(input("Marks 1 (out of 100): "))
marks_2 = int(input("Marks 2 (out of 100): "))
marks_3 = int(input("Marks 3 (out of 100): "))

total = marks_1 + marks_2 + marks_3
avg = total / (3 * 100)
percent = avg * 100
is_passed = True

if marks_1 < 35:
    is_passed = False
    print(f"{marks_1} marks_1 failed")
if marks_2 < 35:
    is_passed = False
    print(f"{marks_2} marks_2 failed")
if marks_3 < 35:
    is_passed = False
    print(f"{marks_3} marks_3 failed")

print("Report")
print("Total = " + str(total))
print("Percent = " + str(round(percent,2)))

if is_passed:
    print("Passed")
else:
    print("Failed")

'''
Output:
Marks 1 (out of 100): 44
Marks 2 (out of 100): 32
Marks 3 (out of 100): 90
32 marks_2 failed
Report
Total = 166
Percent = 55.33
Failed
'''