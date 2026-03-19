def research_agent(vector_store, query):

    docs = vector_store.similarity_search(query)

    return docs