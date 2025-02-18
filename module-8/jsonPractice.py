import json

# load student data into a python class list
def loadStudents(filename):
    with open(filename) as f:
        return json.load(f)

# print student list
def printStudentList(studentsData):
    for studentData in studentsData:
        print(f"{studentData["L_Name"]}, {studentData['F_Name']} : ID = {studentData['Student_ID']} , Email = {studentData['Email']}")

# main function
def main():
    studentsData = loadStudents("student.json")

    print("This is original student list.")
    printStudentList(studentsData)

    # append student
    studentsData.append({
    "F_Name": "Emily",
    "L_Name": "Smith",
    "Student_ID": 12345,
    "Email": "emilysmith@gmail.com"
  })
    
    print("This is updated student list.")
    printStudentList(studentsData)

    #update json file
    with open("student.json", "w") as f:
        json.dump(studentsData, f, indent=4)
    print("Student JSON file has been updated.")

if __name__ == "__main__":
    main()