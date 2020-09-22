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
        soup = service.get_url(this)
        myfolder = service.create_folder_from_dict(this)
        mytarget = service.setting_target(soup,this)
        service.loop_fun(mytarget,this,myfolder)

    def movie_csv(self):
        service=self.service
        this =self.entity
        soup=service.get_url(this)

        target = service.setting_targets(soup,this)
        self.service.loop_fun2(target,this)

if __name__ == '__main__':
    api = Controller()
    api.entity.dict= {'mon': '월요일', 'tue': '화요일', 'wed': '수요일', 'thu': '목요일', 'fri': '금요일', 'sat': '토요일', 'sun': '일요일'}
    api.entity.columns = {'타이틀 번호','요일','제목','링크'}
    api.entity.filename = 'cartoon.csv'
    api.entity.url = 'https://comic.naver.com/webtoon/weekday.nhn'
    api.entity.new_folder_name = 'newfile'
    api.entity.tag='div'
    api.entity.attrs='thumb'
    api.entity.replace_str ='/webtoon/list/nhn?' 

    api.naver_cartoon()

    api2 = Controller()
    api2.entity.columns = ['순위','제목','변동','변동폭']
    api2.entity.url = "http://movie.naver.com/movie/sdb/rank/rmovie.nhn"
    api2.entity.tag ='tr'
    api2.entity.filename= 'navermovierank.csv'

    api2.movie_csv