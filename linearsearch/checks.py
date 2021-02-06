import check50
import check50.c

@check50.check()
def exists():
    """linear.c exists"""
    check50.exists("linear.c")

@check50.check(exists)
def compiles():
    """linear.c compiles"""
    check50.c.compile("linear.c", lcs50=True)

@check50.check(compiles)
def test1():
    """handles an input of 7 correctly"""
    out = check50.run("./linear").stdin("7").stdout("Found your number! Bingo!")

@check50.check(compiles)
def test2():
    """handles an input of 64 correctly"""
    out = check50.run("./linear").stdin("64").stdout("Found your number! Bingo!")
    
@check50.check(compiles)
def test3():
    """handles an input in middle of array correctly"""
    out = check50.run("./linear").stdin("34").stdout("Found your number! Bingo!")
    
@check50.check(compiles)
def test4():
    """handles an input for number not on care correctly"""
    out = check50.run("./linear").stdin("41").stdout("Sorry better luck next time!")
