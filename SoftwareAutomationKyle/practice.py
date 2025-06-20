# def find_largest(x, y, z):
#     return max(x, y, z)
#
# test_cases = [
#     (1, 150, 150),
#     (2, 150, 150),
#     (150, 150, 150),
#     (299, 150, 150),
#     (300, 150, 150),
#     (150, 1, 150),
#     (150, 2, 150),
#     (150, 299, 150),
#     (150, 300, 150),
#     (150, 150, 1),
#     (150, 150, 2),
#     (150, 150, 299 ),
#     (150, 150, 300)
# ]
#
# print("Test Case | x y z | Expected output | Actual Output | MAtch")
# print("-----------------------------------------------------------")
#
# for i, (x, y, z) in enumerate (test_cases, start=1):
#     excepted = max (x, y, z)
#     actual = find_largest(x, y, z)
#     match = "✅" if actual == excepted else "X"
#     print(f"{i<9} | {x:3} {y:3} {z:3} | {excepted:8} | {actual:6} | {match}")
# from numpy.ma.extras import average
# from scipy.cluster.hierarchy import average


# def final_grade(mark1, mark2, mark3):
#
#     if 75 <= average <= 100:
#         return "First Division with distinction"
#     elif 60 <= average < 75:
#         return "First division"
#     elif  50 <= average < 60:
#         return "Second division"
#     elif 40 <= average < 50:
#         return "Third deivision"
#     else:
#         return "Fail"
#
# grade_case = [
#     (0,0,0),
#     (39,39,39),
#     (40, 40, 40),
#     (49,49,49),
#     (50,50,50),
#     (59, 59, 59),
#     (60, 60, 60),
#     (74, 74, 74),
#     (75,75,75),
#     (100,100,100),
#     (39, 40, 40),
#     (49, 49, 50),
#     (74, 74, 75)
# ]
#
# print ("Test Case | Final Marks                           | Average | Expected grade")
# print("-----------------------------------------------------------------------------")
#
# for i, (m1, m2, m3) in enumerate (grade_case, start=1):
#     average = (m1 + m2 + m3 ) / 3
#     grade = final_grade(m1, m2, m3)
#     print(f"{i:9} | {m1:3}{m2:3}{m3:3} | {average:7.2f} | {grade}")


# def is_valid_triangle(a, b, c):
#     return (a + b > c) and (a + c > b) and (b + c > a)
#
#
# def classify_triangle(a, b, c):
#     if not is_valid_triangle(a, b, c):
#         return "Invalid Triangle"
#
#
#     sides = sorted([a, b, c])
#     x, y, z = sides  # x is a y is b and z is z
#     x2, y2, z2 = x ** 2, y ** 2, z ** 2
#
#     if z2 == x2 + y2:
#         return "Right
#         angled triangle"
#     elif z2 > x2 + y2:
#         return "Obtuse Triangle"
#     else:
#         return "Acute triangle"
#
#
# try:
#
#     a = int(input("Enter side a (1-100): "))
#     b = int(input("Enter side b (1-100): "))
#     c = int(input("Enter side c (1-100): "))
#
#     if 1 <= a <= 100 and 1 <= b <= 100 and 1 <= c <= 100:
#         result = classify_triangle(a, b, c)
#         print(f"\nResult: {result}")
#     else:
#         print("\n Please enter values between 1 and 100.")
# except ValueError:
#     print("\n Invalid input. Please enter integer values.")
#
# triangle_case = [
#     (1, 1, 1),
#     (100, 100, 100),
#     (3, 4, 5),
#     (5, 12, 13),
#     (6, 8, 10),
#     (2, 2, 3),
#     (10, 10, 19),
#     (10, 10, 20),
#     (5, 5, 8),
#     (5, 5, 9),
#     (99, 100, 1),
#     (1, 100, 100)
# ]
#
# print("Test Case |          a  b  c | Classification")
# print("------------------------------------------------")
#
# for i, (a,b,c) in enumerate (triangle_case, start=1):
#     result = classify_triangle(a,b,c)
#     print(f"{i:9} | {a:3}{b:3}{c:3} | {result}")

# def get_marks():
#     global counter
#     while True:
#         try:
#             mark = int(input(f"Enter mark {counter} (1-100): "))
#             if 1 <= mark <= 100:
#                 return mark
#             else:
#                 print("❌ Please enter a value between 1 and 100.")
#         except ValueError:
#             print("❌ Invalid input. Please enter a number.")
#
# counter=1
# m1=get_marks()
# m2=get_marks()
# m3=get_marks()
#
# avg = int(m1+m2+m3) / 3
#
# if avg >= 75:
#     print("First Division with distinction")
# elif avg >= 60:
#     print("First div")
# elif avg >= 50:
#     print("Seoncd div")
# elif avg >= 40:
#     print("third")
# else:
#     print("fail")


# set1 = {10,20,30,40}
# set2 = {50, 20, "10", 60}
# set3 = set1.union(set2)
# print(set3)

# sampleSet = {"Yellow", "Orange", "Black"}
# sampleSet.add("Blue")
# sampleSet.add("Orange")
# print(sampleSet)

# sampleDict = dict([
# ('first', 1),
# ('second', 2),
# ('third', 3)
# ])
# print(sampleDict)

# import unittest
#
#
# class TestSum(unittest.TestCase):
#
#     def test_sum(self):
#         self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")
#
#     def test_sum_tuple(self):
#         self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
#
# if __name__ == '__main__':
#     unittest.main()

aTuple = (10, 20, 30, 40, 50, 60, 70, 80)
print(aTuple[2:5], aTuple[:4], aTuple[3:])