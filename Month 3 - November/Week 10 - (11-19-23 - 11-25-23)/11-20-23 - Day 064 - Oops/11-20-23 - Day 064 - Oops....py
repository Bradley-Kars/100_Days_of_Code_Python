class Job:
  def __init__(self, name, salary, hours_worked):
    self.name = name
    self.salary = salary
    self.hours_worked = hours_worked

class Doctor(Job):
  def __init__(self):
    super().__init__("Doctor", "$201,000", "50")
    self.experience = "7"
    self.speciality = "Paediatric Consultant"

class Teacher(Job):
  def __init__(self):
    super().__init__("Teacher", "$66,397", "40")
    self.subject = "Computer Science"

class Engineer(Job):
  def __init__(self):
    super().__init__("Engineer", "$90,000", "45")
    self.engineering_field = "Electrical Engineering"
    self.certifications = ["PE License", "Cisco Certified Network Professional"]

class Chef(Job):
  def __init__(self):
    super().__init__("Chef", "$50,000", "60")
    self.cuisine_specialty = "French Cuisine"
    self.restaurant_experience = "10 years"

class Artist(Job):
  def __init__(self):
    super().__init__("Artist", "$40,000", "30")
    self.art_medium = "Oil Painting"
    self.exhibition_experience = "5 years"

teacher_instance = Teacher()
print(f"""{teacher_instance.name}:
Subject: {teacher_instance.subject}
Salary: {teacher_instance.salary}
Expected hours: {teacher_instance.hours_worked}""")

print()

doctor_instance = Doctor()
print(f"""{doctor_instance.name}:
Subject: {doctor_instance.speciality}
Salary: {doctor_instance.salary}
Expected hours: {doctor_instance.hours_worked}
Expected experience: {doctor_instance.experience}""")

print()

engineer_instance = Engineer()
print(f"""{engineer_instance.name}:
Engineering Field: {engineer_instance.engineering_field}
Salary: {engineer_instance.salary}
Expected hours: {engineer_instance.hours_worked}
Certifications: {engineer_instance.certifications}""")

print()

chef_instance = Chef()
print(f"""{chef_instance.name}:
Cuisine Specialty: {chef_instance.cuisine_specialty}
Salary: {chef_instance.salary}
Expected hours: {chef_instance.hours_worked}
Restaurant Experience: {chef_instance.restaurant_experience}""")

print()

artist_instance = Artist()
print(f"""{artist_instance.name}:
Art Medium: {artist_instance.art_medium}
Salary: {artist_instance.salary}
Expected hours: {artist_instance.hours_worked}
Exhibition Experience: {artist_instance.exhibition_experience}""")
