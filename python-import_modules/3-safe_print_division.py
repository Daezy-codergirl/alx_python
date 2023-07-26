def safe_print_division(a, b):

 try:
        result = a / b
        print("Inside result: {}".format(result))

 except ZeroDivisionError:
        result = None
 finally:
        print("Inside result: {}".format(result))
        return result

      




    
    
