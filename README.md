# Embedding-model


A simple Python project that demonstrates how to generate sentence embeddings using SentenceTransformers and compare sentences using cosine similarity.

## About the Project

This project uses the `all-mpnet-base-v2` model from SentenceTransformers to convert sentences into numerical vector representations called embeddings.

Cosine similarity is then used to measure how semantically similar the sentences are.

## Features

- Generates sentence embeddings
- Uses a pre-trained SentenceTransformer model
- Calculates cosine similarity between sentences
- Identifies highly similar sentence pairs
- Displays the embedding dimension
- Simple and beginner-friendly implementation

## Technologies Used

- Python
- SentenceTransformers
- Scikit-learn
- Cosine Similarity

## Project Structure

```text
Embedding-model/
│
├── embedding.py
├── README.md
├── Output 1.png
└── Output 2.png
```

## How It Works
1. Load the Embedding Model

The project loads the pre-trained all-mpnet-base-v2 model.

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-mpnet-base-v2")

2. Provide Sentences

The program contains a list of sample sentences related to programming, weather, and college.

3. Generate Embeddings

Each sentence is converted into a numerical vector:

embeddings = model.encode(sentences)

4. Calculate Similarity

Cosine similarity is calculated between the generated embeddings:

from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(embeddings)

5. Find Similar Sentences

The program checks sentence pairs and displays pairs whose similarity score is greater than 0.7.

Sample Output
Total sentences: 7
Embedding dimension: 768

## --- Similar Sentences ---

Sentence 1: I enjoy coding in Python.
Sentence 2: I love programming in Python.
Similarity: 0.xxxx

The exact similarity values may vary depending on the model version and environment.

## Applications

Sentence embeddings and semantic similarity can be used in:

Semantic search
Document similarity
Duplicate sentence detection
Recommendation systems
Question-answer matching
Text clustering
Natural Language Processing (NLP)

## Future Enhancements
Add user input for custom sentences
Display similarity scores in a table
Add a Streamlit interface
Compare multiple embedding models
Add semantic search functionality
Visualize embeddings using PCA or t-SNE

## Author

Sandhiya R
