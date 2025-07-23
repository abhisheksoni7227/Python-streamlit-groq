# from openai import OpenAI
import os

from dotenv import find_dotenv , load_dotenv # type: ignore
from groq import Groq # type: ignore
import  streamlit as st # type: ignore

load_dotenv(find_dotenv())
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def generate_milestone(task_description):
    # prompt= f''''Break down the following tasks into smaller milestones:
    # \n\nTask:
    # {task_description}
    # \n\n step or milestones: '''``


    prompt= f''''Give in simple and elobrated manner
    {task_description}
    \n\n '''

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",

                    # "content":"You are a super knowledgeable, kind, super fun teacher who teaches everyone like a kid in super simple manner"
                    "content": "You are a efficient task-driven and successful person. You have helped millions of people to be more productive and able to accomplish their most important goals and milestones in their life in simpler and deeper and detailed way. "

                },
                {

                    "role": "user",
                    "content": f"Breakdown the following task in smaller milestones or steps: \n\n{prompt} ",
                }
            ],
            model="llama3-8b-8192",
            stream=False,

        )

        # print(chat_completion.choices[0].message.content)
        return chat_completion.choices[0].message.content
    except Exception as e: return f'an error occure here---> \n {e}'

def app_console():
    print('****** Welcome to Task And Milestone Generator ******')
    task_description = input('Enter the task you would like to breakdown: ')
    if task_description:
        print('Generating milestone... ')

        milestone  = generate_milestone(task_description)
        if milestone:
            print(milestone)

        else:print('Failed to generate milestone')
    else:print('Error getting task description ')

def main():
    # app_console()
    streamlit_app()

def streamlit_app():
    st.title("PathFinder🔎: Get the step guides for anything")
    task_description = st.text_area("Enter the task you wish to be guided for:")
    if st.button('Generate...  ♪(´▽｀) '):
        if task_description:
            milestones = generate_milestone(task_description)
            st.markdown(" ============= Milestones / Steps:: =============")
            st.write(milestones)
        else:
            st.write('( ͠° ͟ʖ ͡°) Did you seriously clicked generate without any text ...？')

main()