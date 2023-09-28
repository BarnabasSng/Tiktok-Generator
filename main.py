import openai
import streamlit as st
import os
from langchain.tools import Tool
from langchain.utilities import GoogleSearchAPIWrapper
import time
from apikeys import openai_key,google_cse_key,google_api_key

os.environ["OPENAI_API_KEY"]= openai_key
os.environ["GOOGLE_CSE_ID"] = google_cse_key 
os.environ["GOOGLE_API_KEY"] = google_api_key

openai.api_key = openai_key

search = GoogleSearchAPIWrapper(k=10)

tool = Tool(
    name="Google Search",
    description="Search Google for recent trends on Tiktok.",
    func=search.run,
)

st.title('Viral Tiktok')
st.subheader('This app checks for current trends on Tiktok and helps you to create a video based on it.')

with st.chat_message("assistant"):
    st.markdown("Hi! What is the topic of your video?")

topic = st.text_input('Topic of video:')

if topic:
    with st.chat_message("assistant"):
        st.markdown("Great! Do you have any conditions you want your video to have? (e.g. time limit)")

    conditions = st.text_input('Write any specific conditions you want your video to have:')

    if conditions:
        with st.chat_message("assistant"):
            message_2 = st.empty()
            response_2 = ''
            for word in "No problem! I will now generate an idea for a Tiktok video.".split():
                response_2 += word + ' '
                time.sleep(0.05)
                message_2.markdown(response_2 + "▌")
            message_2.markdown(response_2)

        with st.chat_message("assistant"):
            trends = tool.run(f'{topic} Tiktok trends')
            final_message = st.empty()
            full_response = ""

            streamed_response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a professional video analyst that creates viral videos on Tiktok. The videos you make must be professional and not cheesy."},
                    {"role": "assistant", "content": f"Here are some recent tiktok trends about {topic}: {trends}"},
                    {"role": "user", "content": f"Use one of the tiktok trends given about {topic} and describe what it's about. Then, create a script for the video. The video must follow these conditions: {conditions}. Include a caption and relevant hashtags for the video"}],
            stream = True
            )

            for chunk in streamed_response:
                full_response += chunk.choices[0].delta.get("content", "")
                final_message.markdown(full_response + "▌")
            final_message.markdown(full_response)
