cal = '''
  _____________________
|  _________________  |
| | Emma Cal     0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

'''
print(cal)

def Calculator():

    def add(x,y):
        return x + y

    def sub(x,y):
        return x - y

    def mul(x,y):
        return x*y

    def div(x,y):
        return x / y

    print("List of Operations: + - * /")

    num_1 = float (input("Enter the first number: "))
    num_2 = float( input("Enter the second number: "))
    operation = (input("Enter the operation to perfrom: "))

    result = 0

    if operation == "+":
        result = add(num_1, num_2)
    elif operation == "-":
        result = sub(num_1, num_2)
    elif operation == "*":
        result = mul(num_1, num_2)
    elif operation == "/":
        result = div(num_1, num_2)
    elif operation == "/" and num_2 == 0:
        print("Cannot Divide By 0")
    else:
        print("An Invalid Input.")
        
    print("Result:" ,round(result, 3))   

Calculator()
    
thanks =    '''
 _   _                 _                       
| | | |               | |                  
| |_| |__   __ _ _ __ | | _____ 
| __| '_ \ / _` | '_ \| |/ / __|
| |_| | | | (_| | | | |   <\__ \ 
 \__|_| |_|\__,_|_| |_|_|\_\___/
                                                
    '''                                      
print(thanks)
