import check50
import check50.c

@check50.check()
def exists():
    """recursion.c exists"""
    check50.exists("recursion.c")
 
@check50.check(exists)
def compiles():
    """recursion.c compiles"""
    check50.c.compile("recursion.c", lcs50=True)

@check50.check(compiles)
def test1():
    """Adds up the numbers correctly"""
    out = check50.run("./recursion").stdin("4").stdout("The sum of 1 through 4 is: 10")
