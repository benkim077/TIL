# 모듈과 패키지

모듈
- 특정 기능을 하는 코드를 .py 파일 단위로 작성한 것

패키지
- 여러 모듈의 집합
- 서브 패키지

## 모듈과 패키지 불러오기

외부 개발자들이 만든 것을 가져다 쓰자

### 모듈 불러오기

`import moduleName as name` as name 별명 지정하기

`from moduleName import var, function, Class`

`from moduleName import *`

### 패키지 불러오기

`from package import moduleName`

`from package.moduleName import var, function, Class`