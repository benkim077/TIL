# gitignore란?

> 비밀번호 등 중요한 정보가 들어있는 파일을 github에 올리고 싶지 않은데?
> 이런 상황에서 .gitignore를 사용한다.

.gitignore에 적혀있는 파일들을 git에서 제외시킨다.

**gitignore까지가 최초 커밋이다.**

## 어떻게 적지?

```
(.gitignore 파일 내용)
filename.txt
dir/
*.json
dir/*.txt
```

## gitignore에 한번에 추가하기!

> 프로젝트를 진행하다 보면 자동으로 생성되는 파일들이 있다. 
> 이런 파일들을 git으로 관리할 필요는 없다.

- 링크로 들어가서, [gitignore.io](gitignore.io)

- 자신의 프로젝트에 꼭 맞는 .gitignore 파일을 만드세요.
운영체제, 언어, 프레임워크 등을 적어넣으면 .gitignore를 자동으로 만들어준다!

- 복사해서 .gitignore에 붙여넣기

- 맨 위에는 내가 따로 관리하고 싶은 파일들을 적어서 gitignore 시키면 된다.