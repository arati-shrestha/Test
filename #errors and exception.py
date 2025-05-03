# #errors and exception
# x = -5
# if x < 0:
#     raise Exception("number should be positive")
# if 100 > x > 80:
#     raise Exception("why are you not dead yet?")
# if x > 100:
#     raise Exception("dead people can't enter anything, sorry.")
    


# assert(x>=0), 'x is not positive'

try:
    a = 5/0
except ZeroDivisionError as e:
    print(e)

finally:
    print("cleaning up...")

    
class ValueTooHighError(Exception):
    pass