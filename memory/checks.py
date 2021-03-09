import check50
import check50.c

@check50.check()
def exists():
    """memory.c exists"""
    check50.exists("memory.c")
    check50.include("1.txt")

@check50.check(exists)
def compiles():
    """memory.c compiles"""
    check50.c.compile("memory.c", lcs50=True)
    
@check50.check(compiles)
def numbers_swapped():
    """Numbers get swapped"""
    out = check50.run("./memory").stdout(open("1.txt").read())
