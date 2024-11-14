from src.translator import translate_content


def test_chinese():
    is_english, translated_content = translate_content("这是一条中文消息")
    assert is_english == False
    assert translated_content == "This is a Chinese message"

def test_llm_normal_response():
    is_english_1, translated_content = translate_content("This is an English message")
    assert is_english_1 == True
    assert translated_content == "This is an English message"

    is_english_2, translated_content = translate_content("Esta es un mensaje en español")
    assert is_english_2 == False
    assert translated_content == "This is a Spanish message"

    is_english_3, translated_content = translate_content("Ceci est un message en français")
    assert is_english_3 == False
    assert translated_content == "This is a French message"

    is_english_4, translated_content = translate_content("Это сообщение на русском")
    assert is_english_4 == False
    assert translated_content == "This is a Russian message"

    is_english_5, translated_content = translate_content("Esto es un mensaje en catalán")
    assert is_english_5 == False
    assert translated_content == "This is a Catalan message"

    is_english_6, translated_content = translate_content("هذه رسالة باللغة العربية")
    assert is_english_6 == False
    assert translated_content == "This is an Arabic message"

    is_english_7, translated_content = translate_content("นี่คือข้อความภาษาไทย")
    assert is_english_7 == False
    assert translated_content == "This is a Thai message"

    is_english_8, translated_content = translate_content("Bu bir Türkçe mesajdır")
    assert is_english_8 == False
    assert translated_content == "This is a Turkish message"

    is_english_9, translated_content = translate_content("Esta é uma mensagem em português")
    assert is_english_9 == False
    assert translated_content == "This is a Portuguese message"

    is_english_10, translated_content = translate_content("これは日本語のメッセージです")
    assert is_english_10 == False
    assert translated_content == "This is a Japanese message"

    is_english_11, translated_content = translate_content("이것은 한국어 메시지입니다")
    assert is_english_11 == False
    assert translated_content == "This is a Korean message"

    is_english_12, translated_content = translate_content("Dies ist eine Nachricht auf Deutsch")
    assert is_english_12 == False
    assert translated_content == "This is a German message"

    is_english_13, translated_content = translate_content("Questo è un messaggio in italiano")
    assert is_english_13 == False
    assert translated_content == "This is an Italian message"

    is_english_14, translated_content = translate_content("यह हिंदी में संदेश है")
    assert is_english_14 == False
    assert translated_content == "This is a Hindi message"

    is_english_15, translated_content = translate_content("Đây là một tin nhắn bằng tiếng Việt")
    assert is_english_15 == False
    assert translated_content == "This is a Vietnamese message"

def test_llm_gibberish_response():
    pass