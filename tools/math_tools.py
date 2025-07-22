"""
    Math tools:
    + -
"""
from langchain_core.tools import Tool


#+
def plus(a):
    return sum(map(int, a.split()))

#-
def minus(a):
    nums = list(map(int, a.split()))
    summ = nums[0] - nums[1]
    return summ


plus_tool = Tool(
        name="PlusTool",
        description="",
        func=lambda x: plus(x)
    )

minus_tool = Tool(
        name="MinusTool",
        description="",
        func=lambda x: minus(x)
    )
