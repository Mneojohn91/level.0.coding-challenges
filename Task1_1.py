import pytest
count = 0
for a in range(0,1000):
    if a %3 == 0 or a %5 ==0:
        count += a
print(count)
