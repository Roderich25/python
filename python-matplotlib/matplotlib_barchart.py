# import csv
import pandas
from collections import Counter
from matplotlib import pyplot

pyplot.style.use('fivethirtyeight')
language_counter = Counter()

# with open('data.csv') as csv_file:
#    csv_reader = csv.DictReader(csv_file)
# for row in csv_reader:
# language_counter.update(row['LanguagesWorkedWith'].split(';'))

data = pandas.read_csv('data_barchart.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']
for response in lang_responses:
    language_counter.update(response.split(';'))

languages = []
popularity = []
for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])
languages.reverse()
popularity.reverse()

pyplot.barh(languages, popularity)
pyplot.title('Most popular programming languages')
pyplot.xlabel("People who use it")
pyplot.tight_layout()
pyplot.savefig('barchart.png')
pyplot.show()
