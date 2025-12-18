import os
import json
from google import genai
from google.api_core import exceptions

def load_local_snippets():
    """Reads the JSON library."""
    try:
        if os.path.exists("snippets.json"):
            with open("snippets.json", "r") as f:
                return json.load(f)
    except Exception as e:
        print(f"Error loading JSON: {e}")
    return {}

def generate_project_code(user_query, language):
    """AI First -> Local Library Second -> Universal Fallback Third."""
    
    # 1. --- TRY AI MODE ---
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key:
        try:
            client = genai.Client(api_key=api_key)
            prompt = f"Write a professional {language} script for: '{user_query}'. Return ONLY code."
            response = client.models.generate_content(
                model="gemini-2.0-flash-lite", 
                contents=prompt
            )
            return response.text
        except Exception as e:
            print(f"AI Mode failed (Limit or Connection). Switching to Local.")

    # 2. --- TRY LOCAL LIBRARY ---
    library = load_local_snippets()
    query = user_query.lower()
    lang = language.lower()

    for keyword, data in library.items():
        if keyword in query:
            if lang in data:
                return f"# [LOCAL SNIPPET] {keyword.upper()}\n\n" + data[lang]

    # 3. --- UNIVERSAL FALLBACK (When everything else fails) ---
    return f"""#  Manual Boilerplate
# Request: {user_query}
# Language: {language.upper()}
# Note: AI is currently offline and no local snippet was found for this query.

def start_project():
    # Placeholder for your logic
    print("Welcome to your '{user_query}' project!")
    print("Develop your code here...")

if __name__ == "__main__":
    start_project()
"""