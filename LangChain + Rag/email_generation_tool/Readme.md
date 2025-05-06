
# 📨 Job Scraper & Cold Email Generator

This project automates the process of scraping job descriptions from company websites, extracting structured job data, querying relevant past projects from a portfolio, and generating personalized cold emails tailored to each opportunity using a powerful LLM (LLaMA-3.3-70B via Groq).

## 🚀 Features

- 🔍 **Web Scraping**: Scrapes job postings from career pages using `WebBaseLoader`.
- 🧠 **LLM Integration**: Uses LLaMA-3.3-70B via `ChatGroq` for intelligent extraction and email generation.
- 📊 **Job Embedding Storage**: Stores job-related tech stacks using `ChromaDB` for semantic querying.
- 📬 **Cold Email Generator**: Crafts high-quality, personalized outreach emails in the voice of a BDE at Company.
- 🧪 **Gradio Interface**: User-friendly interface to input job URLs and generate emails with a click.

## 🛠️ Tech Stack

- **Python**
- **ChromaDB**
- **ChatGroq (LLaMA-3.3-70B)**
- **LangChain**
- **Gradio**
- **Pandas**

## 📌 How It Works

1. Scrapes the job posting from a company career page.
2. Uses an LLM to extract structured JSON data from the posting.
3. Queries relevant portfolio projects from `ChromaDB` using extracted skills.
4. Generates a cold email using the job context and portfolio data.
5. Displays the email via Gradio UI.

## 📤 Sample Use Case

1. Input job URL (e.g., a Nike software engineering role).
2. The model extracts fields like `role`, `skills`, `experience`, `description`.
3. The system finds similar projects company has done.
4. Generates an email 

