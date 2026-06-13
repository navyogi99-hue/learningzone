from langchain.tools import tool
import random


@tool(parse_docstring=True)
def get_weather(city: str) -> str:
    """Get the current weather for a city.

    Args:
        city (str): City name.

    Returns:
        str: Current weather of the city.
    """
    return f"It's a sunny day in {city}"


@tool(parse_docstring=True)
def get_popular_city(country: str) -> str:
    """Get the most popular city in a country.

    Args:
        country (str): Country name.

    Returns:
        str: The most popular city in the country.
    """
    cities = ["Hyderabad", "Delhi", "Mumbai"]
    return random.choice(cities)


@tool(parse_docstring=True)
def get_top_attraction(city: str) -> str:
    """Get the top attraction in a city.

    Args:
        city (str): City name.

    Returns:
        str: Attractions if found, else a message.
    """
    attractions = {
        "Hyderabad": ["Charminar", "Golconda Fort", "Hussain Sagar Lake", "Birla Mandir"],
        "Delhi": ["Red Fort", "India Gate", "Qutub Minar", "Lotus Temple"],
        "Mumbai": ["Gateway of India", "Elephanta Caves", "Chhatrapati Shivaji Terminus", "Marine Drive"],
    }

    result = attractions.get(city)
    return ", ".join(result) if result else f"No attractions found in {city}"


@tool(parse_docstring=True)
def best_time_to_visit(city: str) -> str:
    """Get the best time to visit a city.

    Args:
        city (str): City name.

    Returns:
        str: Best time to visit the city.
    """
    best_time = {
        "Hyderabad": "October to February",
        "Delhi": "October to March",
        "Mumbai": "November to February",
    }
    return best_time.get(city, f"Best time to visit {city} is not available")


@tool(parse_docstring=True)
def get_local_cuisine(city: str) -> str:
    """Get the local cuisine of a city.

    Args:
        city (str): City name.

    Returns:
        str: Local cuisine of the city.
    """
    local_cuisine = {
        "Hyderabad": "Biryani, Haleem, Kebabs",
        "Delhi": "Chaat, Butter Chicken, Parathas",
        "Mumbai": "Vada Pav, Pav Bhaji, Bhel Puri",
    }
    return local_cuisine.get(city, f"Local cuisine of {city} is not available")  