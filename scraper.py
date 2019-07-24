from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bsoup
from requests import get
my_url = 'https://www.codechef.com/contests'
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
         'Referer': 'https://cssspritegenerator.com',
         'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
         'Accept-Encoding': 'none',
         'Accept-Language': 'en-US,en;q=0.8',
         'Connection': 'keep-alive'}
d = get(my_url, headers=hdr)
# apply BeautifulSoup
soup = bsoup(d.content, 'html.parser')

#  Present Contest
present_contest = soup.find('h3', text='Present Contests').next_sibling.next_sibling.table.tbody

print('Present Contest')
for contest in present_contest.find_all('tr'):
	code = contest.contents[1].string
	name = contest.contents[3].a.string
	start_time = contest.contents[5]['data-starttime']
	#format time
	start_date = contest.contents[5].contents[0]
	end_time = contest.contents[7]['data-endtime']
	#format time
	end_date = contest.contents[7].contents[0]

	print (code + ' ' + name + ' ' + start_time + ' ' + start_date + ' ' + end_time + ' ' + end_date)



#  Upcoming Contests
upcoming_contest = soup.find('h3', text='Future Contests').next_sibling.next_sibling.table.tbody

print('\nUpcoming Contests')
for contest in upcoming_contest.find_all('tr'):
	code = contest.contents[1].string
	name = contest.contents[3].a.string
	start_time = contest.contents[5]['data-starttime']
	#format time
	start_date = contest.contents[5].contents[0]
	end_time = contest.contents[7]['data-endtime']
	#format time
	end_date = contest.contents[7].contents[0]

	print (code + ' ' + name + ' ' + start_time + ' ' + start_date + ' ' + end_time + ' ' + end_date)