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

## git 명령어

### git add, git commit 명령어

untracked(아직 버전 관리하지 않은 상태의 파일)

→ **git add 명령어**(통해 **변경사항을 staging area**로 옮긴다) ⇒ **staged 상태, tracked 상태**로 바뀜.

→ git commit 명령어 ⇒ repository로 옮긴다.

→ 첫 커밋이 생성. staging area에 두었던 **변경사항**이 기록된다.

이후에 수정하면, **modified 상태**가 된다. (가장 최신 파일(commit)이랑, 현재 상태랑 비교해서 판단)

(반복…) 커밋이 쌓임 commit 1, 2, …

**git add .**  : 모든 파일을 staging area에 올려줘

**git commit -m “message”**

### git status 명령어

### git log 명령어

## commit id

**앞 4자리만 적어줘도 커밋을 구분한다.**

### git diff 명령어

git diff A B (A, B는 commit id)

빠지고 더해지는게 보임

A, B 순서에 따라 다름 ⇒ **A에서 B로 어떻게 변했는지**를 보여준다.

**github 등에서 보세요.**

### 왜 굳이 중간에 Staging Area를 거쳐서 Commit 할까?

**특정 변경 사항**만 쏙쏙 뽑아서 남기고 싶다.

그래서 한 영역이 더 있는 것

**남기고 싶은, 관리하고 싶은 파일만**

## Local Repository → Remote Repository

commit을 단위로 던짐

### git remote add origin {remote_repo}

origin : 별명(alias), 관례상 origin이라 적는다.

remote_repo : url address

### git push where2go branch_name

git push origin master

### git push --set-upstream origin master

origin 과 master 연결

alias : -u

## git clone {remote_repo}

remote repo를 local로 복사

새로 시작할 때 이게 더 간단하네

## git pull