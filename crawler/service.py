from bs4 import BeautifulSoup
from urllib.request import urlopen
#from user.entity import Entity
class Service:
    def __init__(self):
        pass

    def bugs_music(self):
        pass
    
    def cnaver_movie(self):
        pass

    def naver_cartoon(self,url):
        myparser = 'html.parser'
        response = url
        soup = BeautifulSoup(response, myparser)
        print(type(soup))
    
    #요일별 폴더 생성
    def create_folder_weekend(self):
        weekday_dict = {'mon':'월요일', 'tue':'화요일', 'wed':'수요일', 'thu':'목요일', 'fri':'금요일', 'sat':'토요일', 'sun':'일요일'}        
        import os, shutil
        myfolder = 'd:\\imsi\\'

        try :
            if not os.path.exists(myfolder):
                os.mkdir(myfolder)

            for mydir in weekday_dict.values():
                mypath = myfolder + mydir

                if os.path.exists(mypath):
                    # rmtree : remove tree
                    shutil.rmtree(mypath)

                os.mkdir(mypath)

        except FileExistsError as err :
            print(err)

    
# 각 이미지를 저장해주는 함수
# def saveFile(mysrc, myweekday, mytitle):
#     image_file = urlopen(mysrc)
#     filename = myfolder + weekday_dict[myweekday] + '\\' + mytitle + '.jpg'
#     # print(mysrc)
#     # print(filename)

#     myfile = open(filename, mode='wb')
#     myfile.write(image_file.read()) # 바이트 형태로 저장
#     myfile.close()
