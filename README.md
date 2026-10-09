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

## ⚙️ Installation

### Prerequisites

- Python 3.10 or later.
- A GitHub account to clone the repository.
- A Kaggle account to run the AI backend notebook.
- An Ngrok account and authentication token to expose the backend API during development.

### 1. Clone the Repository

git clone YOUR_GITHUB_REPOSITORY_URL
cd ArtSense

Replace `YOUR_GITHUB_REPOSITORY_URL` with the URL of your ArtSense GitHub repository.

Alternatively, download the repository as a ZIP file from GitHub and extract it.

### 2. Install Frontend Dependencies

Open a terminal in the project directory and run:

python -m pip install streamlit requests

These packages are required to run the Streamlit interface and send requests to the AI backend.

### 3. Set Up the AI Backend

1. Open `artsense.ipynb` in Kaggle.
2. Enable GPU acceleration in the notebook settings if available.
3. Run the notebook cells in order to load the movie dataset, generate embeddings, build the FAISS index, and initialize the language model.
4. Install and configure FastAPI, Uvicorn, and Pyngrok as required by the notebook.
5. Configure your Ngrok authentication token securely.
6. Start the FastAPI server and create an Ngrok tunnel.
7. Copy the generated public API endpoint.

**Important:** The Kaggle notebook and Ngrok tunnel must remain active while using this development setup. Availability depends on Kaggle session limits and the tunnel connection.

### 4. Configure the Frontend

Open `app.py` and configure `API_URL` to point to the active backend endpoint, including the `/recommend` path.

Configure the required API authentication on both the frontend and backend. Do not commit API keys or Ngrok tokens to a public repository.

---

## 🚀 Usage

### 1. Start the AI Backend

Open `artsense.ipynb` in Kaggle and run the required cells in order. Wait until the FastAPI server starts and the Ngrok public endpoint is displayed.

### 2. Launch the Web Application

On your computer, open a terminal in the ArtSense project directory and run:

python -m streamlit run app.py

Streamlit will display a local URL in the terminal. Open that URL in your browser.

### 3. Generate Recommendations

1. Enter a creative idea, story concept, or scenario in the input field.
2. Click **Recommend Movies**.
3. ArtSense sends your idea to the backend.
4. The backend retrieves semantically similar movies and uses the language model to generate structured recommendations with explanations.
5. Review the recommended movies and why they match your idea.

### Example Input

"A group of friends trapped in an abandoned place where something dangerous is hunting them."

### Expected Output

ArtSense returns a list of relevant movie recommendations, each accompanied by an explanation of how it relates to the submitted idea.

**Note:** This setup is intended for development and demonstration. The application is not permanently available when the Kaggle session or Ngrok tunnel stops.
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
