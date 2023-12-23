from sys import stdin

q=0
sgn=1   # SEM: sign
val=0   # SEM: absolute value
for c in stdin.readline().strip("\n"):
    if q==0:
        if c=="+": q=1
        elif c=="-": sgn=-1; q=1
        elif c in "01234567": val=int(c); q=2
        else: q=99
    elif q==1:
        if c in "01234567": val=int(c); q=2
        else: q=99
    elif q==2:
        if c in "01234567": val=8*val+int(c); q=2
        else: q=99
if q==2: print("Octal numeral; decimal presentation is", sgn*val)
else: print("Not an octal numeral")
