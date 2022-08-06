from random import seed
from random import randint
import time
a = time.time()
seed(1)
for i in range(10):
    value = randint(1, 10)
a=int(input('1-10 hurtelh too oruul '))
if a > value:
    b = a - value
    print('Sanamsargui toonoos',b,'-r ih baina')
elif a < value:
    b = value - a
    print('Sanamsargui toonoos ',b,'-r baga baina')
elif a == value:
    print('Sanamsargui toog taalaa')
b = time.time()
t = b - a
print('Ajillasan hugatsaa -', t)
