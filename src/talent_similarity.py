# use the query keywords and transform into vectors using a tfidf vectorizer
vectorizer = TfidfVectorizer(stop_words='english', ngram_range = (1, 2))
docs_tfidf = vectorizer.fit_transform(df["job_title"])
query1 = "Aspiring human resources"
query2 = "seeking human resources"
query1_tfidf = vectorizer.transform([query1])
query2_tfidf = vectorizer.transform([query2])

# Use cosine similarity to find matching job descriptions based on the transformed queries
cosine_similarities1 = cosine_similarity(query1_tfidf, docs_tfidf).flatten()
cosine_similarities2 = cosine_similarity(query2_tfidf, docs_tfidf).flatten()
combined_similarities = (cosine_similarities1 + cosine_similarities2) / 2
df['fit'] = combined_similarities
df_sorted = df.sort_values('fit', ascending=False)
df_sorted[['job_title', 'fit']].head(10)