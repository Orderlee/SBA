from titanic.entity import Entity
import numpy as np
import pandas as pd
'''
PassengerId  고객ID,
Survived 생존여부,
Pclass 승선권 1 = 1등석, 2 = 2등석, 3 = 3등석,
Name,
Sex,
Age,
SibSp 동반한 형제, 자매, 배우자,
Parch 동반한 부모, 자식,
Ticket 티켓번호,
Fare 요금,
Cabin 객실번호,
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