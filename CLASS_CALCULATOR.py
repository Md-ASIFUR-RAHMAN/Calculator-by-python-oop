class calculator:
    def __init__(self,value1:int):
        self.value1 = value1


    def get_sum(self,value2:int):
        value = self.value1 + value2
        return value
    def get_sub(self,value3:int):
        valuee = self.value1 - value3
        return valuee
    def get_multi(self,value4:int):
        v = self.value1 * value4
        return v
    def get_divide(self,value5:int):
        val = self.value1 / value5
        return val

while True :

    print("1.sum")
    print("2.sub")
    print("3.multi")
    print("4.Divide")
    print("5.Break")
    n = int(input("Enter Number  :"))
    if n == 1:
        user_input = int(input("Enter 1st value  :"))
        user_input1 = int(input("Enter 2nd value  :"))

        C_calculator = calculator(user_input)
        print(C_calculator.get_sum(user_input1))
    if n == 2:
        user_input = int(input("Enter 1st value  :"))
        user_input1 = int(input("Enter 2nd value  :"))

        C_calculator = calculator(user_input)

        print(C_calculator.get_sub(user_input1))

    if n == 3:
        user_input = int(input("Enter 1st value  :"))
        user_input1 = int(input("Enter 2nd value  :"))

        C_calculator = calculator(user_input)

        print(C_calculator.get_multi(user_input1))
    if n == 4:
        user_input = int(input("Enter 1st value  :"))
        user_input1 = int(input("Enter 2nd value  :"))

        C_calculator = calculator(user_input)

        print(C_calculator.get_divide(user_input1))
    if n== 5:
        break
