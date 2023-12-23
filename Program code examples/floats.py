from sys import stdin
q=0
for c in stdin.readline().strip("\n"):
    if q==0:
        if c.isdigit(): q=1
        elif c==".": q=7
        else: q=99
    elif q==1:
        if c.isdigit(): q=1
        elif c==".": q=2
        elif c=="E" or c=="e": q=4
        else: q=99
    elif q==2:
        if c.isdigit(): q=3
        elif c=="E" or c=="e": q=4
        else: q=99
    elif q==3:
        if c.isdigit(): q=3
        elif c=="E" or c=="e": q=4
        else: q=99
    elif q==4:
        if c.isdigit(): q=6
        elif c=="+" or c=="-": q=5
        else: q=99
    elif q==5:
        if c.isdigit(): q=6
        else: q=99
    elif q==6:
        if c.isdigit(): q=6
        else: q=99
    elif q==7:
        if c.isdigit(): q=3
        else: q=99
    
if q in [2,3,6]: print("Is a valid floating point numeral")
else: print("Not a floating point numeral")
