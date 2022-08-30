from search_engines import Google

engine = Google()
query = input("Enter Query: ")
results = engine.search(query)
links = results.links()

print(links)