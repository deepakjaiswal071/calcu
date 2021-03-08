def switch() -> object:

    a = int(input(" enter the number " ))
    b = int(input(" enter the number " ))
    dee =['press 1. for add','press 2. for sub','press 3. for multi','press 4. for divide']
    dee= '\n'.join(dee)
    print(dee)
    option: int = int(input(" your choices "))
    def add():
     num : int = a + b
     print(num)
    def sub():
     num : int = a - b
     print(num)
    def multi():
     num : int = a * b
     print(num)
    def divide():
     num : int = a / b
     print(num)
    def defult():
     print("invalid ")
    dict = {
        1 : add,
        2 : sub,
        3 : multi,
        4 : divide
        }
    dict.get(option,defult)()

switch()
switch()
switch()
switch()
