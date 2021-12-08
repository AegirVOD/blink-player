def parse_result(result):
    search_results = []
    for key in result['result']:
        search_results.append(SearchResult(key))
    return search_results


class SearchResult:

    def __init__(self, result_string):
        self.title = result_string['title']
        self.id = result_string['id']

    def get_url(self):
        return 'https://www.youtube.com/watch?v=' + self.id
