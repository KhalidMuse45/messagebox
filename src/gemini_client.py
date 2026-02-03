import os
from dotenv import load_dotenv
from google import genai


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
#genai.configure(api_key=api_key)
if not API_KEY:
    raise ValueError("Please set the API key in your .env file ")

client = genai.Client(api_key = API_KEY)

def ask_question(watched_movies) -> str:
    if not watched_movies:
        return ' No Movies watched/provided'

    movies_str = '\n'.join(watched_movies)
    prompt = f"""Here is a list of movies this person has ALREADY WATCHED (do NOT recommend any of these):
{movies_str}

Recommend exactly 3 NEW movies they have NOT seen yet. Every recommendation MUST be different from every movie in the list above. Do not repeat any title from the list above.

Your response must use this exact format for each of the 3 movies:
Title: [movie title]
Year: [year]
Director: [director name]
why it fits: [short reason]

Use # as a delimiter between each movie. Do not include list brackets, extra commas, or any other text. Only the format above, three times, separated by #."""

    try:
        response = client.models.generate_content(
            model ="gemini-2.5-flash",
            contents = prompt
            #max_output_tokens = 500,
            #api_key = API_KEY
        )
        return response.text

    except Exception as e:
        return f"Error:{e}"