from src.translator import translate_content
from src.translator import client
from src.translator import INVALID_LANGUAGE_RESPONSE, GET_LANGUAGE_ERROR, TRANSLATE_ERROR
from sentence_transformers import SentenceTransformer, util
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Now you can access the variables using os.getenv
AZURE_OPENAI_API_KEY = os.getenv('AZURE_OPENAI_API_KEY')
AZURE_OPENAI_ENDPOINT = os.getenv('AZURE_OPENAI_ENDPOINT')
model = SentenceTransformer('all-MiniLM-L6-v2')

def eval_single_response_translation(expected_answer: str, llm_response: str) -> float:
  '''TODO: Compares an LLM response to the expected answer from the evaluation dataset using one of the text comparison metrics.'''
  # The sentences to encode
  sentences = [
      expected_answer, llm_response
  ]

  # Encode sentences to embeddings
  embedding1 = model.encode(sentences[0], convert_to_tensor=True)
  embedding2 = model.encode(sentences[1], convert_to_tensor=True)

  # Normalize embeddings (to prevent score from being outside of (-1, 1) range)
  embedding1 = embedding1 / embedding1.norm()
  embedding2 = embedding2 / embedding2.norm()

  similarity_score = util.cos_sim(embedding1, embedding2).item()
  print(similarity_score)

  return similarity_score

def test_english_posts():
    is_english, translated_content = translate_content("What is the best way to learn programming?")
    assert is_english == True
    similarity_score = eval_single_response_translation("What is the best way to learn programming?", translated_content)
    assert similarity_score > 0.9

    is_english, translated_content = translate_content("How can I improve my problem-solving skills?")
    assert is_english == True
    similarity_score = eval_single_response_translation("How can I improve my problem-solving skills?", translated_content)
    assert similarity_score > 0.9

    is_english, translated_content = translate_content("What are the benefits of using cloud services for small businesses?")
    assert is_english == True
    similarity_score = eval_single_response_translation("What are the benefits of using cloud services for small businesses?", translated_content)
    assert similarity_score > 0.9

    is_english, translated_content = translate_content("Is it necessary to learn data structures to become a software developer?")
    assert is_english == True
    similarity_score = eval_single_response_translation("Is it necessary to learn data structures to become a software developer?", translated_content)
    assert similarity_score > 0.9

    is_english, translated_content = translate_content("How do I get started with machine learning")
    assert is_english == True
    similarity_score = eval_single_response_translation("How do I get started with machine learning", translated_content)
    assert similarity_score > 0.9

    is_english, translated_content = translate_content("What's the best approach for learning new programming languages quickly?")
    assert is_english == True
    similarity_score = eval_single_response_translation("What's the best approach for learning new programming languages quickly?", translated_content)
    assert similarity_score > 0.9

    is_english, translated_content = translate_content("What are some good resources for learning web development?")
    assert is_english == True
    similarity_score = eval_single_response_translation("What are some good resources for learning web development?", translated_content)
    assert similarity_score > 0.9

    is_english, translated_content = translate_content("How can I protect my data from cyber threats?")
    assert is_english == True
    similarity_score = eval_single_response_translation("How can I protect my data from cyber threats?", translated_content)
    assert similarity_score > 0.9

    is_english, translated_content = translate_content("What is the importance of version control in programming?")
    assert is_english == True
    similarity_score = eval_single_response_translation("What is the importance of version control in programming?", translated_content)
    assert similarity_score > 0.9

    is_english, translated_content = translate_content("Which programming languages are best suited for AI development?")
    assert is_english == True
    similarity_score = eval_single_response_translation("Which programming languages are best suited for AI development?", translated_content)
    assert similarity_score > 0.9

    is_english, translated_content = translate_content("What tools are recommended for managing remote teams effectively?")
    assert is_english == True
    similarity_score = eval_single_response_translation("What tools are recommended for managing remote teams effectively?", translated_content)
    assert similarity_score > 0.9

    is_english, translated_content = translate_content("How does blockchain technology impact data security?")
    assert is_english == True
    similarity_score = eval_single_response_translation("How does blockchain technology impact data security?", translated_content)
    assert similarity_score > 0.9

    is_english, translated_content = translate_content("What are the key skills for a data scientist?")
    assert is_english == True
    similarity_score = eval_single_response_translation("What are the key skills for a data scientist?", translated_content)
    assert similarity_score > 0.9

    is_english, translated_content = translate_content("What's the difference between supervised and unsupervised learning?")
    assert is_english == True
    similarity_score = eval_single_response_translation("What's the difference between supervised and unsupervised learning?", translated_content)
    assert similarity_score > 0.9

    is_english, translated_content = translate_content("How do algorithms work in recommendation systems?")
    assert is_english == True
    similarity_score = eval_single_response_translation("How do algorithms work in recommendation systems?", translated_content)
    assert similarity_score > 0.9

