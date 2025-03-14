"""Summarizer class that contains the main logic."""

import os

import json

from dotenv import load_dotenv

from openai import OpenAI

from web_summarizer.prompts import PROMPT

import requests

from bs4 import BeautifulSoup

class Summarizer:
    """Summarizer using OpenAI API."""
    
    def __init__(self):
        load_dotenv()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
    def summarize_web(
        self,
        web_url:str,
        style:str = "formal",
    ) -> str:
        """Summarize a web page.

        Args:
            web_url (str): web from the website.
            style (str, optional): summarize style. Defaults to "formal".

        Returns:
            str: A summarize of the web page.
        """
        
        # Obtains the plain text from the url.
        web_text = self.extract_web_info(url=web_url)
        
        # We make a json for the llm call
        json_data = json.dumps({"text": web_text, "style": style})
        
        # Call the llm to summarize the text
        response = self.call_llm(web_text=json_data)
        
        return response
        
        
    def call_llm(
        self,
        web_text:str,
        model:str="gpt-4o-mini",
        temperature:float=0.3      
    ) -> str:
        """Calls the OpenAI API to make a summarize from a web page.

        Args:
            web_text (str): Web text to summarize
            model (str, optional): Set the model from the OpenAI models availables. Defaults to "gpt-4o-mini".
            temperature (float, optional): Set the temperature model. Defaults to 0.3.

        Returns:
            str: Returns the summarize from the web page.
        """
        
        messages = [
            {"role": "user", "content": PROMPT.format(input=web_text)}
        ]
        
        response=self.client.chat.completions.create(
            messages=messages,
            model=model,
            temperature=temperature
        )
        
        return (response.choices[0].message.content)
    
    def extract_web_info(
        self,
        url:str
    ) -> str:
        """Extract with BeautifulSoup the text info from an url.

        Args:
            url (str): Url from the website.

        Returns:
            str: returns the plain text with the information of the website.
        """
        
        html_text=requests.get(url=url)
        
        if html_text.status_code == 200:
            soup = BeautifulSoup(html_text.text, "html.parser")
        else:
            print(f"Error al obtener la página: {html_text.status_code}")
            
        return soup.get_text(separator="\n", strip=True)
        
        
        
