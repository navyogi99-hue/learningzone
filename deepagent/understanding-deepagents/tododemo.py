from utils import get_model
from tools import(
    get_local_cuisine,
    get_popular_city,
    get_top_attraction,
    best_time_to_visit,
    get_weather
)
from deepagents import create_deep_agent

model =get_model()

agent = create_deep_agent(
    model=model,
    tools=[get_local_cuisine,
            get_popular_city,
            get_top_attraction,
            best_time_to_visit,
            get_weather],
            system_prompt="You are a travel assistant that helps users plan their trips by providing information about popular cities, attractions, local cuisine, weather, and the best time to visit."
            )
if __name__ == "__main__":
    TASK="Plan a trip to India. I want to visit the most popular city, know the top attractions, best time to visit, local cuisine, and current weather."
    result = agent.invoke(
        {
            "messages": [
                {"role": "user", "content": TASK}
            ]
        }
    )
    print(result)