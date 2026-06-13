from utils import get_model
from langchain.tools import tool
from deepagents import create_deep_agent

@tool()
def add(a:int|float, b:int|float) -> int|float:
    """Performs addition of two numbers
    
    Args:
        a (int|float): The first number.
        b (int|float): The second number.

    Returns:
        int|float: The sum of the two numbers.
    """
    return a + b

@tool()
def subtract(a:int|float, b:int|float) -> int|float:
    """Performs subtraction of two numbers
    
    Args:
        a (int|float): The first number.
        b (int|float): The second number.

    Returns:
        int|float: The difference of the two numbers.
    """
    return a - b
@tool()
def multiply(a:int|float, b:int|float) -> int|float:
    """Performs multiplication of two numbers
    
    Args:
        a (int|float): The first number.
        b (int|float): The second number.

    Returns:
        int|float: The product of the two numbers.
    """
    return a * b
@tool()
def divide(a:int|float, b:int|float) -> int|float:
    """Performs division of two numbers
    
    Args:
        a (int|float): The first number.
        b (int|float): The second number.

    Returns:
        int|float: The quotient of the two numbers.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
@tool()
def modulus(a:int|float, b:int|float) -> int|float:
    """Performs modulus of two numbers
    
    Args:
        a (int|float): The first number.
        b (int|float): The second number.

    Returns:
        int|float: The modulus of the two numbers.
    """
    if b == 0:
        raise ValueError("Cannot perform modulus by zero.")
    return a % b

model = get_model()

agent = create_deep_agent(
    model=model,
    system_prompt="You are a helpful assistant in performing logical and mathematical operations.",
    tools=[add, subtract, multiply, divide, modulus]
)
