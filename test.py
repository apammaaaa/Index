from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import os

def switch_img_number():
    global n, mode
    ls = os.listdir(h1)
    ls.sort(key=lambda x:int(x.strip(".webp"))) # 顺序是乱的，可能是根据文件大小排的序，所以根据文件名排序
    if len(ls) and mode != "3":
        last_img = int(ls[-1].strip(".webp"))
        mode = "1"
    else:
        last_img = 0
    n = last_img

def download_img(img_em):
    r = requests.get(img_em.attrs['src'])
    with open("./{}/{}.webp".format(h1, n), "wb") as f:
        f.write(r.content)
        f.close()
def get_img(target_img_em):
    global n
    for i in target_img_em:
        if i and type(i) != type(1):
            if not os.path.isfile("./{}/{}.webp".format(h1, n)) :
                download_img(i)
            n += 1  

def find_next_a(bsObj) -> bool:
    target_span_em = ("span", {"class": "next"})
    if bsObj.find(target_span_em[0], target_span_em[1]).a:
        return True
    return False

def get_next_url(bsObj):
    if find_next_a(bsObj):
        link = "?type=C&start={}&sortby=like&size=a&subtype=a".format(divmod(n, 30)[0]*30)
        return first_link + link
    else:
        return None

def build_file(bsObj):
    global h1
    target_div = ("div", {"id":"content"})
    h1 = bsObj.find(target_div[0], target_div[1]).h1.get_text()
    if not os.path.isdir(h1):
        os.mkdir(h1)

def init(bsObj):
    global n
    if not h1 or not os.path.isdir(str(h1)):
        build_file(bsObj)
    if not n:
        switch_img_number()
        n = divmod(n, 30)[0] * 30
    if mode == "3":
        n = divmod(n, 30)[0] * 30
    
def get_target_img_em(link):    
    target_ul = ("ul", {"class":"poster-col3 clearfix"})
    driver.get(link)
    bsObj = BeautifulSoup(driver.page_source, 'lxml')
    target_ul_em = bsObj.find(target_ul[0], target_ul[1])
    target_li_em = bsObj.findAll("li")
    target_img_em = [i.find("img") for i in target_ul_em]
    return bsObj, target_img_em 

def find_lost_img():
    ls = os.listdir(h1)
    ls.sort(key=lambda x:int(x.strip(".webp")))
    last_number = int(ls[-1].strip(".webp"))
    switch_ls = [str(i) + ".webp" for i in range(last_number+1)]
    s1 = set(ls)
    s2 = set(switch_ls)
    s3 = s2.difference(s1)
    print(s3)
    return s3

def build_lost_n(img_s):
    global n
    n = divmod(int(img_s.strip(".webp")), 30)[0] * 30

def main(link):
    global mode
    bsObj, target_img_em  = get_target_img_em(link)
    init(bsObj)
    if mode == "0":
        """按顺序下载"""
        print("go to 1 mode")
        get_img(target_img_em)
        link = get_next_url(bsObj)
        if link:
            main(link)
    elif mode == "1":
        """接着最后一张图片下载"""
        print("go to 2 mode")
        inherit_link = get_next_url(bsObj)
        if inherit_link:
            bsObj, target_img_em  = get_target_img_em(inherit_link)
            get_img(target_img_em)
            mode = "0"
            link = get_next_url(bsObj)
            if link:
                main(link)
    elif mode == "3":
        """查漏模式:下载缺失的图片"""
        print("go to 3 mode")
        lost_img_s = find_lost_img()
        for img_s in lost_img_s:
            build_lost_n(img_s)
            link = get_next_url(bsObj)
            if link:
                bsObj, target_img_em  = get_target_img_em(link)
                get_img(target_img_em)
if __name__ == "__main__":
    n = 0
    h1 = None
    mode = "3"
    first_link = "https://movie.douban.com/celebrity/1018743/photos/" # 初始页面
    driver = webdriver.Chrome()
    main(first_link)
    driver.close()
    print("done")