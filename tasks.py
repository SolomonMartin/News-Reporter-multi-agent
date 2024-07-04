from crewai import Task 
from tools import tool
from agents import news_researcher,news_writer

research_task = Task(
    description = (
        """
        Identify the next big trend in {topic}, focus on identifying pros and cons and the overall
        narrative. your final report should clearly articulate the key points, its market
        oppurtunities , and potential risks
        """
    ),
    expected_output = 'A comprehensive 3 para long report on the latest trends in {topic}',
    tools = [tool],
    agent = news_researcher

)

write_task = Task(
    description = (
        """
        Compose an insightful articulate on {topic}. focus on 
        the latest trends and how its impacting the industry. this
        article should be easy to understand, engaging and positive
        """
    ),
    expected_output = 'A 4 para article on {topic} advancements formatted as markdown',
    tools = [tool],
    agent = news_writer,
    async_execution = False,
    output_file='new-blog-post.md',
)