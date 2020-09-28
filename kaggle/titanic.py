import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from config import basedir
from util.file_handler import FileReader
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
# 내부에서는 모듈의 객체를 인스턴스화해야 한다.
# 대문자는 클래스
# 소문자는 인스턴스= (객체)
# 라운드 브레이스가 있는 클래스는 생성자이다.
# 결론.. 객체지향(OOP)에서는 속성과 기능을 호출하는 구조로 
# 두가지 방식이 있는데
# (스태틱)클래스 객체
# (다이나믹) 인스턴스 객체
class Service:
    def __init__(self):
        self.entity = FileReader()
        self.kaggle = os.path.join(basedir,'kaggle')
        self.data = os.path.join(self.kaggle,'data')

    # payload(컴퓨팅)
    # 전송되는 데이터
    def new_model(self, payload)-> object:
        this = self.entity
        this.data =self.data
        this.fname = payload
        return pd.read_csv(os.path.join(self.data, this.fname))

    @staticmethod
    def create_train(this)-> object:
        return this.train.drop('Survived',axis=1) #train 은 답이 제거된 데이터셋이다.

    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived']

    @staticmethod
    def drop_feature(this,feature) -> object:
        this.train =this.train.drop([feature],axis=1)
        this.test = this.test.drop([feature],axis=1)
        return this
    @staticmethod
    def pclass_ordinal(this)-> object:
        return this
    @staticmethod
    def name_norminal(this)-> object:
        return this
    @staticmethod
    def sex_norminal(this)-> object:
        combine =[this.train,this.test]
        sex_mapping= {'male': 0,'female':1}
        for dataset in combine:
            dataset['Sex'] = dataset['Sex'].map(sex_mapping)
        this.train = combine[0] # overriding
        this.test= combine[1]
        return this
    @staticmethod
    def age_ordinal(this)-> object:
        train = this.train
        test = this.test
        train['Age']= train['Age'].fillna(-0.5)
        test['Age']= test['Age'].fillna(-0.5) 
        
        # age 는 가중치가 상당하므로 디테일한 접근이 필요합니다.
        # 나이를 모르는 승객은 모르는 상태로 처리해야 값의 왜곡을 줄일수 있다.
        # -0.5 라는 중간값으로 처리했습니다.
        bins =[-1,0,5,12,18,24,35,60,np.inf]
        # [] 에 있으니 이것은 변수명
        labels = ['Unknown','Baby','Child','Teenager','Student','Young Adult','Adult','Senior']
        train['AgeGroup']=pd.cut(train['Age'],bins,labels =labels)
        test['AgeGroup']=pd.cut(train['Age'],bins,labels =labels)
        age_title_mapping = {
            0:'Unknown',
            1:'Baby',
            2:'Child',
            3:'Teenager',
            4:'Student',
            5:'Young Adult',
            6:'Adult',
            7:'Senior'
        }

        for x in range(len(train['AgeGroup'])):
            if train['AgeGroup'][x] == 'Unknown':
                train['AgeGroup'][x]= age_title_mapping[train['Title'][x]]

        for x in range(len(test['AgeGroup'])):
            if test['AgeGroup'][x] == 'Unknown':
                test['AgeGroup'][x]= age_title_mapping[train['Title'][x]]       
        age_mapping = {
            'Unknown':0,
            'Baby':1,
            'Child':2,
            'Teenager':3,
            'Student':4,
            'Young Adult':5,
            'Adult':6,
            'Senior':7
        }    
        train['AgeGroup'] = train['AgeGroup'].map(age_mapping)
        test['AgeGroup'] = test['AgeGroup'].map(age_mapping)
        return this
    
    @staticmethod
    def sibsp_numeric(this)-> object:
        return this
    @staticmethod
    def parch_numeric(this)-> object:
        return this
    @staticmethod
    def embarked_norminal(this)-> object:
        
        this.train = this.train.fillna({'Embarked':'S'}) # S가 가장 많아서 빈곳에 채움
        this.test = this.test.fillna({'Embarked':'S'}) #  교과서 144
        # 많은 머신러닝 라이브러리는 클래스 레이블이"정수"로 인코딩 되어있다고 기대함
        this.train['Embarked']= this.train['Embarked'].map({'S': 1, 'C':2 , 'Q':3} )
        this.test['Embarked']= this.test['Embarked'].map({'S': 1, 'C':2 , 'Q':3} )

        return this
    @staticmethod
    def fare_ordinal(this)-> object:
        this.train['FareBand'] = pd.qcut(this.train['Fare'], 4, labels={1,2,3,4})
        this.test['FareBand'] = pd.qcut(this.test['Fare'], 4, labels={1,2,3,4})
        return this   
    @staticmethod
    def fareBand_ordinal(this)-> object:
        this.train = this.train.fillna({"FareBand":1})
        this.test = this.test.fillna({"FareBand":1})
        return this
    @staticmethod
    def title_norminal(this)-> object:
        combine =[this.train,this.test]
        for dataset in combine:
            dataset['Title']= dataset.Name.str.extract('([A-Za-z]+)\.',expand= False)
        for dataset in combine:
            dataset['Title']= dataset['Title'].replace(['Mme','Capt', 'Col','Don','Dr','Major','Rev','Jonkheer','Dona'],'Rare')
            dataset['Title']= dataset['Title'].replace(['Countess','Lady','Sir'],'Rare')
            dataset['Title']= dataset['Title'].replace('Ms','Miss')
            dataset['Title']= dataset['Title'].replace('Mlle','Mr')
        title_mapping ={'Mr':1,'Miss':2,'Mrs':3,'Master':4,'Royal':5,'Rare':6}
        for dataset in combine:
            dataset['Title']= dataset['Title'].map(title_mapping)
            dataset['Title']= dataset['Title'].fillna(0) # Unknown
        this.train = this.train
        this.test = this.test
        return this
    @staticmethod
    def create_k_fold():
        return KFold(n_splits=10,shuffle=True,random_state=0)

    def accuracy_by_dtree(self,this):
        dtree = DecisionTreeClassifier()
        score =cross_val_score(dtree, this.train,this.label,cv=Service.create_k_fold(),n_jobs=1, scoring='accuracy')
        return round(np.mean(score)*100,2)
    def accuracy_by_rforest(self,this):
        rforest = RandomForestClassifier()
        score = cross_val_score(rforest, this.train, this.label, cv=Service.create_k_fold(), n_jobs=1,
                                scoring='accuracy')
        return round(np.mean(score) * 100, 2)

    def accuracy_by_nb(self,this):
        nb = GaussianNB()
        score = cross_val_score(nb, this.train, this.label, cv=Service.create_k_fold(), n_jobs=1,
                                scoring='accuracy')
        return round(np.mean(score) * 100, 2)
    def accuracy_by_knn(self,this):
        knn = KNeighborsClassifier()
        score = cross_val_score(knn, this.train, this.label, cv=Service.create_k_fold(), n_jobs=1,
                                scoring='accuracy')
        return round(np.mean(score) * 100, 2)
    def accuracy_by_svm(self,this):
        svm = SVC()
        score = cross_val_score(svm, this.train, this.label, cv=Service.create_k_fold(), n_jobs=1,
                                scoring='accuracy')
        return round(np.mean(score) * 100, 2)

