import check50
import check50.c

@check50.check()
def exists():
    """placeholders.c exists"""
    check50.exists("string.c")
    check50.include("1.txt")
    
@check50.check(exists)
def compiles():
    """string.c compiles"""
    check50.c.compile("string.c", lcs50=True)

@check50.check(compiles)
def test1():
    """handles inputs correctly"""
    out = check50.run("./string").stdin("John").stdout(open("1.txt").read())
