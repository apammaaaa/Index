import requests
import json
from bs4 import BeautifulSoup
import re
import sys

def handle_headers(h):
    di = {}
    for i in h.strip("\n").split("\n"):
        l = i.split(":")
        d = {l[0].strip(":"):l[1].strip()}
        di.update(d)
    return di

def cut_text(em):
    text = em.get_text().strip().strip("\n").strip("\t")
    if not text or text == "\n":
        text = "None"
    return text
def psp(em, emname):
    if emname != "form":
        text = cut_text(em)
        if emname == "a":
            print(text, end="")
            try:
                print("[{}]".format(em.attrs['href']))
            except:
                print("[<a>]")
        else:
            print(text)
    else:
        print("<form>", "[{}]".format(em.attrs))
        for j in em:
            if j.name != "input":
                if str(type(j)) == "<class 'bs4.element.Tag'>":
                    text = cut_text(j)
                    print(" "*4 + "<{}>".format(j.name), text, j.attrs)
            else:
                print(" "*4 ,j)
        print("</form>")
def pb(em, sp):
    for i in em:
        if str(type(i)) == "<class 'bs4.element.Tag'>":
            emname = i.name
            if emname in sp:
                psp(i, emname)
            pb(i, sp)
        
def print_bsobj(bsObj):
    matchls = ("a", "p", "h1", "h2", "h3", "h4", "h5", "h6", "form")
    sp = ("style", "script", "textarea", "input")
    head = bsObj.find("head")
    body = bsObj.find("body")
    pb(body, matchls)
def handle_links(links) -> str:
    if not links.startswith("http"):
        link2 = "https://" + links
        return link2
    return links

def get_url(links):
    try: 
        r = session.get(url=links, headers=headers)
    except:
        try:
            r = session.get(url="http://"+links.strip("https://"), headers=headers)
        except:
            r = None
    return r
    
h = """
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: max-age=0
Connection: keep-alive
Cookie: BIDUPSID=731DA63DC0C06F0D7CE75BEEA81F0585; PSTM=1601437281; BD_UPN=12314753; hide_hotsearch=1; BAIDUID=D66438B5A8AA61C80E84BE523DB00EC4:FG=1; __yjs_duid=1_f30217da54c2f9f498a66820bd7ee2401608803866823; BDUSS=jE4eUFxd3BRcEJOTkZNeERaUWJjUFoySmV5Q2ZPZmc3UFpsdnprZXlWQ3BVeHBnSVFBQUFBJCQAAAAAAAAAAAEAAABKHFWxSGFydXRhc2F2ZQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKnG8l-pxvJfR; BDUSS_BFESS=jE4eUFxd3BRcEJOTkZNeERaUWJjUFoySmV5Q2ZPZmc3UFpsdnprZXlWQ3BVeHBnSVFBQUFBJCQAAAAAAAAAAAEAAABKHFWxSGFydXRhc2F2ZQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKnG8l-pxvJfR; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; yjs_js_security_passport=c799578d989d6359c951c46459c05a8e955ba6cd_1610007231_js; BAIDUID_BFESS=9ED2EC11F2BEA2DAEC050D1E65E19960:FG=1; COOKIE_SESSION=11434_0_9_0_16_4_0_0_9_4_0_0_0_0_20_0_1610018147_0_1610029561%7C9%2386134_437_1610006661%7C9; H_PS_645EC=7f30DB5Upc8%2BPWvTFIyDPVhEleLdc5XRnVq5j3evdNPkl4vn3VHZDGNlMHzwr%2B6N8Vo4; BD_HOME=1; H_PS_PSSID=33423_1459_33438_31254_32973_33287_33350_33413_26350_33389_33370; sug=3; sugstore=0; ORIGIN=2; bdime=0; BA_HECTOR=0l012h0h25250h8h4n1fvfg9d0q
sec-ch-ua: "Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"
sec-ch-ua-mobile: ?0
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
"""
headers = handle_headers(h)
links = sys.argv[1]
links = handle_links(links)
session = requests.session()
r = get_url(links)
if r:
    bsObj = BeautifulSoup(r.text, 'lxml')
    print_bsobj(bsObj)
else:
    print("连接错误")