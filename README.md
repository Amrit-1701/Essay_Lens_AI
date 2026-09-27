# EssayLens AI

### Intelligent NLP-Based Essay Evaluation and Feedback System

EssayLens AI is a web-based Natural Language Processing (NLP) application that automatically evaluates essays and provides a structured score out of 100 along with detailed feedback.

The system analyzes an essay using multiple linguistic and structural features including content development, topic relevance, organization, grammar and spelling signals, and vocabulary diversity.

---

## Project Overview

EssayLens AI is designed as an academic NLP project that demonstrates how Natural Language Processing techniques can be applied to automated essay evaluation.

The system accepts:

- An essay topic
- An essay written by the user

It then processes the essay and generates:

- Overall score
- Category-wise scores
- Strengths
- Areas for improvement
- Suggestions
- Radar chart
- Linguistic statistics

---

## Main Features

- Essay topic and essay input
- Automatic text preprocessing
- Sentence and word tokenization
- Stop-word filtering
- Content analysis
- Topic relevance analysis
- Organization analysis
- Grammar and spelling analysis
- Vocabulary analysis
- Overall score out of 100
- Category-wise score breakdown
- Strength detection
- Weakness detection
- Automated improvement suggestions
- Radar chart visualization
- Linguistic statistics dashboard
- Interactive web interface
- Flask REST API

---

# Scoring System

EssayLens AI evaluates an essay using five major criteria.

| Evaluation Criterion | Maximum Score |
|---|---:|
| Content | 25 |
| Relevance | 20 |
| Organization | 20 |
| Grammar | 15 |
| Vocabulary | 20 |
| **Total** | **100** |

The final score is calculated as:

```text
Total Score =
Content
+ Relevance
+ Organization
+ Grammar
+ Vocabulary
```

---

# NLP Methodology

## 1. Text Preprocessing

The essay is first processed using NLTK.

The preprocessing pipeline includes:

- Lowercase conversion
- Sentence tokenization
- Word tokenization
- Stop-word filtering
- Alphabetic word filtering
- Whitespace normalization

The preprocessing module prepares the essay for further linguistic analysis.

---

## 2. Content Analysis

Content is evaluated using measurable linguistic and structural features.

The system considers:

- Word count
- Sentence count
- Paragraph count
- Vocabulary diversity
- Introduction presence
- Conclusion presence

A heuristic scoring system converts these features into a score out of 25.

---

## 3. Topic Relevance Analysis

Topic relevance uses a combination of lexical NLP techniques.

### TF-IDF

TF-IDF is used to represent important terms in the essay and the given topic.

### Cosine Similarity

Cosine similarity measures the similarity between the topic representation and essay representation.

### Keyword Coverage

Important words extracted from the topic are compared with words present in the essay.

The final relevance score combines:

```text
TF-IDF Similarity
+
Topic Keyword Coverage
```

The maximum relevance score is 20.

> Note: This implementation uses lexical similarity techniques rather than transformer-based semantic embeddings.

---

## 4. Organization Analysis

Essay organization is evaluated using rule-based structural analysis.

The system considers:

- Number of paragraphs
- Introduction presence
- Body structure
- Conclusion detection
- Sentence distribution
- Paragraph balance
- Transition words
- Essay length

The organization score is calculated out of 20.

---

## 5. Grammar and Language Analysis

EssayLens AI uses TextBlob-based language analysis to identify possible spelling and language errors.

The module considers:

- Sentence count
- Word count
- Possible spelling corrections
- Error rate
- Language accuracy

The grammar/language score is calculated out of 15.

> Note: This is an automated linguistic error approximation and is not intended to replace a complete professional grammar-checking system.

---

## 6. Vocabulary Analysis

Vocabulary quality is analyzed using:

- Total valid words
- Unique words
- Lexical diversity
- Long-word ratio
- Average word characteristics

Lexical diversity is calculated as:

```text
Lexical Diversity =
Unique Words / Total Valid Words
```

The vocabulary score is calculated out of 20.

---

# System Architecture

