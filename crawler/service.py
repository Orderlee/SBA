import sys
sys.path.insert(0, '/users/YoungWoo/SBA')
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os, shutil
from pandas import DataFrame
from crawler.entity import Entity

class Service:
    def __init__(self):
        self.entity = Entity()

    def bugs_music(self):
        pass
    
    def naver_movie(self):
        pass

    @staticmethod
    def get_url(self, url)-> object:
        myparser = 'html.parser' 
        response =urlopen(url)
        soup = BeautifulSoup(response, myparser)
        return soup

    # 이미지 저장경로와 실제로 파일쓰기를 수행하는 함수
    @staticmethod
    def create_folder_from_dict(self, weekday_dict, myfolder):
        try:
            if not os.path.exists(myfolder):
                os.mkdir(myfolder)

            for mydir in weekday_dict.values():
                mypath = myfolder + mydir


                if os. path.exists(mypath):
                    shutil.rmtree(mypath)

                os. mkdir(mypath)

        except FileExistsError as err:
            print(err)
        return weekday_dict

    # 웹툰 리스트 만들고 이미지 파일을 저장
    def create_webtoon_list(self, soup, myfolder, weekday_dict):
        mytarget = soup.find_all('div', attrs={'class':'thumb'})
        print(len(mytarget))

        mylist = []

        for abcd in mytarget:
            myhref = abcd.find('a').attrs['href']
            myhref = myhref.replace('/weebtoon/list.nhn?','')
            retuls = myhref.split('&')

            mytitleid = result[0].split('=')[1]
            myweekday = result[1].split('=')[1]

            imgtag = abcd.find('img')
            mytitle = imgtag.attrs['title'].strip()
            mytitle = mytitle.replace('?','').replace(':','')
            mysrc = imgtag.attrs['scr']

            Service.save_imag_file(
                mysrc, myfolder, weekday_dict, myweekday, mytitle)

            sublist = [mytitleid, myweekday, mytitle, mysrc]
            mylist.append(sublist)

        return mylist

    # csv 파일로 저장하는 함수
    def save_csv_file(self, mylist, filename):
        mycolumns =['타이틀 번호', '요일', '제목', '링크']
        myframe = DataFrame(mylist, columns = mycolumns)
        myframe.to.csv(filename, encoding='UTF-8', index=False)
        print('csv 저장 되었습니다.')
    