import check50
import check50.c

@check50.check()
def exists():
    """monte_hall.c exists"""
    check50.exists("monte_hall.c")

@check50.check(exists)
def compiles():
    """monte_hall.c compiles"""
    check50.c.compile("monte_hall.c", lcs50=True)
