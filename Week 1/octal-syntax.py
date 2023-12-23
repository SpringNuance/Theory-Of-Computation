from sys import stdin

q=0
for c in stdin.readline().strip("\n"):
    if q==0:
        if c=="+" or c=="-": q=1
        elif c in "01234567": q=2
        else: q=99
    elif q==1:
        if c in "01234567": q=2
        else: q=99
    elif q==2:
        if c in "01234567": q=2
        else: q=99
if q==2: print("Octal numeral")
else: print("Not an octal numeral")
