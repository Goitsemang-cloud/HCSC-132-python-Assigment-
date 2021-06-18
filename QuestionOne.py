class Calculator:

    def __init__(self, A, B, C, D):
        self.list   = [A,B,C,D]
        

        
    def Sum_input(self):
        total = self.list
        
        return sum(total)
    
    def Average_input(self):

        average = self.Sum_input()/ len(self.list) 

        print("")
        print("")
        print("-------------------------------Sum function------------------------------")
        print("")
        print("")
        print(f"The sum for elements: {self.list} is :{self.Sum_input()}")
       

        print("")
        print("")
        print("-----------------------------Average function----------------------------")
        print("")
        print("")


        print(f"The average is : {average}") 

    def Compare_input(self):
        elements = self.list
        
        #here we are comparing elements if they're equall to each other
        # and the out put values is a boolean 

        #comparsion bewteen A and B , A and C , A and D
        element1_2 = elements[0] == elements[1]
        element1_3 = elements[0] == elements[2]
        element1_4 = elements[0] == elements[3]

        #comparsion bewteen B and C , B and D 
        element2_3 = elements[1] == elements[2]
        element2_4 = elements[1] == elements[3]

        #comparsion between C and D
        element3_4 = elements[2] == elements[3]

        print("")
        print("")
        print("---------------------------------comparsion function-----------------------")
        print("")
        print("---------------------------------Eqaulity comparion------------------------")
        print("")
        print("")
        #output for all the elements that are being compared
        print("comparsion bewteen A and B , A and C , A and D")
        print(f"Element {elements[0]} and Element {elements[1]} are equal : {element1_2}")
        print(f"Element {elements[0]} and Element {elements[2]} are equal : {element1_3}")
        print(f"Element {elements[0]} and Element {elements[3]} are equal : {element1_4}")

        print("")
        print("")

        print("comparsion bewteen B and C , B and D ")
        print(f"Element {elements[1]} and Element {elements[2]} are equal : {element2_3}")
        print(f"Element {elements[1]} and Element {elements[3]} are equal : {element2_4}")

        print("")
        print("")
        
        print("comparsion between C and D")
        print(f"Element {elements[2]} and Element {elements[3]} are equal : {element3_4}")
        


        #here we are comparing elements are greater or less than eachother 
        # and the out put values is a boolean

        #comparsion bewteen A and B , A and C , A and D 
        element1_less_2     = elements[0] < elements[1]
        element1_greater_2  = elements[0] > elements[1]
        element1_less_3     = elements[0] < elements[2]
        element1_greater_3  = elements[0] > elements[2]
        element1_less_4     = elements[0] < elements[3]
        element1_greater_4  = elements[0] > elements[3]

        #comparsion bewteen B and C , B and D 
        element2_less_3     = elements[1] < elements[2]
        element2_greater_3  = elements[1] > elements[2]
        element2_less_4     = elements[1] < elements[3]
        element2_greater_4  = elements[1] > elements[3]

        #comparsion between C and D
        element3_less_4     = elements[2] < elements[3]
        element3_greater_4  = elements[2] > elements[3]


        #output for all the elements that are being compared
        print("")
        print("")
        print("-------------------- Greater or less than comparion ----------------------")
        print("")
        print("")

        print("comparsion bewteen A and B , A and C , A and D")
        print(f"Element {elements[0]} less than      {elements[1]} : {element1_less_2}")
        print(f"Element {elements[0]} greater than   {elements[1]} : {element1_greater_2}")
        print(f"Element {elements[0]} less than      {elements[2]} : {element1_less_3}")
        print(f"Element {elements[0]} greater than   {elements[2]} : {element1_greater_3}")
        print(f"Element {elements[0]} less than      {elements[3]} : {element1_less_4}")
        print(f"Element {elements[0]} greater than   {elements[3]} : {element1_greater_4}")
        
        print("")
        print("")

        print("comparsion bewteen B and C , B and D")
        print(f"Element {elements[1]} less than      {elements[2]} : {element2_less_3}")
        print(f"Element {elements[1]} greater than   {elements[2]} : {element2_greater_3}")
        print(f"Element {elements[1]} less than      {elements[3]} : {element2_less_4}")
        print(f"Element {elements[1]} greater than   {elements[3]} : {element2_greater_4}")

        print("")
        print("")

        print("comparsion between C and D")
        print(f"Element {elements[2]} less than      {elements[3]} : {element3_less_4}")
        print(f"Element {elements[2]} greater than   {elements[3]} : {element3_greater_4}")


    def odd_OR_even(self):
        elements = self.list

        print("")
        print("")

        print("------------------Odd and Even number function------------------------")
        for element in elements:
            if element % 2 == 0:
                print(f"element {element} is an Even number ")
            else:
                print(f"element {element} is an Odd number ")

    def displayValues(self):
        elements = self.list

        print("")
        print("")

        print("------------------display Values function----------------------------")
        for element in elements:
            print(f"{element}")




A = Calculator(10,5,3,8)

A.Sum_input()
A.Average_input()
A.Compare_input()
A.odd_OR_even()
A.displayValues()