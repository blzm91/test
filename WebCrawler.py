from requests import get

headers = {"Accept-Language": "en-US, en;q=0.5"}
url = 'http://glaw.scourt.go.kr/wsjo/panre/sjo100.do?contId=2251456&q=*&nq=&w=panre&section=panre_tot&subw=&subsection=&subId=1&csq=&groups=6,7,5,9&category=&outmax=1&msort=d:1:1&onlycount=&sp=&d1=&d2=&d3=&d4=&d5=&pg=2&p1=&p2=&p3=&p4=&p5=&p6=&p7=&p8=0,1&p9=&p10=&p11=&p12=&sysCd=WSJO&tabGbnCd=&saNo=&joNo=&lawNm=&hanjaYn=N&userSrchHistNo=&poption=&srch=&range=&daewbyn=N&smpryn=N&tabId='


response = get(url)

from bs4 import BeautifulSoup

html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)

page = html_soup.find_all('div', class_ = 'container')

#first = page[0]
#print(first)
#first_year = first_movie.h3.find('span', class_ = 'lister-item-year text-muted unbold')






# Lists to store the scraped data in
abstract = []
years = []
imdb_ratings = []
metascores = []
votes = []
