# Project 1 - Day1: Leveraging LLM APIs with Python

## Project Overview
This project demonstrates how to leverage **Large Language Model (LLM) APIs** using **Python**, with **GEMINI** as the LLM provider.  
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


## Project 3 - Day 3: Tokenization and Context Management
Tokens are the fundamental unit of cost and context for LLMs. An AI Engineer must master token counting to manage API costs, prevent context window overflow, and optimize the efficiency of every API call.

- **Tokenization and Token counting**
- **Maximum Tokens and Context Length**
- **Context Management Stragtegies**

## Project 4- Day 4: System Prompt
The System Prompt is the most powerful tool an AI Engineer has to define the model's persona, constraints, and instructions, fundamentally changing its output without retraining.

- **Defining persona and constraints**
- **Controlling creativity with Temperature**
- **Controlling diversity with top_p**

## Project 5 - Day 5: Prompting Techniques
Prompting techniques using Zero-shot, Few-shot and Chain of Thought to check the state of prompting.

- ## Zero-Shot prompting
The model is asked to do a task without being given any examples.
It relies entirely on what it already learned during training.

- ## Few-shot prompting
The model is given a few examples (usually 1–5) to show how to do the task before answering a new one.

- ## Chain of thoughts
The model is encouraged to reason step-by-step before giving the final answer.
This improves performance on logic, math, and multi-step reasoning problems.