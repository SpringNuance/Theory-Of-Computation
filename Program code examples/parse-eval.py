from sys import stdin
def error(s): print(s); exit(1)
def e():          # E -> T + E | T
    global next
    pf1=t()
    if next=="+":
        next=stdin.read(1)
        return pf1+e()+"+" # E1.pf := T.pf E2.pf +
    else: return pf1       # E.pf  := T.pf
def t():          # T -> F * T | F
    global next
    pf1=f()
    if next=="*":
        next=stdin.read(1)
        return pf1+t()+"*" # T1.pf := F.pf T2.pf *
    else: return pf1       # T.pf  := F.pf
def f():          # F -> a | (E)
    global next
    if next=="a":
        next=stdin.read(1)
        return "a"                    # F.pf := a
    elif next=="(":
        next=stdin.read(1)
        pf=e()
        if next!=")": error(") expected.")
        next=stdin.read(1)
        return pf                     # F.pf := E.pf
    else: error("F cannot start with this.")

next=stdin.read(1)
print(e())
