import check50
import check50.c

@check50.check()
def exists1():
    """fileio exists"""
    check50.exists("fileio.c")
@check50.check()
def exists2():
    """copy.txt exists"""
    check50.exists("copy.txt")
