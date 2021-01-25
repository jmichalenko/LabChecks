import check50
import check50.c

@check50.check()
def exists():
    """Bathroom_cabinet.txt exists"""
    check50.exists("./bathroom/bathroom_cabinet/bathroom_cabinet.txt")
