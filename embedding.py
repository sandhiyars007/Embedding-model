from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-mpnet-base-v2")

sentences = [
    "I enjoy coding in Python.",
    "I love programming in Python.",
    "Python is my favorite programming language.",
    "The weather is very hot today.",
    "It is raining heavily outside.",
    "I went to college this morning.",
    "My college has many computer science students."
]

embeddings = model.encode(sentences)

print("Total sentences:", len(sentences))
print("Embedding dimension:", len(embeddings[0]))

similarity = cosine_similarity(embeddings)

print("\n--- Similar Sentences ---")

for i in range(len(sentences)):
    for j in range(i + 1, len(sentences)):
        if similarity[i][j] > 0.7:
            print("\nSentence 1:", sentences[i])
            print("Sentence 2:", sentences[j])
            print("Similarity:", round(similarity[i][j], 4))