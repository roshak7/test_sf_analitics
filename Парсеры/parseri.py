import requests, json

url = input('url: ')
headers = {
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
		'x-youtube-client-name': '1',
		'x-youtube-client-version': '2.20200429.03.00',
		}
token_page = requests.get(url, headers=headers)
nextDataToken = token_page.text.split('"nextContinuationData":{"continuation":"')[1].split('","')[0]
sleep = False #Цикл будет завершен, когда не будет токенов
ids = []
while not sleep:
	service = 'https://www.youtube.com/browse_ajax'
	params = {
	"ctoken": nextDataToken,
	"continuation": nextDataToken
	}
	r = requests.post(service, params=params, headers=headers)
	r_json = r.json()[1]
	r_jsonResponse = r_json['response']
	dataContainer = r_jsonResponse["continuationContents"]["playlistVideoListContinuation"]
	try: #пробуем найти токен
		nextDataToken = dataContainer["continuations"][0]["nextContinuationData"]["continuation"]
	except:
                #токен не найден. Значит, далее запроса не будет. Остается собрать оставшийся контент
		sleep = True
	for content in dataContainer["contents"]:
		videoId = content['playlistVideoRenderer']['videoId']
		ids.append(videoId)