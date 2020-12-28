def show_result(result):
    i = 1
    for key in result['result']:
        print(i, ' : ',  key['title'])
        print('https://www.youtube.com/watch?v=' + key['id'])
        i = i + 1
