import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

pattern1 = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
matches = pattern1.finditer(text_to_search)
for match in matches:
    print(match)


pattern2 = re.compile(r'\d{3}.\d{3}.\d{4}')
with open('data.txt', 'r') as f:
    contents = f.read()
    matches = pattern2.finditer(contents)
    for match in matches:
        print(match.group())
        
urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern3 = re.compile(r'https?://(www\.)?(\w+)(\.\w+)', re.I) # flag re.I ignores case
subbed_urls = pattern3.sub(r'\2\3', urls)
print(subbed_urls)        