```text
                         USER
                           |
                           v
                +---------------------+
                |    Web Interface    |
                |     HTML/CSS/JS     |
                +---------------------+
                           |
                           v
                +---------------------+
                |      Flask API      |
                |      /analyze       |
                +---------------------+
                           |
                           v
                +---------------------+
                |  Text Preprocessing |
                |        NLTK         |
                +---------------------+
                           |
             +-------------+-------------+
             |             |             |
             v             v             v
        Content       Relevance     Organization
        Analysis       Analysis       Analysis
             |             |             |
             +-------------+-------------+
                           |
                    +------+------+
                    |             |
                    v             v
                Grammar      Vocabulary
                Analysis      Analysis
                    |             |
                    +------+------+
                           |
                           v
                   Scoring Engine
                           |
                           v
                      Score /100
                           |
                           v
                  Feedback Generator
                           |
                           v
                    Web Dashboard
```

---

# Project Workflow

```text
User enters Topic + Essay
          |
          v
    Text Preprocessing
          |
          v
    Feature Extraction
          |
          +-----------------------------+
          |                             |
          v                             v
   Linguistic Analysis           Topic Analysis
          |                             |
          v                             v
 Content / Grammar /          TF-IDF + Keyword
 Vocabulary / Organization        Coverage
          |                             |
          +-------------+---------------+
                        |
                        v
                  Scoring Engine
                        |
                        v
                  Final Score
                        |
                        v
              Feedback Generation
                        |
                        v
                  Web Dashboard
```

---

# Project Structure

```text
Essay-LensAI/
│
├── backend/
│   ├── analyzer.py
│   ├── evaluator.py
│   ├── features.py
│   ├── feedback.py
│   ├── grammar.py
│   ├── organization.py
│   ├── preprocessing.py
│   ├── semantic.py
│   ├── vocabulary.py
│   └── app.py
│
├── dataset/
│
├── documentation/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── models/
│
├── notebooks/
│
├── venv/
│
├── requirements.txt
│
└── README.md
```

---

# Technologies Used

## Frontend

- HTML5
- CSS3
- JavaScript
- HTML Canvas

## Backend

- Python
- Flask
- Flask-CORS

## NLP and Machine Learning

- NLTK
- TextBlob
- Scikit-learn
- TF-IDF
- Cosine Similarity
- Rule-based linguistic analysis

---

# Installation

EssayLens AI currently runs directly from the local project folder.

## 1. Open the project

```text
D:\Essay-LensAI
```

## 2. Create the virtual environment

```powershell
python -m venv venv
```

## 3. Activate the virtual environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

## 4. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

---

# Running the Application

EssayLens AI uses two terminals:

- Terminal 1 → Flask backend
- Terminal 2 → Frontend web server

---

## Terminal 1 — Start Backend

Run:

```powershell
cd D:\Essay-LensAI
.\venv\Scripts\Activate.ps1
python backend\app.py
```

The backend will run at:

```text
http://127.0.0.1:5000
```

You should see:

```text
ESSAYLENS AI SERVER
Server: http://127.0.0.1:5000
```

---

## Terminal 2 — Start Frontend

Open another PowerShell terminal:

```powershell
cd D:\Essay-LensAI
.\venv\Scripts\Activate.ps1
python -m http.server 5500 --bind 127.0.0.1 --directory frontend
```

The frontend will run at:

```text
http://127.0.0.1:5500/
```

Open that address in your browser.

---

# How to Use

1. Open the EssayLens AI web dashboard.
2. Enter the essay topic.
3. Enter the essay.
4. Click **Analyze Essay**.
5. The frontend sends the data to the Flask API.
6. The backend performs NLP analysis.
7. The scoring engine calculates the five category scores.
8. Feedback is generated.
9. The dashboard displays the final evaluation.

---

# Example Evaluation

### Essay Type: Good Essay

```text
Content:       19 / 25
Relevance:     18.98 / 20
Organization:  20 / 20
Grammar:       14.43 / 15
Vocabulary:    12.31 / 20

Total:         84.72 / 100
```

