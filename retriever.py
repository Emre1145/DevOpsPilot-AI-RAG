from config import TOP_K_RESULTS

def get_retriever(vector_store):
    retriever = vector_store.as_retriever(
            search_kwargs ={"k":TOP_K_RESULTS}
            )
    return retriever

