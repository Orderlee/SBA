from bs4 import BeautifulSoup
from urllib.request import urlopen
import os, shutil
from pandas import DataFrame
from crawler.entity import Entity

class Service:
    def __init__(self):
        pass

    def bugs_music(self):
        pass
    
    def cnaver_movie(self):
        pass

    @staticmethod
    def get_url(this)-> object:
        url = this.url
        myparser = 'html.parser' 
        response =urlopen(url)
        soup = BeautifulSoup(response, myparser)
        return soup

   
    @staticmethod
    def create_folder_from_dict(this)->object:
        
        mydict = this.dict
        folderName= this.new_folder_name
        myfolder = '../'+folderName +'/' 
        try:
            if not os.path.exists(myfolder):
                os.mkdir(myfolder)

            for mydir in mydict.values():
                mypath = myfolder + mydir

                if os.path.exists(mypath):
                    
                    shutil.rmtree(mypath)

                os.mkdir(mypath)

        except FileExistsError as err:
            print(err)
        return myfolder

    
    