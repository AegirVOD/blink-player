def show_result(search_results):
    i = 1
    for line in search_results:
        print(i, ' : ', line.title)
        print(line.get_url())
        i = i + 1
