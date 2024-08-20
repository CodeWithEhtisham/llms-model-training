import chromadb
chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="shami")
collection.add(
    documents=[
        "My name is ehtisham",
        "i'm computer science student",
        "my friend name is shami",
    ],
    ids=["id1", "id2","id3"]
)
results = collection.query(
    query_texts=["what is my name"], # Chroma will embed this for you
    n_results=2 # how many results to return
)
print(results)