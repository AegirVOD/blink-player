def show_result(result):
    i = 1
    search_results = []
    for key in result['result']:
        search_results.append(SearchResult(key))
        print(i, ' : ',  search_results[i - 1].title)
        print(search_results[i - 1].get_url())
        i = i + 1


class SearchResult:

    def __init__(self, result_string):
        self.title = result_string['title']
        self.id = result_string['id']

    def get_url(self):
        return 'https://www.youtube.com/watch?v='+self.id