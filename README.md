# Sentiment Analysis and Natural Language Processing for Marketing

I'm keeping my documents/source codes related to this Manning liveProject in my GitHub account [here](https://github.com/longlivewama).

---

## Project Summary

In this liveProject, you will gain an overall impression of the job of a Natural Language Processing (NLP) Specialist working on the Growth Hacking Team of a freshly launched startup introducing a new video game to the market.  

One of the key targets of a growth hacking team is to drive rapid growth for early startups. This often involves strategies to acquire as many customers as possible at the lowest cost. As part of the strategy, your boss wants to map the video game market to understand how customers evaluate competitors’ products — namely, what they **like** and **dislike** in a video game.  

Knowing what makes a video game attractive to gamers helps the marketing team craft a more effective product message. To achieve this, you will dive into customer reviews to extract insights using various NLP methods.

---

## Tasks as an NLP Specialist

Your main responsibilities in this project include:

- Download the dataset of Amazon reviews.  
- Create a filtered dataset for video game reviews.  
- Assign a sentiment score between **-1** and **1** to each review.  
- Compare sentiment scores with star ratings to evaluate accuracy.  
- Experiment with multiple sentiment analysis methods.  
- Classify reviews as **Positive**, **Negative**, or **Neutral**.  
- Summarize findings to highlight what gamers like or dislike about video games.

---

## Techniques Employed

To deeply understand gamers’ opinions, the project uses:

- **Imbalanced Dataset Sampling** – with the `imbalanced-learn` package.  
- **Dictionary-based Sentiment Analysis** – using NLTK sentiment tools.  
- **Model Evaluation** – via scikit-learn metrics.  
- **Neural Network-based Analysis** – using the **DistilBERT** model with PyTorch, transformers, and simpletransformers.  
- **Data Visualization** – via Altair to show key “liked” and “disliked” terms.  
- **Interactive Web Application** – powered by **Streamlit** for real-time sentiment analysis.  

---

## Project Outline

1. **Creating Your Dataset**  
2. **Dictionary-based Sentiment Analyzer**  
3. **Evaluator for Dictionary-based Analyzer**  
4. **Neural Network-based Sentiment Analyzers**  
5. **Reporting and Visualization**  
6. **Interactive Streamlit Demonstration**

---

## Dataset

The Amazon review dataset can be downloaded from [here](https://nijianmo.github.io/amazon/index.html).  
Use the **Video Games 5-core** JSON file from *Small subsets for experimentation*.  

---

## Additional Work: Interactive Sentiment Analyzer with Streamlit

An interactive **Streamlit** application was added to make the project more engaging and accessible for both technical and non-technical audiences.  

**Live Demo Features**:
- Real-time sentiment analysis of text.  
- Interactive gauge charts showing sentiment scores.  
- Sample reviews for quick testing.  
- Rule-based sentiment classification.  
- Mobile-friendly interface.  

---

### Running the Streamlit Application Locally

1. Install Python (3.8+ recommended).  
2. Clone the repository:  
   ```bash
   git clone https://github.com/longlivewama/sentiment_analysis_project.git
   cd sentiment_analysis_project
