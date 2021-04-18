class Student:
  gender = "Female"
  def __init__(self,scores=[]):
    self.scores= scores

  def avg(self):
     return round(sum(self.scores)/ len(self.scores))

  @staticmethod
  def notice():
       return "Exams next week!"

  @classmethod
  def what_is_gender(cls):
    return " I am{cls.gender}"

print(Student.what_is_gender())
print(Student.gender)