print("=========================Student Grade Calculation Program=======================")


class StudentGrade:

	def __init__ (self):
		self.name = input("Enter your Name Please? ").title()
		self.department = input("Enter your Department Please? ").upper()
		self.level = int(input("Enter your Level Please? "))

		print(self.Course())
		print(self.Mark())
		print(self.DisplayStudentData())

	def DisplayStudentData(self):

		print("="*85)
		print(f"Name: {self.name}\t\t Department: {self.department}\t\tLevel: {self.level}")
		print("="*85)
		print("")

		print("\tID|\t|  Course\t| Mark\t|  Grade| Point")

		for n in range(len(self.course)):
			print(f"\t{n} |\t|  {self.course[n]}\t| {self.mark[n]}\t|   {self.ShowGrade()[n]}\t|  {self.Point()[n]}")

		return ""

	def Course(self):
		self.courseNum = int(input("How many course you are offering? "))

		self.course = [input(f"Enter Course {c} Title Please? ").upper() for c in range(1,self.courseNum+1)]

		return ""

	def Grade(self,score):

		if 100 >=  score >= 70: return "A"

		elif 70 > score >= 60: return "B"

		elif 60 >  score >= 50: return "C"

		elif 50 > score  >= 40: return "D"

		elif 40 > score >= 0: return "F"

	def Mark(self):
		self.mark = [int(input(f"What do you score in {self.course[c]}? ")) for c in range(self.courseNum)]
		return ""

	def ShowGrade(self):
		self.grade = [self.Grade(m) for m in self.mark]
		return self.grade

	def Point(self):
		p = {"A":5,"B":4,"C":3,"D":2,"F":0}
		self.point = [p[self.Grade(m)] for m in self.mark]
		return self.point


if __name__ == "__main__":
	obj = StudentGrade()
	