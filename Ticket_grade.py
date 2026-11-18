age = int(input("Enter your age: "))
student = input("Are you a student? (yes/no): ")

if age < 0:
    print("Invalid age")

elif age <= 12:
    print("Child ticket price: Rs. 200")

elif age >= 60:
    print("Senior ticket price: Rs. 250")

elif student == "yes":
    print("Student ticket price: Rs. 300")

else:
    print("Adult ticket price: Rs.500")
    
print("\n--- Grade Calculater ---")
score = int(input("Enter your score: "))

if score < 0 or score > 100:
    print("Invalid score")

elif score >= 90:
    print("Grade: A")

elif score >= 80:
    print("Grade: B")

elif score >= 70:
    print("Grade: C")

elif score >= 60:
    print("Grade: D")

else:
    print("Grade: F")   