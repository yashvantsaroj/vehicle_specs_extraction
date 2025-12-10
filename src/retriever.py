


def retrieve(query, vdb, k=5):
    return vdb.search(query, top_k=k)
