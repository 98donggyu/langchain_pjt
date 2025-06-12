from networkx import hits
import meilisearch
import pandas as pd

client = meilisearch.Client('http://localhost:7700', 'aSampleMasterKey')

def search_company(query):
    return client.index('nasdaq').search(query)

class SearchResult:
    def __init__(self, item):
        self.item = item

    @property    
    def symbol(self):
        return self.item['Symbol']
    
    @property
    def name(self):
        return self.item['Name']
    
    def __str__(self):
        return f"{self.symbol}: {self.name}"

if __name__ == "__main__":
    # symbol = "Apple"
    # company_info = search_company(symbol)
    # print(company_info['hits'])
    hits = search_company['hits'] 
    # result = [] 
    # for hit in hits:
    #     print(SearchResult(hit))
    #     result.append(SearchResult(hit))
    search_results = [SearchResult(hit) for hit in hits]
    print(search_results[0])
    