클래스 하나가 단위 Unitdl 됨
이제 확장 하겠습니다.
객체지향에서는 디자인패턴이라는 개념이 존재함
1994년 GoF 4인방 개발자 에릭 감마... 패턴 23개로 정의...
이 분이 vscode 개발자

패턴조합을 통해 큰 개념의 패턴 -> MVC 패턴이라고 함
model, view controller 이렇게 조합 --> java, c 언어에서 주로 사용하는 개념.

model : 데이터처리 -> API 서버 -> Python -> Tensorflow
view : 화면 UI처리 -> UI 서버 -> React
controller : model + view 를 연결 --> 네트워크라고 함 -> Flask : app.py -> RESTful 방식

팀내에서의 나의 역할을 고민
취업시 자신을 어필할 수 있는 혹은 자신있는 혹은 흥미있는 카테고리를 결정하는것
Backedn Tier (API 서버 구축담당: Java, C, python)
Frontend Tier (UI 서버 구축담당: Javascript,HTML,Reactjs))

모델을 제작하고 뷰를 만들어서 컨트롤러로 연결한다. 이 컨셉을 이해
프로토타입
독자적으로 움직임 --> ㅁ모듈
5개의 모듈(개인이 작성)을 합쳤을 때, 조립이 잘 되서 작동이 잘 되면 1단계 패스

dataset (test.csv, train.csv)

titanic 폴더에
dataset(test.csv,train.csv)이게 존재
entity(속성) + service(기능) = 객체(object)

def __init__(self, ....) => 속성
def abc(): 기능
결국 class는 객체를 정의하는 것