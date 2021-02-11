import check50
import check50.c

@check50.check()
def exists():
    """binary.c exists"""
    check50.exists("binary.c")
   
@check50.check(exists)
def compiles():
    """binary.c compiles"""
    check50.c.compile("binary.c", lcs50=True)

@check50.check(compiles)
def test1():
    """handles an input of 18 correctly"""
    out = check50.run("./binary").stdin("18").stdout("Found")

@check50.check(compiles)
def test2():
    """handles an input of 23 correctly"""
    out = check50.run("./binary").stdin("23").stdout("Not found!")
