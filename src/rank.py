# Rank the candidates based on fit
df["rank"] = df["fit"].rank(ascending=False)

df_sorted = df.sort_values('rank', ascending=True)

# Re-rank candidates after starring the 7th candidate
starred_candidiate_id = 7
df_sorted.loc[starred_candidiate_id, "rank"] = 1
df_sorted.sort_values(by="rank", inplace=True)