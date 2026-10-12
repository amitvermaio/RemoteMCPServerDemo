from random import randint
from fastmcp import FastMCP

mcp = FastMCP("Utility Server")

@mcp.tool
def add_numbers(first: float, second: float) -> float:
    """Add any number of numeric arguments and return their sum."""
    return first + second

@mcp.tool
def generate_random_number(min_value: int = 1, max_value: int = 100) -> int:
    """Generate a random integer between min_value and max_value, inclusive."""
    if min_value > max_value:
        raise ValueError("min_value cannot be greater than max_value")

    return randint(min_value, max_value)


# Resource: Structured information about available tools
@mcp.resource("tools://info")
def get_tools_info() -> dict:
    """Return structured metadata describing the server's tools."""	
    return {
        "server_name": "Utility Server",
        "tools": [
            {
                "name": "add_numbers",
                "description": "Add any number of numeric arguments.",
                "arguments": {
                    "numbers": {
                        "type": "number",
                        "variadic": True,
                        "required": False,
                    }
                },
                "example": {
                    "input": [10, 20, 30],
                    "output": 60,
                },
            },
            {
                "name": "generate_random_number",
                "description": "Generate a random integer within a range.",
                "arguments": {
                    "min_value": {
                        "type": "integer",
                        "default": 1,
                    },
                    "max_value": {
                        "type": "integer",
                        "default": 100,
                    },
                },
                "example": {
                    "input": {
                        "min_value": 10,
                        "max_value": 20,
                    },
                    "output": 15,
                },
            },
        ],
    }


if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=8000,
    )