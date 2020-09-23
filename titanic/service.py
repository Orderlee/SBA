from titanic.entity import Entity
import numpy as np
import pandas as pd
'''
-----PassengerId  고객ID,
-----Survived 생존여부,
Pclass 승선권 1 = 1등석, 2 = 2등석, 3 = 3등석,
Name,
Sex,
Age,
SibSp 동반한 형제, 자매, 배우자,
Parch 동반한 부모, 자식,
-----Ticket 티켓번호,
Fare 요금,
-----Cabin 객실번호,
Embarked 승선한 항구명 C = 쉐브루, Q = 퀸즈타운, S = 사우스햄튼
'''
class Service:
    def __init__(self):
        self.entity = Entity() #@Autowired Entitny entity (스프링에서 같은거)

    #train은 답이 제거된 데이터셋 axis=0 가로 1은 세로
    #self를 사용하는면 다이나믹으로 진행 
    #this.context='./data/'
    #label 은 곧 답이 된다.
    # 머신러닝교과서 p.139  df = tensor
    def new_model(self,payload) -> object: 
        this = self.entity  
        this.fname = payload 
        return pd.read_csv(this.context + this.fname) 

    
    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived',axis=1) 
    
    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived'] 

    @staticmethod
    def drop_feature(this,feature) -> object:
        this.train = this.train.drop([feature], axis=1)
        this.test = this.test.drop([feature], axis=1) #훈련,테스트 세트로 나눈다.
        return this

    @staticmethod
    def pclass_ordinal(this) -> object:
        return 

    @staticmethod
    def name_norminal(this) -> object:
        return this
    
    @staticmethod
    def sex_nornimal(this) -> object:
        combine =[this.train, this.test] # train과 test가 묶임
        sex_mapping = {'male':0,'female':1}
        for dataset in combine:
            dataseet['Sex'] = dataset['Sex'].map(sex_mapping)
        
        this.train = this.train # overriding # 같은의미 this.train=comine[0] #this.train['Sex'] = this.train['Sex'].map({'female':1,'male':0})
        this.test = this.test  # 같은의미 this.test=comine[1] #this.test['Sex'] = this.test['Sex'].map({'female':1,'male':0})
        
        return this
    
    @staticmethod
    def age_ordinal(this) -> object:
        train = this.train
        test = this.test
        train['Age'] = train['Age'].fillna(-0.5)
        test['Age'] = test['Age'].fillna(-0.5)
        # age를 평균으로 넣기도 애매, 다수결로 넣을 근거가 없다.
        # age는 생존률 판단에서 가중치(weight)가 상당하므로 디테일한 접근이 필요
        # 나이를 모르는 승객은 모르는 상태로 처리해야 값의 왜곡을 줄일 수 있음
        # -0.5라는 경계값으로 처리
        bins = [-1,0,5,12,18,24,35,60,np.inf] # [] 에 있으니 변수명, 범위를 의미(-0이상 0미만... 60이상 기타)
        labels = ['Unknown','Baby','child','Teenager','Student','Young Adult','Adult','Senior'] #[]은 변수명으로 선언
        train['AgeGroup'] = pd.cut(train['Age'],bins,labels=labels)
        test['AgeGroup'] = pd.cut(test['Age'],bins,labels=labels)
        age_title_mapping = {0:'Unknown',
        1:'Baby',
        2:'child',
        3:'Teenager',
        4:'Student',
        5:'Young Adult',
        6:'Adult',
        7:'Senior'} # labels 를 값으로 처리
        return this

    @staticmethod
    def fare_ordinal(this) -> object:
        this.train['FareBand'] = pd.qcut(this['Fare'], 4, labels={1,2,3,4})
        this.test['FareBand'] = pd.qcut(this['Fare'], 4, labels={1,2,3,4})
        return this

    
    @staticmethod
    def fareBand_nominal(this) -> object: 
        this.train = this.train.fillna({'FareBand':1}) #요금이 다양하여 클러스터링을 하기 위한 준비,fareBand는 없는 변수인데 추가함
        this.test = this.test.fillna({'FareBand':1})
        return this

    @staticmethod
    def name_nominal(this) -> object:
        return this

    @staticmethod
    def embarked_norminal(this) -> object:
        this.train = this.train.fillna({'Embarked':'S'} # S가 가장 많아서 빈곳에 채움
        this.test = this.test.fillna({'Embarked':'S'}) # 교과서 144 : 많은 머신러닝 라이브러리는 클래스 레이블이 '정수'로 인코딩 되어있음
        # 교과서 146 문자 blue = 0, green =1 , red = 2 로 치환 -> mapping 함
        this.train['Embarked'] = this.train['Embarked'].map({'S':1,'C':2,'Q':3}) # ordinal 아님
        this.test['Embarked'] = this.test['Embarked'].map({'S':1,'C':2,'Q':3})
        return this
    
    @staticmethod
    def parch_numeric(this) ->object:
        return this

    @staticmethod
    def sibsp_numeric(this) ->object:
        return this