class Controller:
    def __init__(self):
        self.entity = FileReader()
        self.kaggle = os.path.join(basedir,'kaggle')
        sefl.data = os.path.ojin(self.kaggle,'data')
        self.service = Service()
    
    def modeling(self,train, test):
        service = self.service
        this = self.preprocessing(train, test)
        print(f'훈련 컬럼: {this.train.columns}')
        this.label =service.create_label(this)
        this.train = service.create_train(this)
        return this
    
    def preprocessing(self, train, test):
        service = self.service
        this = self.entity
        this.train = service.new_model(train) #payload
        this.test = service.new_model(test)
        this.id = this.test['PassengerId'] #머신이에게는 이것이 question이 됩니다.
        
        this = service.drop_feature(this,'Cabin')
        this = service.drop_feature(this,'Ticket')
        
        this = service.drop_feature(this, 'PassengerId')
        this = service.embarked_norminal(this)
        print(f'드롭 후 변수 :\n{this.train.columns}')
        
        print(f'승선한 항구 정제 결과:\n{this.train.head()}')
       
        this = service.title_norminal(this)
        print(f'이름 정제 결과:\n{this.train.head()}')
        this = service.drop_feature(this, 'Name')
        
        this = service.fare_ordinal(this)
        print(f'요금 정제 결과:\n{this.train.head()}')
        this = service.fareBand_ordinal(this)
        print(f'요금2 정제 결과:\n{this.train.head()}')
        this = service.age_ordinal(this)
        print(f'나이 정제 결과:\n{this.train.head()}')
        this = service.sex_norminal(this)
        this = service.drop_feature(this,'Fare')
        print(f'성별 정제 결과:\n{this.train.head()}')
        print(f'#########  TEST 정제결과 ###############')
        print(f'{this.test.head()}')
        print(f'######## train na 체크 ##########')
        print(f'{this.train.isnull().sum()}')
        print(f'######## test na 체크 ##########')
        print(f'{this.test.isnull().sum()}')

        return this

    
    def learing(self,train,test):  # evaluation과 합친다.
        service = self.service
        this = self.modeling(train,test)
        print(f'결정 트리:{service.accuracy_by_dtree(this)}' )
        print(f'nb:{service.accuracy_by_nb(this)}')
        print(f'knn:{service.accuracy_by_knn(this)}')
        print(f'svm:{service.accuracy_by_svm(this)}')
        print(f'rforest:{service.accuracy_by_rforest(this)}')

    def submit(self,train,test): # 파일로 저장
        this = self.modeling(train,test)
        clf = RandomForestClassifier()
        clf.fit(this.train,this.label)
        prediction = clf.predict(this.test)
        pd.DataFrame(
            {'PassengerId': this.id , 'Survived': prediction}
        ).to_csv(os.path.join(self.data,'submission.csv'),index =False)

if __name__ =='__main__':
    print(f'***************** {basedir} **************')
    ctrl = Controller()
    ctrl.submit('train.csv', 'test.csv')