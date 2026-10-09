# 🚀 [Tips Hindawi](https://www.tipshindawi.com/) Internship (August–October) 2026

> 🎓 This project was built during the [ **Tips Hindawi** ](https://www.tipshindawi.com/) **Internship (August–October) 2026**.

## 👤 Participant

| Field            | Value                                |
| ---------------- | ------------------------------------ |
| Full Name        |Youssef Mohamed Abdel-Fattah|
| Project Name     |ArtSense|
| GitHub Username  |youssif-elsoufy|
| Internship Batch | August–October 2026|
| Training Program | Large Language Models (LLMs) Program |
| Organization     | [**Edrak for Ai**](https://edrak4ai.com/en)                         |

---

# 🎨 ArtSense — AI-Powered Creative Recommendation System

## 📖 Project Overview

ArtSense is an AI-powered recommendation system that helps users discover movies and other creative works based on their own ideas and descriptions.

Using Retrieval-Augmented Generation (RAG), Sentence Transformers, FAISS vector search, and a Mistral language model, ArtSense retrieves semantically similar works and generates personalized recommendations with explanations.

The project currently focuses on movie recommendations, with future plans to support books, plays, and other creative works.
---

✨ Features

💡 Idea-Based Recommendations: Discover movies by describing your own ideas.

🔎 Semantic Search: Find movies based on meaning and context, not just keywords.

🧠 AI-Generated Explanations: Understand why each recommended movie matches your idea.

📚 Retrieval-Augmented Generation (RAG): Combines movie retrieval with language model generation.

⚡ Vector Search: Uses FAISS to efficiently search movie embeddings.

🖥️ Interactive Web Interface: Enter your idea and view recommendations through Streamlit.

---

🛠️ Technologies Used

Python — Core programming language.

Streamlit — Interactive user interface.

Hugging Face Transformers — Language model loading and text generation.

Sentence Transformers — Semantic text embeddings using all-MiniLM-L6-v2.

FAISS — Vector similarity search.

LangChain — Prompt templates and structured output parsing.

FastAPI — Backend API for processing recommendation requests.

Ngrok — Temporary public tunnel for accessing the development API.

Pandas & NumPy — Data processing and numerical operations.

TMDB 5000 Movies Dataset — Movie information used for retrieval.

---

⚙️ Installation

Prerequisites

Python 3.10 or later.

pip package manager.

Access to the project files and the required model resources.

1. Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL
cd CineMatch

Replace YOUR_GITHUB_REPOSITORY_URL with your repository's actual URL.

2. Create a virtual environment (optional)

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

3. Install dependencies

pip install streamlit requests

The AI backend requires additional dependencies and a compatible environment. Refer to the notebook for the backend setup.

4. Configure the backend URL

Update the API_URL in app.py to point to your running FastAPI endpoint.

Configure any required API keys securely. Do not commit API keys, authentication tokens, or other secrets to GitHub.

---

🚀 Usage

Start the AI backend and make its API endpoint accessible.

Set the correct backend URL and authentication configuration in app.py.

Open a terminal in the project directory.

Run the Streamlit application:

python -m streamlit run app.py

Open the local URL displayed in the terminal.

Describe a movie idea, story, or situation in the input field.

Click Recommend Movies to receive relevant movie suggestions and explanations.

Example input:

A group of friends trapped in an abandoned place where something dangerous is hunting them.

---

# 📸 Demo

<img width="1438" height="736" alt="image" src="https://github.com/user-attachments/assets/7c973680-6eb8-4e63-819e-a2b6e47e39c4" />
<img width="1440" height="721" alt="image" src="https://github.com/user-attachments/assets/f2a00853-969d-44c1-abac-440e3ce22878" />
<img width="1437" height="726" alt="image" src="https://github.com/user-attachments/assets/495e7f14-988a-4aab-87f5-6d1853ca09e6" />

---

📈 Results

Processed a dataset containing 4,803 movies.

Generated 384-dimensional semantic embeddings using all-MiniLM-L6-v2.

Built a FAISS index for similarity-based movie retrieval.

Integrated semantic retrieval with a Mistral language model.

Used LangChain's PromptTemplate and StructuredOutputParser to generate structured recommendations.

Connected the recommendation pipeline to a Streamlit interface through a FastAPI backend.

---

🔮 Future Improvements

🌐 Deploy the application online with a stable public URL.

📚 Expand the system to recommend books, plays, and other creative works.

🎯 Improve recommendation relevance and ranking.

💾 Add user accounts and saved recommendations.

🎨 Enhance the interface and display movie posters and additional metadata.

🔐 Improve backend authentication and API security.

⚡ Optimize model inference and response time.

---

# 📚 About the Internship

This project was developed as part of the [**Tips Hindawi**](https://www.tipshindawi.com/) **Internship (August–October) 2026**, and it will be showcased on the official [Tips Hindawi](https://www.tipshindawi.com/) website.

[Tips Hindawi](https://www.tipshindawi.com/) is the internships department of [**Edrak for Ai**](https://edrak4ai.com/en), and the internship encourages participants to build real-world projects, apply practical skills, and showcase their work through GitHub.

For more information about the internship, training programs, and upcoming batches, visit the official [Tips Hindawi](https://www.tipshindawi.com/) website.

---

# 📄 License

This project is shared for educational and portfolio purposes.
