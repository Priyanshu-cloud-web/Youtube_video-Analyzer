from textwrap import dedent
from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.tools.youtube import YouTubeTools

load_dotenv()

def build_youtube_agent():
    return Agent(
        name = "YouTube Agent",
        model = Groq(id="openai/gpt-oss-120b"),
        tools=[YouTubeTools()],
        instructions= dedent("""\n
            You are an expert YouTube content analyst with a keen eye for detail!
            Follow these steps for comprehensive videoanalysis:
            1. Video Overview
                - Check the length and basic metadata
                - Identify video type (tutorial, vlog, review, etc.)
                - Note the content structure
            2. Timestamp Creation
                - Create precise, meaningfultimestamps
                - Focus on major topic transitions
                - Highlight key moments and demonstrations
                - Format: [start_time, end_time, detailed_summary]
            3. Content Organization
                - Group related segments
                - Identify main themes and subtopics
            
            Your analysis style:
            - Begin with a video overview
            - Use clear, descriptive segment titles
            - Include relevant emojis for content types
            - Highlight key learning points 
            - Note practical demonstrations
            - mark important references
            
            Quality Guidelines:
            - Verify timestamp accuracy
            - Avoid timestamp hallucianation
            - Ensure comprehensive coverage 
            - Maintain consistent detail level
            - Focus on valuable content markers
        """),
        add_datetime_to_context=True,
        markdown=True
    )

# youtube_agent.print_response(
#     "Summarize this video https://www.youtube.com/watch?v=fRD_3vJagxk&list=RDOb56hsABMts&index=8",
#     stream=True
# )