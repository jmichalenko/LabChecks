import check50
import check50.c

@check50.check()
def exists():
    """students.c exists"""
    check50.exists("st.c")
    check50.include("1.txt")
    check50.include("2.txt")

@check50.check(exists)
def compiles():
    """students.c compiles"""
    check50.c.compile("students.c", lcs50=True)

@check50.check(compiles)
def test1():
    """handles inputs correctly"""
    out = check50.run("./students").stdin(open("2.txt").read()).stdout(open("1.txt").read())
