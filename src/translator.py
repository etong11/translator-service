from openai import AzureOpenAI
import os

if os.path.exists('.env'):
    from dotenv import load_dotenv
    load_dotenv()

# Initialize the Azure OpenAI client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-15-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

GET_LANGUAGE_ERROR = "Error: Azure LLM call to get language failed."
INVALID_LANGUAGE = "Error: Azure LLM call to get language returned an invalid language."
TRANSLATE_ERROR = "Error: Azure LLM call to translate post failed."

def get_language(post: str) -> str:
    context = "You are a translator for a Q&A platform. Your job is to take in post content and determine what language it is. Only return this language."
    response = client.chat.completions.create(
    model="gpt-4o-mini",  # This should match your deployment name in Azure
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

def get_translation(post: str) -> str:
    context = "You are a translator for a Q&A platform. Your job is to take in non-English post content and translate it into English. You will be given an input of content to translate and will return the English translation."
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
  except Exception as e:
    return (True, INVALID_LANGUAGE)

  if isEnglish:
      result = (isEnglish, content)
  else:
      if " " in post_lang:
        return (True, INVALID_LANGUAGE)
      try:
        translation = get_translation(content)
        result = (isEnglish, translation)
      except Exception as e:
          return (True, TRANSLATE_ERROR)
  return result
