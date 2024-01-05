# error handling
#
# types of errors
# compile errors such as wrong spelling or missing : in loops or indentation
# logical errors such as 2+2=5
# runtime errors such as divide by zero

try:
    a = int(input('enter a '))
    b = int(input('enter b '))
    print('result of a/b = ', a / b)
    print('Resource open')
    n = int(input('Enter value of n: '))

except ZeroDivisionError as e:
    print('You cannot divide by Zero\n', e)

except ValueError as e:
    print('please input an integer\n', e)

except Exception as e:
    print('Something went wrong', e)

finally:
    print('resource closed')
