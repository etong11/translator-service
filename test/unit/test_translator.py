from src.translator import translate_content
from src.translator import client

def test_chinese():
    is_english, translated_content = translate_content("这是一条中文消息")
    assert is_english == False
    assert translated_content == "This is a message in Chinese."

def test_llm_normal_response():
    is_english_1, translated_content = translate_content("This is an English message.")
    assert is_english_1 == True
    assert translated_content == "This is an English message."

    is_english_2, translated_content = translate_content("Esta es un mensaje en español.")
    assert is_english_2 == False
    assert translated_content == "This is a message in Spanish."

    # is_english_3, translated_content = translate_content("Ceci est un message en français.")
    # assert is_english_3 == False
    # assert translated_content == "This is a French message."

    # is_english_4, translated_content = translate_content("Это сообщение на русском.")
    # assert is_english_4 == False
    # assert translated_content == "This is a Russian message."

    # is_english_5, translated_content = translate_content("Esto es un mensaje en catalán.")
    # assert is_english_5 == False
    # assert translated_content == "This is a Catalan message."

    # is_english_6, translated_content = translate_content("هذه رسالة باللغة العربية.")
    # assert is_english_6 == False
    # assert translated_content == "This is an Arabic message."

    # is_english_7, translated_content = translate_content("นี่คือข้อความภาษาไทย.")
    # assert is_english_7 == False
    # assert translated_content == "This is a Thai message."

    # is_english_8, translated_content = translate_content("Bu bir Türkçe mesajdır.")
    # assert is_english_8 == False
    # assert translated_content == "This is a Turkish message."

    # is_english_9, translated_content = translate_content("Esta é uma mensagem em português.")
    # assert is_english_9 == False
    # assert translated_content == "This is a Portuguese message."

    # is_english_10, translated_content = translate_content("これは日本語のメッセージです.")
    # assert is_english_10 == False
    # assert translated_content == "This is a Japanese message."

    # is_english_11, translated_content = translate_content("이것은 한국어 메시지입니다.")
    # assert is_english_11 == False
    # assert translated_content == "This is a Korean message."

    # is_english_12, translated_content = translate_content("Dies ist eine Nachricht auf Deutsch.")
    # assert is_english_12 == False
    # assert translated_content == "This is a German message."

    # is_english_13, translated_content = translate_content("Questo è un messaggio in italiano.")
    # assert is_english_13 == False
    # assert translated_content == "This is an Italian message."

    # is_english_14, translated_content = translate_content("यह हिंदी में संदेश है")
    # assert is_english_14 == False
    # assert translated_content == "This is a Hindi message."

    # is_english_15, translated_content = translate_content("Đây là một tin nhắn bằng tiếng Việt.")
    # assert is_english_15 == False
    # assert translated_content == "This is a Vietnamese message."

# def test_llm_gibberish_response():
#     is_english, translated_content = translate_content("abcd1234!")
#     assert is_english == True
#     assert translated_content == "abcd1234!"
#     # is_english2, translated_content = translate_content("??¿¿!!??")
#     # assert is_english2 == False
#     # assert translated_content == "??¿¿!!??"
#     is_english3, translated_content = translate_content("||| broken sentence.")
#     assert is_english3 == True
#     assert translated_content == "||| broken sentence."
#     # is_english4, translated_content = translate_content("テスト123 abc xyz")
#     # assert is_english4 == True
#     # assert translated_content == "テスト123 abc xyz"
#     # is_english5, translated_content = translate_content(".....!!!???...")
#     # assert is_english5 == True

# Mock tests
from mock import patch, MagicMock
import pytest

GET_LANGUAGE_ERROR = "Error: Azure LLM call to get language failed."
INVALID_LANGUAGE = "Error: Azure LLM call to get language returned an invalid language."
TRANSLATE_ERROR = "Error: Azure LLM call to translate post failed."

# These mock tests are commented out because we can't mock the LLM since the LLM response is hardcoded right now
# Test for unexpected language detection
@patch.object(client.chat.completions, 'create')
def test_unexpected_language(mocker):
    # Mock the response to simulate an unexpected message
    mocker.return_value.choices[0].message.content = "I don't understand your request"

    # Call the function and assert that the error message is returned
    assert translate_content("Hier ist dein erstes Beispiel.") == (True, INVALID_LANGUAGE)

# Test for non-string response from language detection
@patch.object(client.chat.completions, 'create')
def test_non_string_response_language(mocker):
    # Mock response to return a non-string type for language detection
    mocker.return_value.choices[0].message.content = 12345  # Non-string response

    # Call the function and check that the error message is returned
    result = translate_content("Hier ist dein erstes Beispiel.")
    print("getting this", result)
    assert result == (True, INVALID_LANGUAGE)

# Test for null response from language detection
@patch.object(client.chat.completions, 'create')
def test_null_response(mocker):
    mocker.return_value = None

    # Call the function and check that the error message is returned
    result = translate_content("Hier ist dein erstes Beispiel.")
    assert result == (True, GET_LANGUAGE_ERROR)

# Test for empty choices response from language detection
@patch.object(client.chat.completions, 'create')
def test_empty_choices_response(mocker):
    mocker.return_value.choices = []

    # Call the function and check that the error message is returned
    result = translate_content("Hier ist dein erstes Beispiel.")
    assert result == (True, GET_LANGUAGE_ERROR)


# Test for unexpected exception during translation
@patch.object(client.chat.completions, 'create')
def test_unexpected_exception_during_translation(mocker):
    # Simulate language detection being successful, but translation fails due to an unexpected error
    mocker.return_value.choices[0].message.content = "German"  # Mock valid language detection

    # Simulate an unexpected exception during translation (e.g., network issue, timeout, etc.)
    mocker.side_effect = Exception("Unexpected error during translation")

    # Call the function and check that the returned error tuple indicates failure
    result = translate_content("Hier ist dein erstes Beispiel.")
    assert result == (True, GET_LANGUAGE_ERROR)
