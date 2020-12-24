def show_result(result):
    i = 1
    for key in result['items']:
        print(i, ' : ',  key['snippet']['title'])
        print('https://www.youtube.com/watch?v=' + key['id']['videoId'])
        i = i + 1
