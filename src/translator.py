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

# def translate_content(content: str) -> tuple[bool, str]:
#     if content == "这是一条中文消息":
#         return False, "This is a Chinese message"
#     if content == "Ceci est un message en français":
#         return False, "This is a French message"
#     if content == "Esta es un mensaje en español":
#         return False, "This is a Spanish message"
#     if content == "Esta é uma mensagem em português":
#         return False, "This is a Portuguese message"
#     if content  == "これは日本語のメッセージです":
#         return False, "This is a Japanese message"
#     if content == "이것은 한국어 메시지입니다":
#         return False, "This is a Korean message"
#     if content == "Dies ist eine Nachricht auf Deutsch":
#         return False, "This is a German message"
#     if content == "Questo è un messaggio in italiano":
#         return False, "This is an Italian message"
#     if content == "Это сообщение на русском":
#         return False, "This is a Russian message"
#     if content == "هذه رسالة باللغة العربية":
#         return False, "This is an Arabic message"
#     if content == "यह हिंदी में संदेश है":
#         return False, "This is a Hindi message"
#     if content == "นี่คือข้อความภาษาไทย":
#         return False, "This is a Thai message"
#     if content == "Bu bir Türkçe mesajdır":
#         return False, "This is a Turkish message"
#     if content == "Đây là một tin nhắn bằng tiếng Việt":
#         return False, "This is a Vietnamese message"
#     if content == "Esto es un mensaje en catalán":
#         return False, "This is a Catalan message"
#     if content == "This is an English message":
#         return True, "This is an English message"
#     return True, content

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
    return (False, GET_LANGUAGE_ERROR)

  try:
    isEnglish = 'english' in post_lang.lower()  # Accounts for possible regional dialects
  except Exception as e:
    return (False, INVALID_LANGUAGE)

  if isEnglish:
      result = (isEnglish, content)
  else:
      if " " in post_lang:
        return (False, INVALID_LANGUAGE)
      try:
        translation = get_translation(content)
        result = (isEnglish, translation)
      except Exception as e:
          return (False, TRANSLATE_ERROR)
  return result
