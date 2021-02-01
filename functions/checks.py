import check50
import check50.c

@check50.check()
def exists():
    """functions.c exists"""
    check50.exists("functions.c")

@check50.check(exists)
def compiles():
    """functions.c compiles"""
    check50.c.compile("functions.c", lcs50=True)

@check50.check(compiles)
def test1():
    """handles an input of 10 correctly"""
    out = check50.run("./functions").stdin("10").stdout("My positive int is 10.")
    
@check50.check(compiles)
def test_reject_negative():
    """rejects a negative input like -1"""
    check50.run("./functions").stdin("-1").reject()
    
