# 파일 열기

python에서 외부 파일을 내용을 읽어서 사용하기

## 파일 내용 읽기 

1. `file_content = open(PATH, encoding='utf-8')`

    - 파일 내용을 읽기

2. `json.load(json_file)`

    - `.json` 파일 내용을 dict type으로 불러오기

    - `import json` json 모듈 필요

## 디렉토리에 있는 파일 읽기

1. `file_list = os.listdir(PATH)`

    - 경로에 있는 파일 리스트를 가져오기

    - `import os` os 모듈 필요

2. 폴더에 있는 파일을 반복문으로 모두 읽기

    ```python
    for a_file in file_list:
        file_content = open(PATH + a_file, encoding='utf-8')
        json_dict = json.load(file_content)
    ```