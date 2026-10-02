import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)


def get_learning_path(career, profile):

    prompt = f"""
You are a career learning advisor for interns.

Recommended career:
{career}

Intern profile:
{profile}

Create a personalized learning path for this intern.

Requirements:
- Give 6 to 8 learning topics.
- Start from the intern's current skills.
- Focus on skills needed for the recommended career.
- Consider the intern's interests.
- Order the topics from beginner to advanced.
- Return only a numbered list.
"""

    response = model.invoke(
        [HumanMessage(content=prompt)]
    )

    return response.text