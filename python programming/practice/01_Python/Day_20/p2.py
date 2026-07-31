# Try - Except block

# let,s create a file 
with open('file2.txt','w') as f :
    f.write('Hello World')

# Try Catch Demo
try:
    with open('file2.txt','r') as f:
        print(f.read())
except:
    print('sorry file not found') 

# catching specific exception
try:
    f = open('file2.txt','r')
    print(f.read())
    # print(m)
    print(5/2)
    l = [1,2,3]
    l[100]
except FileNotFoundError:
    print('sorry file not found')
except NameError:
    print('variable is not defined')
except ZeroDivisionError:
    print('cannot divide by zero')
except Exception as e:
    print('e.with_traceback')
except Exception as e:
    print(e)

# ELSE
try :
    f = open('file2.txt','r')
except FileNotFoundError:
    print('sorry file not found')
except Exception:
    print('some error occurred')
else:
    print(f.read())
finally:
    print('this will always execute')