from youtubesearchpython import VideosSearch

def by_keyword(keyword):
    search = VideosSearch(keyword, limit = 2)
    response = search.result()
#    print(response)
    return response
