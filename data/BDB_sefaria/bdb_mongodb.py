from bs4 import BeautifulSoup
import re

with open('BDB_dict.html') as fp:
    html = fp.read()

# Fusionne les </p><p> qui ne sont pas le début d'une nouvelle entrée
html = re.sub(r'</p>\s*<p>(?!<span>\d+:)', ' ', html)

soup = BeautifulSoup(html, features='html.parser')

ps = soup.find_all('p')
with_page = [p for p in ps if p.find('span') and re.match(r'^\d+:$', p.find('span').text.strip())]
print(f"Total p : {len(ps)}")
print(f"Avec numéro de page : {len(with_page)}")
print(f"Sans numéro de page : {len(ps) - len(with_page)}")

without_page = [p for p in ps if not (p.find('span') and re.match(r'^\d+:$', p.find('span').text.strip()))]
for p in without_page:
    print(f"* {p.text[:80]}\n")
"""    

# Select only dicitonary entries on strogs-number
entries = []
for p in ps:
    if p.find('span', class_='strongs-number'):
        entries.append(p)



#Pour chaque entrée, sélectionne les champ du dictionnaire
# for p in entries:
#     page = p.find('span').text.strip().rstrip(':')
    
"""