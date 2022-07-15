# Git 기초

### git 이란?

분산 버전 관리 도구

- ‘버전 관리 도구’
  - 변경사항과 최종 파일만 저장해서 관리
- ‘분산’ (↔ 중앙 집중 (ex.은행))
  - 다른 컴퓨터 A, B 그리고 서버 컴퓨터(github 같은 것)

git은 버전 관리 프로그램.

github은 버전 관리 서비스를 제공하는 곳.

### github을 사용하면 뭐가 좋을까?

1. 버전관리
2. 포트폴리오 ⇒ gitlab과 github 둘 다 쓴다.
3. github의 social coding (git을 사용해서 협업하는 능력은 필수)
4. 내 코드를 이용한 SNS

### markdown과 github

- [README.md](http://README.md) 를 통해 오픈 소스의 공식 문서 작성
- 개인 프로젝트의 소개 문서
- 매일 학습한 내용 정리
- 마크다운을 위한 블로그 운영

⇒ 개발 문서의 시작과 끝

## Repository

**특정 디렉토리를 기준**으로

버전 관리하는 **저장소**

**git init 명령어** → **로컬 저장소 생성(.git 디렉토리가 생김)**

.git 디렉토리에 버전 관리에 필요한 모든 것

master → git으로 버전관리가 되고 있는 곳 (master branch)

## [README.md](http://README.md) 생성하기

특정 버전으로 남긴다 → 커밋(commit) 한다.

3가지 영역을 바탕으로 동작

- Working Directory
  - 내가 작업하고 있는 실제 디렉토리
- Staging Area
  - 커밋(commit)으로 남기고 싶은, 특정 버전으로 관리하고 싶은 파일이 있는 곳
  - **상태들이 잠시 머무는 곳.**
- Repository (.git 디렉토리)
  - 커밋들이 저장되는 곳
