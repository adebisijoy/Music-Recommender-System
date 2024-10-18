# Song Recommendation System

This project was built as part of the Skill Harvest Training, utilizing natural language processing (NLP) techniques and cosine similarity to recommend songs to users based on their preferences.

## Project Overview
The system recommends songs by analyzing the textual content of the song lyrics. It processes a large dataset and generates song recommendations using **TF-IDF** vectorization and **Cosine Similarity**.

## Dataset
- **Size**: 57,650 rows
- **Columns**: Artist, Song, and Text
- The **Link** column was dropped to focus on the relevant text features.
- A sample of **15,000 rows** was selected for computational efficiency.

## Preprocessing Steps
1. **Dropping Columns**: The 'Link' column was removed.
2. **Text Cleaning**: Cleaned the text data using regular expressions.
3. **Tokenization and Stemming**: 
   - Tokenized the text.
   - Applied stemming using **PorterStemmer** to reduce words to their root forms.

## Model and Techniques
- **TF-IDF Vectorization**: 
   - Converted the song lyrics into numerical vectors based on term frequency and inverse document frequency (TF-IDF).
- **Cosine Similarity**: 
   - Computed the similarity between songs based on the TF-IDF vectors.
   - Songs with higher similarity scores were recommended to users.



Additionally, the system was validated using **user feedback** and was found to perform well in terms of both recommendation quality and computational efficiency.

## Author
- **Name**: Adebisi Joy Ebubechi
- **Email**: adebisijoy24@gmail.com
- **Role**: Data Scientist
- **Phone**: +2348028912360
- **Portfolio Projects**: [Link to Portfolio] (Optional)

## Technologies Used
- **Python**
- **Natural Language Processing (NLP)**
- **TF-IDF**
- **Cosine Similarity**

## How to Run the Project
1. Clone the repository: 
   ```bash
   git clone [repository-url]
