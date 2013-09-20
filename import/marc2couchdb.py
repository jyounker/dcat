#aka marc2json
import couchdb
from pymarc import MARCReader


marc_decoded = {
  '001' : 'BIBID',
  '005' : 'Last_updated',
  '020' : 'ISBN',
  '022' : 'ISSN',
  '050' : 'Call#',
  '099' : 'Call#',
  '100' : 'Author',
  '110' : 'Corporate',
  '111' : 'Conference',
  '130' : 'Uniform_title',
  '240' : 'Uniform_title',
  '245' : 'Title_proper',
  '246' : 'Subtitle',
  '250' : 'Edition',
  '260' : 'Publishing_info',
  '300' : 'Details',
  '440' : 'Series',
  '490' : 'Series',
  '500' : 'Notes',
  '504' : 'Notes',
  '505' : 'TOC',
  '511' : 'Participants',
  '520' : 'Description',
  '530' : 'Notes',
  '590' : 'Notes',
  '600' : 'Subject',
  '610' : 'Subject',
  '611' : 'Subject',
  '650' : 'Subject',
  '651' : 'Subject',
  '655' : 'Genre',
  '700' : 'Person',
  '710' : 'Additional_Corporate_Author',
  '740' : 'Subtitle',
  '856' : 'URL',
  '930' : 'Holdings',
  '970' : 'TOC',
}
server = couchdb.Server()
db = server['brock']
filename = 'March25'
fd = open(filename, 'rU')
reader = MARCReader(fd, to_unicode=True)
cnt = 0
for r in reader:
  if cnt % 1000 == 0:
    print cnt
  cnt += 1
  marcjson = {}
  for f in r.get_fields():
    if marc_decoded.has_key(f.tag):
      field = marc_decoded[f.tag]
      marcjson.setdefault(field, [])
      marcjson[field].append(f.value().rstrip(' .-,;:'))
  #print marcjson
  db.save(marcjson)
