from src.translator import translate_content


def test_chinese():
    is_english, translated_content = translate_content("这是一条中文消息")
    assert is_english == False
    assert translated_content == "This is a Chinese message"

def test_llm_normal_response():
    pass

def test_llm_gibberish_response():
    is_english, translated_content = translate_content("abcd1234!")
    assert is_english == False
    assert translated_content == "I don't understand your request"
    is_english2, translated_content = translate_content("??¿¿!!??")
    assert is_english2 == False
    assert translated_content == "I don't understand your request"
    is_english3, translated_content = translate_content("||| broken sentence.")
    assert is_english3 == False
    assert translated_content == "I don't understand your request"
    is_english4, translated_content = translate_content("テスト123 abc xyz")
    assert is_english4 == False
    assert translated_content == "I don't understand your request"
    is_english5, translated_content = translate_content(".....!!!???...")
    assert is_english5 == False
    assert translated_content == "I don't understand your request"