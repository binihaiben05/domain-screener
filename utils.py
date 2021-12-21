import json
import requests
import os


# 读取文件
def read_file(filename:str):
    with open(filename,'r') as f:
        return f.read()

#以json格式读取文件
def read_json(filename:str):
    return json.loads(read_file(filename))

# 判断文件是否已存在
def file_exists(filename:str):
    return os.path.exists(filename)

# 写入一个文件
def write_file(filename:str,content:str):
    with open(filename,'a+') as f:
         f.write(content)
    return content


#以json格式写入文件
def write_json(filename:str,content:str):
    write_file(filename,content)
    return json.loads(content)

#得到每一页的url     
def get_url(page:int):
    return f'https://www.domain.com.au/sold-listings/?ptype=apartment-unit-flat,block-of-units,duplex,free-standing,new-apartments,new-home-designs,new-house-land,pent-house,semi-detached,studio,terrace,villa&page={page}'

#以属性和页数合成文件名
def get_file_name(page:str):
    page_number = str(page).zfill(4)
    return f'{page_number}.json'

#判断是否下载并读取

def download_or_read_json(filename:str,url):
    if file_exists(filename):
        print(f'already downloaded {filename}')
        return read_json(filename)
    else:
        print(f'need to downloaded {url}')
        payload = requests.get(url,headers = {'Accept':'application/json'}).text
        return write_json(filename,payload)


#开始下载
def download(page: int=1): 
    while(page < 2):
        file_name = get_file_name(page)
        url = get_url(page)
        page += 1
        if file_exists(file_name):
            print(f'already downloaded {file_name}')
            continue
        else:
            download_or_read_json(file_name,url)

# download()