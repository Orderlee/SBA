import sys
sys.path.insert(0, '/users/YoungWoo/SBA')
from crawler.entity import Entity
from crawler.service import Service

class Controller:
    def __init__(self):
        self.entity = Entity()
        self.service = Service()

    def naver_cartoon(self):
        service = self.service
        this = self.entity
        soup = service.url_open('https://comic.naver.com/webtoon/weekday.nhn')
        myfolder = '/users/YoungWoo/SBA/crawler/image'
        weekday_dict = {'mon':'월요일', 'tue':'화요일', 'wed':'수요일', 'thu':'목요일', 'fri':'금요일', 'sat':'토요일', 'sun':'일요일'}
        service.create_weekday_folder(weekday_dict, myfolder)
        mylist = service.create_webtoon_list(soup, myfolder, weekday_dict)
        service.save_csv_file(mylist, 'cartoon.csv')

if __name__ == '__main__':

    api = Controller()
    api.naver_cartoon