def test_non_english_posts():
    is_english, translated_content = translate_content("¿Cuál es la mejor manera de aprender Python?")
    assert is_english == False
    similarity_score = eval_single_response_translation("What is the best way to learn Python?", translated_content)
    assert similarity_score > 0.9

    is_english, translated_content = translate_content("Quels sont les avantages du cloud computing?")
    assert is_english == False
    similarity_score = eval_single_response_translation("What are the advantages of cloud computing?", translated_content)
    assert similarity_score > 0.9
    
    is_english, translated_content = translate_content("バックアップのベストプラクティスは何ですか？")
    assert is_english == False
    similarity_score = eval_single_response_translation("What are the best practices for backups?", translated_content)
    assert similarity_score > 0.9
    
    is_english, translated_content = translate_content("Как настроить сервер для высокой безопасности?")
    assert is_english == False
    similarity_score = eval_single_response_translation("How to set up a server for high security?", translated_content)
    assert similarity_score > 0.9

    is_english, translated_content = translate_content("Wie lernt man maschinelles Lernen am besten?")
    assert is_english == False
    similarity_score = eval_single_response_translation("What is the best way to learn machine learning?", translated_content)
    assert similarity_score > 0.9

    is_english, translated_content= translate_content( "¿Cómo proteger mis datos en línea?")
    assert is_english == False
    similarity_score = eval_single_response_translation("How can I protect my data online?", translated_content)
    assert similarity_score > 0.9

    is_english, translated_content = translate_content("Quais são os desafios da inteligência artificial?")
    assert is_english == False
    similarity_score = eval_single_response_translation("What are the challenges of artificial intelligence?", translated_content)
    assert similarity_score > 0.9

    is_english, translated_content = translate_content("ما هي أفضل ممارسات الأمان على الإنترنت؟")
    assert is_english == False
    similarity_score = eval_single_response_translation("What are the best practices for online security?", translated_content)
    assert similarity_score > 0.85

    is_english, translated_content = translate_content("Qual è il modo migliore per proteggere i dati?")
    assert is_english == False
    similarity_score = eval_single_response_translation("What is the best way to protect data?", translated_content)
    assert similarity_score > 0.9

    is_english, translated_content = translate_content( "¿Cómo mejorar la productividad en equipos remotos?")
    assert is_english == False
    similarity_score = eval_single_response_translation("How to improve productivity in remote teams?", translated_content)
    assert similarity_score > 0.9

    is_english, translated_content = translate_content("Quels outils sont essentiels pour la gestion de projet?")
    assert is_english == False
    similarity_score = eval_single_response_translation("What tools are essential for project management?", translated_content)
    assert similarity_score > 0.9

    is_english, translated_content = translate_content("どのようにしてデータのセキュリティを向上させますか？")
    assert is_english == False
    similarity_score = eval_single_response_translation("How do you improve data security?", translated_content)
    assert similarity_score > 0.9

    is_english, translated_content = translate_content( "Каковы лучшие методы защиты данных?")
    assert is_english == False
    similarity_score = eval_single_response_translation("What are the best methods for data protection?", translated_content)
    assert similarity_score > 0.9

    is_english, translated_content = translate_content("Comment puis-je améliorer mes compétences en résolution de problèmes?")
    assert is_english == False
    similarity_score = eval_single_response_translation("How can I improve my problem-solving skills?", translated_content)
    assert similarity_score > 0.9

    is_english, translated_content = translate_content("¿Cuál es la importancia del control de versiones?")
    assert is_english == False
    similarity_score = eval_single_response_translation("What is the importance of version control?", translated_content)
    assert similarity_score > 0.9

def test_unintelligible_posts():    
    is_english, translated_content = translate_content("abcd1234!")
    assert is_english == True
    similarity_score = eval_single_response_translation("abcd1234!", translated_content)
    assert similarity_score > 0.9

    is_english, translated_content = translate_content("??¿¿!!??")
    assert is_english == True
    similarity_score = eval_single_response_translation(translated_content, "??¿¿!!??")
    assert similarity_score > 0.9

    is_english, translated_content = translate_content("||| ajfhakdhfkadhfad")
    assert is_english == True
    similarity_score = eval_single_response_translation(translated_content, "||| ajfhakdhfkadhfad")
    assert similarity_score > 0.9

    is_english, translated_content = translate_content("テالأماスト123 abc الأمان")
    assert is_english == True
    similarity_score = eval_single_response_translation(translated_content, "テالأماスト123 abc الأمان")
    assert similarity_score > 0.9

    is_english, translated_content = translate_content(".....!!!???...")
    assert is_english == True
    similarity_score = eval_single_response_translation(translated_content,  ".....!!!???...")
    assert similarity_score > 0.9


# Mock tests
from mock import patch, MagicMock
import pytest

# Test for unexpected language detection
@patch.object(client.chat.completions, 'create')
def test_unexpected_language(mocker):
    # Mock the response to simulate an unexpected message
    mocker.return_value.choices[0].message.content = "I don't understand your request"

    print(translate_content("Hier ist dein erstes Beispiel."))

    # Call the function and assert that the error message is returned
    assert translate_content("Hier ist dein erstes Beispiel.") == (True, INVALID_LANGUAGE_RESPONSE)

# Test for non-string response from language detection
@patch.object(client.chat.completions, 'create')
def test_non_string_response_language(mocker):
    # Mock response to return a non-string type for language detection
    mocker.return_value.choices[0].message.content = 12345  # Non-string response

    # Call the function and check that the error message is returned
    result = translate_content("Hier ist dein erstes Beispiel.")
    assert result == (True, INVALID_LANGUAGE_RESPONSE)

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