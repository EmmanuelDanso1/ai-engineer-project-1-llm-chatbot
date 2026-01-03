# Project 1 - Day1: Leveraging LLM APIs with Python

## Project Overview
This project demonstrates how to leverage **Large Language Model (LLM) APIs** using **Python**, with **OpenAI** as the LLM provider.  
The project is structured to run inside a Python virtual environment to ensure dependency isolation and reproducibility.

---

## Technologies Used
- **Python 3.12**
- **Gemini API**
- **Virtual Environment (venv)**
- **VS Code**

---

## Project Structure

### Create a Virtual Environment
Run the following command in the project root directory:

python -m venv venv

### Activate the Virtual Environment
venv\Scripts\activate

### Installing Dependencies
pip install -r requirements.txt

### Setup with an updated README.md 
- **GEMINI_API_KEY** was set from **GOOGLE STUDIO** platform
- **.env** was placed into **.gitignore** file. This was done to prevent commiting **.env** to github.


## Project 2 - Day2: Building A CLI Chatbot
Leveraging Gemini Chat API. Knowing API is stateless such that it doesn't keep record of chat unless it's being appended.

## CLI Chatbot
Creating a command line interface chatbot to take multimodal user inputs