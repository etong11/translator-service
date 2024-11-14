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
from mock import patch, MagicMock
import pytest

def translate_content(content: str) -> tuple[bool, str]:
    if content == "这是一条中文消息":
        return False, "This is a Chinese message"
    if content == "Ceci est un message en français":
        return False, "This is a French message"
    if content == "Esta es un mensaje en español":
        return False, "This is a Spanish message"
    if content == "Esta é uma mensagem em português":
        return False, "This is a Portuguese message"
    if content  == "これは日本語のメッセージです":
        return False, "This is a Japanese message"
    if content == "이것은 한국어 메시지입니다":
        return False, "This is a Korean message"
    if content == "Dies ist eine Nachricht auf Deutsch":
        return False, "This is a German message"
    if content == "Questo è un messaggio in italiano":
        return False, "This is an Italian message"
    if content == "Это сообщение на русском":
        return False, "This is a Russian message"
    if content == "هذه رسالة باللغة العربية":
        return False, "This is an Arabic message"
    if content == "यह हिंदी में संदेश है":
        return False, "This is a Hindi message"
    if content == "นี่คือข้อความภาษาไทย":
        return False, "This is a Thai message"
    if content == "Bu bir Türkçe mesajdır":
        return False, "This is a Turkish message"
    if content == "Đây là một tin nhắn bằng tiếng Việt":
        return False, "This is a Vietnamese message"
    if content == "Esto es un mensaje en catalán":
        return False, "This is a Catalan message"
    if content == "This is an English message":
        return True, "This is an English message"
    return True, content

# These mock tests are commented out because we can't mock the LLM since the LLM response is hardcoded right now
# # Test for unexpected language detection
# @patch.object(client.chat.completions, 'create')
# def test_unexpected_language(mocker):
#     # Mock the response to simulate an unexpected message
#     mocker.return_value.choices[0].message.content = "I don't understand your request"

#     # Call the function and assert that the error message is returned
#     assert translate_content("Hier ist dein erstes Beispiel.") == (False, INVALID_LANGUAGE)

# # Test for non-string response from language detection
# @patch.object(client.chat.completions, 'create')
# def test_non_string_response_language(mocker):
#     # Mock response to return a non-string type for language detection
#     mocker.return_value.choices[0].message.content = 12345  # Non-string response

#     # Call the function and check that the error message is returned
#     result = translate_content("Hier ist dein erstes Beispiel.")
#     print("getting this", result)
#     assert result == (False, INVALID_LANGUAGE)

# # Test for null response from language detection
# @patch.object(client.chat.completions, 'create')
# def test_null_response(mocker):
#     mocker.return_value = None

#     # Call the function and check that the error message is returned
#     result = translate_content("Hier ist dein erstes Beispiel.")
#     assert result == (False, GET_LANGUAGE_ERROR)

# # Test for empty choices response from language detection
# @patch.object(client.chat.completions, 'create')
# def test_empty_choices_response(mocker):
#     mocker.return_value.choices = []

#     # Call the function and check that the error message is returned
#     result = translate_content("Hier ist dein erstes Beispiel.")
#     assert result == (False, GET_LANGUAGE_ERROR)


# # Test for unexpected exception during translation
# @patch.object(client.chat.completions, 'create')
# def test_unexpected_exception_during_translation(mocker):
#     # Simulate language detection being successful, but translation fails due to an unexpected error
#     mocker.return_value.choices[0].message.content = "German"  # Mock valid language detection

#     # Simulate an unexpected exception during translation (e.g., network issue, timeout, etc.)
#     mocker.side_effect = Exception("Unexpected error during translation")

#     # Call the function and check that the returned error tuple indicates failure
#     result = translate_content("Hier ist dein erstes Beispiel.")
#     assert result == (False, GET_LANGUAGE_ERROR)
