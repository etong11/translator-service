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

def test_english_posts():
    is_english, translated_content = translate_content("What is the best way to learn programming?")
    assert is_english == True
    assert translated_content == "What is the best way to learn programming?"

    is_english, translated_content = translate_content("How can I improve my problem-solving skills?")
    assert is_english == True
    assert translated_content == "How can I improve my problem-solving skills?"

    is_english, translated_content = translate_content("What are the benefits of using cloud services for small businesses?")
    assert is_english == True
    assert translated_content == "What are the benefits of using cloud services for small businesses?"

    is_english, translated_content = translate_content("Is it necessary to learn data structures to become a software developer?")
    assert is_english == True
    assert translated_content == "Is it necessary to learn data structures to become a software developer?"

    is_english, translated_content = translate_content("How do I get started with machine learning")
    assert is_english == True
    assert translated_content == "How do I get started with machine learning"

    is_english, translated_content = translate_content("What's the best approach for learning new programming languages quickly?")
    assert is_english == True
    assert translated_content == "What's the best approach for learning new programming languages quickly?"

    is_english, translated_content = translate_content("What are some good resources for learning web development?")
    assert is_english == True
    assert translated_content == "What are some good resources for learning web development?"

    is_english, translated_content = translate_content("How can I protect my data from cyber threats?")
    assert is_english == True
    assert translated_content == "How can I protect my data from cyber threats?"

    is_english_9, translated_content = translate_content("What is the importance of version control in programming?")
    assert is_english == True
    assert translated_content == "What is the importance of version control in programming?"

    is_english, translated_content = translate_content("Which programming languages are best suited for AI development?")
    assert is_english == True
    assert translated_content == "Which programming languages are best suited for AI development?"

    is_english, translated_content = translate_content("What tools are recommended for managing remote teams effectively?")
    assert is_english == True
    assert translated_content == "What tools are recommended for managing remote teams effectively?"

    is_english, translated_content = translate_content("How does blockchain technology impact data security?")
    assert is_english == True
    assert translated_content == "How does blockchain technology impact data security?"

    is_english, translated_content = translate_content("What are the key skills for a data scientist?")
    assert is_english == True
    assert translated_content == "What are the key skills for a data scientist?"

    is_english, translated_content = translate_content("What's the difference between supervised and unsupervised learning?")
    assert is_english == True
    assert translated_content == "What's the difference between supervised and unsupervised learning?"

    is_english, translated_content = translate_content("How do algorithms work in recommendation systems?")
    assert is_english == True
    assert translated_content == "How do algorithms work in recommendation systems?"

def test_non_english_posts():
    is_english, translated_content = translate_content("¿Cuál es la mejor manera de aprender Python?")
    assert is_english == False
    assert translated_content == "What is the best way to learn Python?"

    is_english, translated_content = translate_content("Quels sont les avantages du cloud computing?")
    assert is_english == False
    assert translated_content ==  "What are the advantages of cloud computing?"

    is_english, translated_content = translate_content("バックアップのベストプラクティスは何ですか？")
    assert is_english == False
    assert translated_content == "What are the best practices for backups?"

    is_english, translated_content = translate_content("Как настроить сервер для высокой безопасности?")
    assert is_english == False
    assert translated_content == "How to set up a server for high security?"

    is_english, translated_content = translate_content("Wie lernt man maschinelles Lernen am besten?")
    assert is_english == False
    assert translated_content == "What is the best way to learn machine learning?"

    is_english, translated_content= translate_content( "¿Cómo proteger mis datos en línea?")
    assert is_english == False
    assert translated_content == "How can I protect my data online?"

    is_english, translated_content = translate_content("Quais são os desafios da inteligência artificial?")
    assert is_english == False
    assert translated_content == "What are the challenges of artificial intelligence?"

    is_english, translated_content = translate_content("ما هي أفضل ممارسات الأمان على الإنترنت؟")
    assert is_english == False
    assert translated_content == "What are the best practices for online security?"

    is_english, translated_content = translate_content("Qual è il modo migliore per proteggere i dati?")
    assert is_english == False
    assert translated_content == "What is the best way to protect data?"

    is_english, translated_content = translate_content( "¿Cómo mejorar la productividad en equipos remotos?")
    assert is_english == False
    assert translated_content == "How to improve productivity in remote teams?"

    is_english, translated_content = translate_content("Quels outils sont essentiels pour la gestion de projet?")
    assert is_english == False
    assert translated_content == "What tools are essential for project management?"

    is_english, translated_content = translate_content("どのようにしてデータのセキュリティを向上させますか？")
    assert is_english == False
    assert translated_content == "How do you improve data security?"

    is_english, translated_content = translate_content( "Каковы лучшие методы защиты данных?")
    assert is_english == False
    assert translated_content == "What are the best methods for data protection?"

    is_english, translated_content = translate_content("Comment puis-je améliorer mes compétences en résolution de problèmes?")
    assert is_english == False
    assert translated_content == "How can I improve my problem-solving skills?"

    is_english, translated_content = translate_content("¿Cuál es la importancia del control de versiones?")
    assert is_english == False
    assert translated_content == "What is the importance of version control?"
    

def test_unintelligible_posts():
    is_english, translated_content = translate_content("abcd1234!")
    assert is_english == False
    assert translated_content == "abcd1234!"

    is_english, translated_content = translate_content("??¿¿!!??")
    assert is_english == False
    assert translated_content == "??¿¿!!??"

    is_english, translated_content = translate_content("||| broken sentence.")
    assert is_english == False
    assert translated_content == "||| broken sentence."

    is_english, translated_content = translate_content("テスト123 abc xyz")
    assert is_english == False
    assert translated_content == "テスト123 abc xyz"

    is_english, translated_content = translate_content(".....!!!???...")
    assert is_english == False
    assert translated_content == ".....!!!???..."
    
def test_llm_gibberish_response():
    pass