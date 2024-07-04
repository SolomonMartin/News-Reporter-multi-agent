from crewai import Agent
from dotenv import load_dotenv
load_dotenv()
from tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
import os

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",verbose=True,Temperature = 0.5,google_api_key = os.getenv("GOOGLE_API_KEY"))

# Senior research agent with memory 

news_researcher  = Agent(
    role = "Senior Researcher",
    goal = 'Uncover latest updates and advancements in {topic}',
    verbose = True,
    memory = True,
    backstory = ("Driven by curiosity, you're at the forefront of innovation , easger to explore and share knowledge that could change the world"),
    tools = [tool],
    llm = llm,
    allow_delegation = True,
)

## Writer agent with custom tools 

news_writer = Agent(
    role = "Write",
    goal = 'Narrate compelling tech stories about {topic}',
    verbose = True,
    memory = True,
    backstory = ( 
    """With a flair for simplifying complex topics , you craft
    engaging narratives that captive and educate, bringing new
    discoveries to light in an accessible manner.
    """
    ),
    tools = [tool],
    llm = llm,
    allow_delegation = False,
    
)