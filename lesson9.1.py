import requests


reponse = requests.get('https://coinmarketcap.com/')
reponse_text = reponse.text
'''
res = []
reponse_parse = reponse_text.split('<span>')
for parse_elem1 in reponse_parse:
    if parse_elem1.startswith('$'):
        for parse_elem2 in parse_elem1.split('</span>'):
            if parse_elem2.startswith('$') and parse_elem2[1].isdigit():
                res.append(parse_elem2)
print('Bitcoin value:', res[0])
'''

if reponse.status_code == 200:
    soup = BeautifulSoup(reponse_text,
                         features='html.parser')

    soup_list = soup.find_all('a',
                              {'href': '/currencies/bitcoin/markets/'})
    res = soup_list[0].find('span')
    print(res.text)