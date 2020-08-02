import glob
from bs4 import BeautifulSoup
from pathlib import Path

# 再帰的に全htmlをリストで取得する
p = Path("./")
targets = list(p.glob("**/*.html"))

# 取得したhtmlに対して、所定の要素を追加する
for target in targets:
    content = ""
    for i in range(str(target).count('\\')):
        content += "../"
    content += "test.js"
    print(content)
    soup = BeautifulSoup(open(target), "xml")
    ret = soup.new_tag('script', src=content)
    soup.find('head').append(ret)
    with open(target, mode='w', encoding = 'utf-8') as fw: fw.write(soup.prettify())
