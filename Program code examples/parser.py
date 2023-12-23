from sys import exit,stdin
def error(s): print(s); exit(1)
def e():
    print("E -> TE'")
    t(); eprime()
def eprime():
    global next
    if next=="+":
        print("E' -> +E")
        next=stdin.read(1)
        e()
    elif next=="-":
        print("E' -> -E")
        next=stdin.read(1)
        e()
    else: print("E ->")
def t():
    global next
    if next=="a":
        print("T -> a")
        next=stdin.read(1)
    elif next=="(":
        print("T -> (E)")
        next=stdin.read(1)
        e()
        if next!=")": error(") expected.")
        next=stdin.read(1)
    else: error("T cannot start with %s"%(next))

next=stdin.read(1)
e()
