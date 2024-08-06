from crewai import Agent

from dotenv import load_dotenv
load_dotenv()

#too call gemini models one importtant library we are going to use below
from langchain_google_genai import ChatGoogleGenerativeAi
##Call the gemini models

llm  = ChatGoogleGenerativeAi(
                                model="",
                                verbose=True,
                                temperature=0.5,
                                google_api_key=os.getenv("GOOGLE_API_KEY"))

## Creating a senior researcher agent with memory and verbose mode

##This person is responsible in creating the news
researcher = Agent(
    role="Senior Researcher",
    goal="Uncover groundbreaking technologies in {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "Driven by the curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."
    ),
    tools=[],
    llm=llm,
    allow_delegation=True,#because I want the researcher to probably communicate with other agents
)

##Creating a writer agents with custom tools reponsible in writing news blog
news_writer = Agent(
    role="Writer",
    goal="Narrate compelling tech stories about {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair of simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[],
    llm=llm,
    allow_delegation=False,#because once the researcher is done and come to the writer, it is responsible for writer to write the entire blog
)
 