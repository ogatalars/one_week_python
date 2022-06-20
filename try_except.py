# try:<code that could generate error>
# except: <code that runs if error occurs>

# We can use the try and except keywords to handle exceptions. If an exception is raised in the try block the excpet block will run. 

try:
   num = int(input('enter a number: '))
except ValueError: 
    print('Except block is running')
    num = 7
except:
    print('EOFEerror is running')    
print(f"you entered {num}")    