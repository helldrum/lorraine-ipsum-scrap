#!/usr/bin/env pipenv-shebang
#coding:utf8

import requests
from bs4 import BeautifulSoup

def main():
  r=requests.get("https://www.lorraine-ipsum.fr/")
  soup = BeautifulSoup(r.text, 'html.parser')
  names_list=[li.text.strip().replace("\n","\t") for li in soup.find_all('li') ]
  [print (f"{name}") for name in names_list]

if __name__ == "__main__":
	 main()
