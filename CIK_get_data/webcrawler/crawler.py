import requests # pip install requests
from bs4 import BeautifulSoup

invalidateCiks = []

def loadDataByCikId(cik, completCIK, completSeries, completClass):
	url = ('https://www.sec.gov/cgi-bin/browse-edgar?scd=series&CIK=%s' % cik)

	response = requests.get(url)
	src = response.content
	soup = BeautifulSoup(src, 'lxml') # pip install lxml

	cikId = None
	cikName = None
	seriesId = None
	seriesName = None

	print('--- loading table of CIK:', cik)
	table = soup.find(lambda tag: tag.name=='table' and not tag.has_attr('width'))
	# i = 0
	if not table:
		invalidateCiks.append(cik)
		print('--------------------- unable to load CIK:', cik)
		return

	for tr in table.find_all('tr'):
		tds = tr.find_all('td')
		if len(tds) == 2: # the CIK row
			if tds[0].has_attr('valign') and tds[0]['valign'] == 'top' and tds[0].find('a'):
				cikId = tds[0].find('a').string
				cikName = tds[1].find('a').string
				print('    gets CIK: ', cikId, cikName)
				completCIK(cikId, cikName)

		elif len(tds) == 3: # the series row
			if tds[1].has_attr('colspan') and tds[1]['colspan'] == '2' and tds[1].find('a'):
				seriesId = tds[1].find('a').string
				seriesName = tds[2].find('a').string
				completSeries(cikId, seriesId, seriesName)

		elif len(tds) >= 4: # the subCat + Name row
			subCat = tds[2]
			name = tds[3]
			subCatStr = None
			nameStr = None
			ticker = None
			if subCat and subCat.find('a') and name:
				subCatStr = subCat.find('a').string
				nameStr = name.string
			if len(tds) == 5:
				ticker = tds[4].string

			if cikId and seriesId and subCatStr and nameStr:
				# print(i)
				# i += 1
				completClass(cikId, seriesId, subCatStr, nameStr, ticker)

