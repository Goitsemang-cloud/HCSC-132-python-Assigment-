class admissions:

    def __init__(self):
        self.Applied_statistics = []
        self.Information_system = []
        self.Computer_science   = []
        self.Guidance_Studies   = []
        self.Medicion           = []
        self.Law                = []
        self.Media              = []


    def input_details(self,Name, Point, ContactNumber, Course,faculty):
        Student_info =  []

        def addInfo():
            Student_info.append(Name)
            Student_info.append(Point)
            Student_info.append(ContactNumber)
            Student_info.append(Course)

        if faculty == "S":
                
            if Course == "AS":
                if Point >= 5:
                    addInfo()

                    self.Applied_statistics.append(Student_info)
                elif Point < 5 or Point < 9:
                    print("")
                    print("Your points are low, Recommend bridging")

            elif Course == "CS":
                if Point >= 9:  
                    addInfo()   

                    self.Computer_science.append(Student_info)
                elif Point < 5 or Point < 9:
                    print("")
                    print("Your points are low, Recommend bridging")
        
            
            elif Course == "GS":
                if Point >= 12:
                    addInfo()

                    self.Guidance_Studies.append(Student_info)
                elif Point < 5 or Point < 11:
                    print("") 
                    print("Your points are low, Recommend bridging")
                

            elif Course == "MED":
                if Point >= 12:
                    addInfo()

                    self.Medicion.append(Student_info)
                elif Point < 5 or Point < 11:
                    print("") 
                    print("Your points are low, Recommend bridging")

        elif faculty == 'C':
            if Course == "IS":
                if Point >= 9:
                    addInfo()

                    self.Information_system.append(Student_info)
                elif Point < 9:
                    print("")
                    print("rejected for this course, Your points are low, ")

        elif faculty == "A":
            if Course == "MEDIA":
                if Point >= 5:
                    addInfo()

                    self.Media.append(Student_info)
                elif Point < 5 or Point < 9:
                    print("")
                    print("rejected for this course, Your points are low, ")

            elif Course == "LAW":
                if Point >= 10:
                    addInfo()

                    self.Law.append(Student_info)
                elif Point < 5 or Point < 9:
                    print("")
                    print("rejected for this course, Your points are low, ")
            else:
                print("The course you picked doesn't exist!!")   


    def Output_enrolled_Count(self):

        print(f"number of students for Applied statistics : {len(self.Applied_statistics)}")
        print(f"number of students for Information system : {len(self.Information_system)}")
        print(f"number of students for Computer science   : {len(self.Computer_science)}")
        print(f"number of students for Guidance Studies   : {len(self.Guidance_Studies)}")
        print(f"number of students for Medicion           : {len(self.Medicion)}")
        print(f"number of students for Law                : {len(self.Law)}")
        print(f"number of students for Media              : {len(self.Media)}")


    def Menu(self):
        print("")
        print("please choose one of the following Options below")
        print("[A] to input student data")
        print("[B] to View Enrolled student ")
        print("[C] to Quit program ")

        print("Enter option : ",end='')
        valuekeyed = input().upper()

        print("")
        if valuekeyed == 'A':

            print("Enter name: ", end='')
            name    = str(input())

            print("Enter obtain point: ", end='')
            point   = int(input())

            print("Enter contact number: ", end='')
            number  = float(input())

            print("")
            print("--------faculties available---------")
            print("[S] Sciences\n[C] Commercial\n[A] Arts")

            print("")
            print("Enter faculty you wish View : ", end=' ')
            faculty  = input().upper()


            if faculty == 'S':
                print("")
                print("--------Courses available---------")
                print("Applied Statistics = [AS]\nComputer science = [CS]\nGuidance Studies = [GS]\nMedicion = [MED]")

                print("")
                print("Enter course you wish to enroll: ", end=' ')
                course  = input().upper()

                self.input_details(name, int(point), number, course, faculty)

            elif faculty == 'C':
                print("")
                print("--------Courses available---------")
                print("Information system = [IS]")

                print("")
                print("Enter course you wish to enroll: ", end=' ')
                course  = input().upper()

                self.input_details(name, int(point), number, course, faculty)

            elif faculty == "A":
                print("")
                print("--------Courses available---------")
                print("Law = [LAW]\nMedia = [MEDIA]")

                print("")
                print("Enter course you wish to enroll: ", end=' ')
                course  = input().upper()

                self.input_details(name, int(point), number, course, faculty)

        elif  valuekeyed == 'B':
            self.Output_enrolled_Count()
        elif  valuekeyed == 'C':
            exit()



if __name__ == "__main__":
    A = admissions()

    print("Would you like to start the program [Y/N]: ",end='')
    B = input().upper()
    while B == 'Y':
        A.Menu()