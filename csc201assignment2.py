
#NOTE: I USED PYTHON 3.9 , if you run this program on python 2 version.
# it will throw an error because it does not support f string format
# and also python 3 version does not use raw input 

print("========================= Student Grade Calculation Program=======================")

#<============== student name ========================> 
name = input("Enter your Name Please? ").title()
#<================== student department ===============>
department = input("Enter your Department Please? ").upper()
#============== student level =========================>
level = int(input("Enter your Level Please? "))

# <=============== number of course student offer in that sememster =============>
courseNum = int(input("How many course you are offering? "))

# List comprehension: to stored all the course student offer in variable called course ======>
course = [input(f"Enter Course {c} Title Please? ").upper() for c in range(1,courseNum+1)]

#<================= student to enter score for each courses ================> 
mark = [int(input(f"What do you score in {course[c]}? ")) for c in range(courseNum)]


#================= Function to compute student score =====================>
def Grade(score):
	if 100 >=  score >= 70: return "A"

	elif 70 > score >= 60: return "B"

	elif 60 >  score >= 50: return "C"

	elif 50 > score  >= 40: return "D"

	elif 40 > score >= 0: return "F"

#=================== Function to show the student grade =================>
def ShowGrade():
	grade = [Grade(m) for m in mark]
	return grade

#================ Function to compute point for student score =================>
def Point():
	p = {"A":5,"B":4,"C":3,"D":2,"F":0}
	point = [p[Grade(m)] for m in mark]
	return point


#=============== Function to show student information ==================>
def DisplayStudentData():

	print("="*85)
	print("Name: {}\t\t Department: {}\t\tLevel: {}".format(name,department,level))
	print("="*85)
	print("")

	print("\tID|\t|  Course\t| Mark\t|  Grade| Point")

	for n in range(len(course)):
		print(f"\t{1+n} |\t|  {course[n]}\t| {mark[n]}\t|   {ShowGrade()[n]}\t|  {Point()[n]}")
			
	return ""

#========= calling  the function here ====================>
print(DisplayStudentData())
	