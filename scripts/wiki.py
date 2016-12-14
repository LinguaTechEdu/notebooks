import requests
import pprint

user_agent = 'MyPyMusicBot/1.0 (http://example.com/MyPyNusicBot/; MyPyMusicBot@example.com) MyPyMusicBot/1.0'

s = requests.Session()
s.headers.update({'User-Agent': user_agent})

r = requests.get('https://en.wikipedia.org/w/api.php?action=parse&pageid=736&format=json&titles=Albert+Einstein')

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(r.content)
