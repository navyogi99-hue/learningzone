from mcp.server.fastmcp import FastMCP
mcp = FastMCP("library-mcp-server")
@mcp.tool("add_book")
def add_book(title: str, author: str) -> str:
    """Adds a book to the library."""
    return f"Book added: {title} by {author}"
def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
