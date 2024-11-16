from openai import AzureOpenAI
import os

if os.path.exists('.env'):
    from dotenv import load_dotenv
    load_dotenv()

# Check if environment variables are set
if not os.getenv("AZURE_OPENAI_API_KEY"):
    raise EnvironmentError("AZURE_OPENAI_API_KEY is not set")
if not os.getenv("AZURE_OPENAI_ENDPOINT"):
    raise EnvironmentError("AZURE_OPENAI_ENDPOINT is not set")

# Initialize the Azure OpenAI client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-15-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

GET_LANGUAGE_ERROR = "Error: Azure LLM call to get language failed."
INVALID_LANGUAGE_RESPONSE = "Error: Azure LLM call to get language returned an invalid response."
TRANSLATE_ERROR = "Error: Azure LLM call to translate post failed."

def get_translation(post: str) -> str:
    context = """
    You are a translator for a Q&A platform. Your job is to take in non-English post content and translate it into English. 
    You will be given an input of content to translate and will return the English translation. 
    If you are unable to determine an English translation, return the exact same text that you were given.
    """
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
          "role": "system",
          "content": f"{context}"
        },
        {
            "role": "user",
            "content": f"{post}"
        }
      ]
    )
    res = (response.choices[0].message.content)
    return res

def get_language(post: str) -> str:
    context = """
    You are a translator for a Q&A platform. Your job is to take in post content and determine what language it is in. Only return this language in its English form.
    If you are unable to recognize the language, only return "Unknown". If you think this post is written in English, return "English".
    """
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
          "role": "system",
          "content": f"{context}"
        },
        {
            "role": "user",
            "content": f"{post}"
        }
      ]
    )
    res = (response.choices[0].message.content)
    return res

def translate_content(content: str) -> tuple[bool, str]:
  if content == "":
    return (True, content)

  try:
    post_lang = get_language(content)
  except Exception as e:
    return (True, GET_LANGUAGE_ERROR)

  try:
    isEnglish = 'english' in post_lang.lower()  # Accounts for possible regional dialects
    isUnknown = 'unknown' in post_lang.lower()
    isResponseNotAlpha = not post_lang.isalpha()
  except Exception as e:
    return (True, INVALID_LANGUAGE_RESPONSE)

  if isEnglish or isUnknown:
      result = (True, content)
  elif isResponseNotAlpha:
      result = (True, INVALID_LANGUAGE_RESPONSE)
  else:
      try:
        translation = get_translation(content)
        result = (isEnglish, translation)
      except Exception as e:
          return (True, TRANSLATE_ERROR)
  return result
