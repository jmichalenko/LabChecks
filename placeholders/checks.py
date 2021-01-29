import check50
import check50.c

@check50.check()
def exists():
    """placeholders.c exists"""
    check50.exists("placeholders.c")
    check50.include("1.txt")
    check50.include("2.txt")

@check50.check(exists)
def compiles():
    """placeholders.c compiles"""
    check50.c.compile("placeholders.c", lcs50=True)

@check50.check(compiles)
def test1():
    """handles inputs correctly"""
    out = check50.run("./placeholders").stdin(open("2.txt").read()).stdout(open("1.txt").read())
