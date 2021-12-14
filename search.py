from youtubesearchpython import VideosSearch

def by_keyword(keyword):
    search = VideosSearch(keyword, limit = 5)
    response = search.result()
#    print(response)
    return response
