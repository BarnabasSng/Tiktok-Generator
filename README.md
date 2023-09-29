# TikTok-Generator
This chatbot creates ideas for TikTok videos based on current, viral trends. With TikTok as such an important platform for aspiring influencers and corporations to reach out to a wider audience, I felt that there is potential for a bot that could generate ideas for TikTok videos quickly. However, TikTok is well-known for having trends that go viral very quickly but are short-lived. As such, using conventional large language models (LLM) such as ChatGPT is an ineffective way to generate videos that can go viral as it is not up-to-date on the most recent trends. As such, I decided to build a chatbot that integrates an LLM (GPT-4) as well as the Google Search API.

I used the OpenAi API to query GPT-4 and used the model to answer my prompts. I also used Langchain in order to interact with Google Search API to find viral trends. This allows the GPT-4 model to use more recent information to generate videos, as GPT-4 was only trained up to around September 2021. Finally, I used Streamlit to build the web app and host it.

## Examples
### Using the chatbot for commercial purposes
![image](https://github.com/BarnabasSng/Tiktok-Generator/assets/138547442/c6fd260c-13e2-4e59-989d-2208c1902fec)

Here, I used the chatbot to generate a video that would showcase the design of a lamp. This has potential for commercial use, as corporations increasingly use TikTok to publicise their products. The chatbot was able to identify a recent trend of sunset lamps, which went viral in March 2023. (https://www.today.com/shop/sunset-projection-lamps-t211085).

### Chatbot's ability to use very recent trends
![image](https://github.com/BarnabasSng/Tiktok-Generator/assets/138547442/e13759dc-00c6-48fb-aeca-70f48a732830)

To showcase a more recent trend, I used the chatbot to create a funny video about a meme that went viral very recently in September 2023, the blue smurf cat. (https://www.dexerto.com/entertainment/what-is-the-blue-smurf-cat-on-tiktok-viral-meme-explained-2293106/). The chatbot was even able to get the audio that is usually played in the background right, Alan Walker's The Spectre.

![image](https://github.com/BarnabasSng/Tiktok-Generator/assets/138547442/886dbc16-591b-46f9-bd5f-5a2bd92cd69a)

When I queried ChatGPT on what the blue smurf cat was about, it was unable to come up with the answer. Hence, this shows that by integrating Google Search to look up trends, the chatbot was able to utilise the new information to generate ideas that were significantly more relevant.
