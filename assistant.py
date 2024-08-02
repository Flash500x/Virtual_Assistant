import speech_recognition as sr
import pyttsx3
import os
import openai
openai.api_key = OPENAI_KEY   
from dotenv import load_dotenv
load_dotenv()
OPENAI_KEY = os.getenv('OPENAI_KEY')








































messages = []#array to store message history
while(True):
    text = record_text()#function to record user's text
    messages.append({"role":"user", "content":text})#the received text for the mic is stored in the form of a dictionary
    response = send_to_chatGPT(messages)#chatGPT has access to all previous messages
    SpeakText(response)#the messages(dictionary)is spoken out
    print(response)