The system identifies strong performance in content, relevance, organization, and grammar/language while identifying vocabulary diversity as an area that can be improved.

---

# Testing

The system was tested using five different essay types.

| Test | Essay Type | Content | Relevance | Organization | Grammar | Vocabulary | Total |
|---|---|---:|---:|---:|---:|---:|---:|
| 1 | Good Essay | 19 | 18.98 | 20 | 14.43 | 12.31 | **84.72** |
| 2 | Average Essay | 17 | 18.68 | 20 | 14.04 | 11.15 | **80.87** |
| 3 | Poor Essay | 14 | 5.78 | 14 | 12.10 | 8.26 | **54.14** |
| 4 | Off-topic Essay | 19 | 0 | 20 | 14.13 | 12.23 | **65.36** |
| 5 | Very Short Essay | 14 | 6.25 | 8 | 12.86 | 13.29 | **54.40** |

### Testing Observations

The testing demonstrates that:

- Clearly relevant essays receive higher relevance scores.
- A completely unrelated essay receives a relevance score of 0.
- Short and poorly structured essays receive lower organization scores.
- Vocabulary diversity affects the vocabulary score.
- Different evaluation components operate independently.

---

# Advantages

- Automated essay evaluation
- Fast analysis
- Multiple evaluation criteria
- Explainable scoring approach
- Interactive web dashboard
- Visual performance analysis
- Topic relevance detection
- Automated feedback
- Modular backend architecture
- Beginner-friendly and extensible implementation

---

# Limitations

The current system has several limitations:

1. Grammar analysis is not a complete grammar-checking system.
2. Topic relevance depends partly on lexical overlap and TF-IDF representation.
3. Content quality is estimated using heuristic features.
4. The system does not fully understand argument quality or logical reasoning.
5. Creativity and originality are not directly measured.
6. Factual correctness is not verified.
7. Automated scores should be treated as indicators rather than replacements for human evaluation.

---

# Future Scope

Future versions of EssayLens AI can include:

- Transformer-based sentence embeddings
- BERT-based semantic analysis
- Advanced grammar correction
- Semantic argument analysis
- Plagiarism detection
- Sentiment and tone analysis
- Automated topic generation
- Personalized learning recommendations
- Teacher/admin dashboard
- Student progress tracking
- Database integration
- PDF and DOCX essay upload
- Multilingual essay evaluation
- Cloud deployment
- User authentication

---

# Academic Objective

The main objective of EssayLens AI is to demonstrate the practical application of Natural Language Processing techniques for automated written-text evaluation.

The project combines NLP preprocessing, linguistic feature extraction, lexical similarity analysis, rule-based structural analysis, scoring, and automated feedback within a complete web application.

---

# Conclusion

EssayLens AI demonstrates how Natural Language Processing can be integrated into a practical essay evaluation system.

The application combines:

- NLTK-based preprocessing
- Linguistic feature extraction
- TF-IDF-based topic relevance
- Keyword coverage
- Rule-based organization analysis
- TextBlob-based language analysis
- Vocabulary analysis
- Automated scoring
- Feedback generation
- Interactive visualization

The resulting system provides students with a structured overview of their essay performance and highlights areas that can be improved.

The project also demonstrates the integration of a Python Flask backend with an HTML, CSS, and JavaScript frontend to create an end-to-end NLP application.

---

# Project Status

```text
NLP Preprocessing       ✓ Completed
Feature Extraction      ✓ Completed
Content Analysis        ✓ Completed
Relevance Analysis      ✓ Completed
Organization Analysis   ✓ Completed
Grammar Analysis        ✓ Completed
Vocabulary Analysis     ✓ Completed
Scoring Engine          ✓ Completed
Feedback System         ✓ Completed
Flask API               ✓ Completed
Web Dashboard           ✓ Completed
Radar Visualization     ✓ Completed
Testing                 ✓ Completed
Documentation           → In Progress
PPT                     → Planned
Viva Preparation        → Planned
```

---

# Author

**EssayLens AI**

NLP Academic Project

---

# License

This project is developed for educational and academic purposes.