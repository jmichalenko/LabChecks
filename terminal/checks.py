import check50
import check50.c

@check50.check()
def exists1():
    """apt1 exists"""
    check50.exists("apt1/test.txt")
@check50.check()
def exists2():
    """apt1/kitchen exists"""
    check50.exists("apt1/kitchen")
