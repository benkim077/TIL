# git 명령어

## git add, git commit 명령어

untracked(아직 버전 관리하지 않은 상태의 파일)

→ **git add 명령어**(통해 **변경사항을 staging area**로 옮긴다) ⇒ **staged 상태, tracked 상태**로 바뀜.

→ git commit 명령어 ⇒ repository로 옮긴다.

→ 첫 커밋이 생성. staging area에 두었던 **변경사항**이 기록된다.

이후에 수정하면, **modified 상태**가 된다. (가장 최신 파일(commit)이랑, 현재 상태랑 비교해서 판단)

(반복…) 커밋이 쌓임 commit 1, 2, …

**git add .**  : 모든 파일을 staging area에 올려줘

**git commit -m “message”**

## git status 명령어

### ## git log 명령어

commit id **앞 4자리만 적어줘도 커밋을 구분한다.**

## git diff 명령어

git diff A B (A, B는 commit id)

빠지고 더해지는게 보임

A, B 순서에 따라 다름 ⇒ **A에서 B로 어떻게 변했는지**를 보여준다.

**github 등에서 보세요.**

### 왜 굳이 중간에 Staging Area를 거쳐서 Commit 할까?

**특정 변경 사항**만 쏙쏙 뽑아서 남기고 싶다.

그래서 한 영역이 더 있는 것

**남기고 싶은, 관리하고 싶은 파일만**

### Local Repository → Remote Repository

commit을 단위로 던짐

## git remote add origin {remote_repo}

origin : 별명(alias), 관례상 origin이라 적는다.

remote_repo : url address

## git push where2go branch_name

git push origin master

### git push --set-upstream origin master

origin 과 master 연결

alias : -u

## git clone {remote_repo}

remote repo를 local로 복사

새로 시작할 때 이게 더 간단하네

## git pull