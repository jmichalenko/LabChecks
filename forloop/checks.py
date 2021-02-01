import check50
import check50.c

@check50.check()
def exists():
    """dowhile.c exists"""
    check50.exists("foorloop.c")

@check50.check(exists)
def compiles():
    """dowhile.c compiles"""
    check50.c.compile("forloop.c", lcs50=True)
    
@check50.check(compiles)
def ten():
    """Adds up the total for numbers 1-10"""
    check50.run("./forloop").stdout(The total of the numbers from 1 to 10 is: 55).exit()
    
