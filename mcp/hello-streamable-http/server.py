from mcp.server.fastmcp import FastMCP
mcp= FastMCP(
    "Demo streamable MCP Server",
    host="localhost",
    port= "3001"
)
@mcp.tool(name= "add" , description="Add two numbers")
def add(a:int , b:int)-> int:
    return a + b
@mcp.tool(name="multiply", description="Multiply two numbers")
def multiply(a: int, b: int) -> int:
    return a * b
@mcp.tool(name="substract", description="Subtract two numbers")
def substract(a: int, b: int) -> int:
    return a - b
@mcp.tool(name="divide", description="Divide two numbers")
def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Denominator cannot be zero")
    return a / b
if __name__ == "__main__":
    mcp.run(transport="streamable-http")