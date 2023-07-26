def safe_print_division(a, b):
    return a / b 
a = 12
b = 2

result = safe_print_division(a, b)




print("{:d} / {:d} = {}".format(a, b, result))

   
if __name__ == "__main__":  

 a = 12
 b = 0
 
 try:
        print("Inside result: {}".format(result))

 except ZeroDivisionError:
        result = None
 finally:
        print("Inside result: {}".format(result))

      




    
    
