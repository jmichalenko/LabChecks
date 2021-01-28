import check50
import check50.c

@check50.check()
def exists():
    """apt1 exists"""
    check50.exists("apt1/test.txt")
    
@check50.check()
def exists():
    """bathroom exists"""
    check50.exists("apt1/bathroom/")
    
@check50.check()
def exists():
    """apt1/bedroom exists"""
    check50.exists("apt1/bedroom")
    
@check50.check()
def exists():
    """apt1/kitchen exists"""
    check50.exists("apt1/kitchen")
