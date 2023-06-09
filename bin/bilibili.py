import requests,re
from lxml import etree

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }
url = "https://rec.danmuji.org/dev/bilibili-cdn/"
pattern = r"(.+bilivideo.com)"
r = requests.get(url,headers=headers)
encoding = r.encoding
page_text = r.text
tree = etree.HTML(page_text)
details = tree.xpath('/html/body/div[3]/main/div/div[3]/article//details')
with open("./bcnd.txt","w",encoding=encoding) as fp:
    print("Writing File... ...")
    for code in details:
        cdn = code.xpath('./div/pre/code/text()')[0]
        list_cdn = re.findall(pattern,cdn,re.M)
        for cdn in list_cdn:
            if cdn:
                #print(cdn)
                cdn = cdn + "\n"
                fp.write(cdn)
print("-------------------------------------------")
print("Done")
