# Import libraries
import asyncio  # run async programs in parallel
import json

from dotenv import load_dotenv  # loading env variables from .env file
from openai import AsyncOpenAI  # openai api for translation and image generation
from pydantic import BaseModel
from tqdm import tqdm  # monitor progress of model operations

# Load environment variable (OpenAI API key) from .env file
load_dotenv()

# Set up AsyncOpenAI client for parallel processing
client = AsyncOpenAI()

# Define simple topic-hindiwords dictionary
topics = {
    "Animals": ["बिल्ली", "कुत्ता", "हाथी", "जिराफ", "खरगोश"],
    "Fruits": ["सेब", "केला", "चेरी", "अंगूर", "संतरा"],
    "Vehicles": ["कार", "बाइक", "विमान", "जहाज","बस"],
    "Things": ["किताब", "कुर्सी", "टेबल", "पेंसिल", "घड़ी"],
    "Places": ["स्कूल", "घर", "पार्क", "हॉस्पिटल", "पुस्तकालय"]
}

# Defining structured output from API with Pydantic object
class HindiResponse(BaseModel):
    english_text: list[str]

# Async Function to translate text using OpenAI Chat Completions API
async def translate_text(words, topic):
    response = await client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"Translate the list of user words from Hindi to English. Once translated, ensure the words are returned in the same order as user input. The words in the list belongs to the topic: {topic}"},
            {"role": "user", "content": f"{words}"}
        ], response_format=HindiResponse
    )
    return json.loads(response.choices[0].message.content)['english_text']

async def run_loop(topics):
    tasks = [translate_text(words_list, topic) for topic, words_list in topics.items()]
    translated_topics = await asyncio.gather(*tasks)
    return translated_topics

# Translate dictionary values
translated_topics = asyncio.run(run_loop(topics))

print(translated_topics)