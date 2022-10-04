# DML

- DML을 통해 데이터 조작(CRUD)

- INSERT, SELECT, UPDATE, DELETE

## Simple query

- `SELECT column1, column2 FORM table_name;`

- 특정 테이블에서 데이터를 조회

- 문법 규칙

    - SELECT 절에서 컬럼 또는 쉼표로 구분된 컬럼 목록 지정

    - FROM 절에서 데이터를 가져올 테이블을 지정

- 다양한 절과 함께 사용(복잡도 UP)

    - ORDER BY, DISTINCT, WHERE, LIMIT, LIKE, GROUP BY

- 이름과 나이 조회하기

    - `SELECT first_name, age FROM users;`

- 전체 데이터 조회하기

    - `SELECT * FROM users;`

## Sorting rows

`SELECT select_list FROM table_name ORDER BY column_1 ASC, column_2 DESC;`

- SELECT 문에 추가하여 결과를 정렬

- FROM 절 뒤에 위치

- ASC, DESC

- 이름과 나이를 나이가 어린 순서대로 조회하기

    - `SELECT first_name, age FROM users ORDER BY age DESC;`

- 이름, 나이, 계좌 잔고를 나이가 어린순으로, 같은 나이라면 계좌 잔고가 많은 순으로 정렬해서 조회하기

    - `SELECT first_name, age, balance FROM users ORDER BY age ASC, balance DESC;`

- NULL의 정렬?

    - SQLite는 NULL은 다른 값보다 작은 것으로 간주

## Filtering data

- 데이터를 필터링하여 중복 제거, 조건 설정 등 쿼리 제어하기

- Clause

    - SELECT DISTINCT, WHERE, LIMIT

- Operator

    - LIKE, IN, BETWEEN

### SELECT DISTINCT clause

- 결과에서 중복된 행을 제거

- 선택적으로 쓸 수 있는 절

- 문법 규칙

    1. SELECT 키워드 바로 뒤에

    2. DISTINCT 키워드 뒤에 컬럼 또는 컬럼 목록을 작성

- 모든 지역 조회하기

    - `SELECT DISTINCT country FROM users;`

- 지역 순으로 내림차순 정렬하여 중복없이 모든 지역 조회하기

    - `SELECT DISTINCT country FROM users ORDER BY country;`

- 이름과 지역이 중복 없이 모든 이름과 지역 조회하기

    - `SELECT DISTINCT first_name, country FROM users;`

> 각 칼럼의 중복을 따로 계산하는 것이 아니라, 두 컬럼을 하나의 집합으로 보고 중복을 제거

- 이름과 지역 중복 없이 지역 순으로 내림차순 정렬하여 모든 이름과 지역 조회하기

    - `SELECT DISTINCT first_name, country FROM users ORDER BY country DESC;`

- NULL with DISTINCT

    - SQLite는 NULL 값을 중복으로 간주

    - NULL도 값이니까, 중복되면 하나만 남긴다.

### WHERE clause

- `SELECT column_list FROM table_name WHERE search_condition;`

- 조회 시 특정 검색 조건을 지정

- WHERE 절은 SELECT, UPDATE, DELETE 문에서 사용할 수 있다.

- FROM 절 뒤에 작성

- 비교 연산자

- 논리 연산자

    - 1, 0 또는 NULL 값을 반환

    - 1은 TRUE, 0은 FALSE를 의미

    - ALL, AND, ANY, BETWEEN, IN, LIKE, NOT, OR 등

- 나이가 30살 이상인 사람들의 이름, 나이, 계좌 잔고 조회하기

    - `SELECT first_name, age, balance FROM user WHERE age >= 30;`

- 나이가 30살 이상이고 계좌 잔고가 50만원 초과인 사람들의 이름, 나이, 계좌 잔고 조회하기

    - `SELECT first_name, age, balance FROM user WHERE age >= 30 AND balance > 500000;`

### LIKE operator

- 패턴 일치를 기반으로 데이터를 조회

- SELECT, DELETE, UPDATE 문의 WHERE 절에서 사용

- 기본적으로 대소문자 구분하지 않음

- 패턴 구성을 위한 두 개의 와일드카드

    - % : 0개 이상의 문자가 올 수 있음

    - _ : 단일 문자가 있음을 의미

#### wildcards character

- 파일을 지정할 때, 구체적인 이름 대신에 여러 파일을 동시에 지정할 목적으로 사용하는 특수 기호

    - *, ? 등

- 이름에 '호'가 포함되는 사람들의 이름과 성 조회하기

    - `SELECT first_name, last_name FROM users WHERE first_name LIKE '%호%';`

- 서울 지역 전화번호를 가진 사람들의 이름과 전화번호 조회하기

    - `SELECT first_name, phone FROM users WHERE phone LIKE '02-%';`

- 나이가 20대인 사람들의 이름과 나이 조회하기

    - `SELECT first_name, age FROM users WHERE age LIKE '2_';`

### IN operator

- 값이 값 목록 결과에 있는 값과 일치하는지 확인

- 일치 여부에 따라 true, false 반환

- NOT IN은 IN의 부정

- 경기도 혹은 강원도에 사는 사람들의 이름과 지역 조회하기

    - `SELECT first_name, country FROM users WHERE country IN ('경기도', '강원도');`

### BETWEEN operator

- 값이 범위에 있는지 테스트. 범위에 있으면 true 반환

- BETWEEN 연산자의 결과 부정 => NOT BETWEEN 사용

- 나이가 20살 이상, 30살 이하인 사람들의 이름과 나이 조회하기

    - `SELECT first_name, age FROM users WHERE age BETWEEN 20 AND 30;`

### LIMIT clause

- `SELECT column_list FROM table_name LIMIT row_count;`

- 쿼리에서 반환되는 행 수를 제한

- row_count는 반환되는 행 수를 지정하는 양의 정수

- 첫 번째부터 열 번째 데이터까지 rowid와 이름 조회하기

    - `SELECT rowid, first_name FROM users LIMIT 10;`

- 계좌 잔고가 가장 많은 10명의 이름과 계좌 잔고 조회하기

    - `SELECT first_name, balance FROM users ORDER BY balance DESC LIMIT 10;`

### OFFSET keyword

- LIMIT 절을 OFFSET과 함께 사용하면 특정 지정된 위치에서부터 데이터를 조회할 수 있음

- 11번째부터 20번째 데이터의 rowid와 이름 조회하기

    - `SELECT rowid, first_name FROM users LIMIT 10 OFFSET 10;`

## Grouping data

- `SELECT column_1, aggregate_function(column_2) FROM table_name GROUP BY column_1, column_2;`

- 특정 그룹으로 묶인 결과를 생성

- 선택된 컬럼 값을 기준으로 데이터들의 공통 값을 묶어서 나타냄

- 각 그룹에 대해 집계 함수(aggregate function)을 적용할 수 있다.

    - MIN, MAX, SUM, COUNT, AVG

- users 테이블의 전체 행 수 조회하기

    - `SELECT COUNT(*) FROM users;`

- 나이가 30살 이상인 사람들의 평균 나이 조회하기

    - `SELECT AVG(age) FROM users WHERE age >= 30;`

- 각 지역별로 몇 명씩 살고 있는지 조회하기

    - `SELECT country, COUNT(*) FROM users GROUP BY country;`

    - 지역별로 그룹이 나눠졌기 때문에, COUNT(*)는 지역별 데이터 갯수를 셈

- 각 성씨가 몇 명씩 있는지 조회하기

    - `SELECT last_name, COUNT(*) AS number_of_name FROM users GROUP BY last_name;`

    - AS 키워드를 사용해 컬럼명을 임시로 변경해서 나타낼 수 있다.

- 인원이 가장 많은 성씨 순으로 조회하기

    - `SELECT last_name, COUNT(*) FROM users GROUP BY last_name ORDER BY COUNT(*) DESC;`

## Changing data

- 데이터를 삽입 INSERT, 수정 UPDATE, 삭제하기 DELETE

### INSERT statement

- `INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);`

- 새 행을 테이블에 삽입

- 문법 규칙

    1. INSERT INTO 키워드 뒤에 데이터를 삽입할 테이블 이름 지정

    2. 테이블 이름 뒤에 쉼표로 구분된 컬럼 목록 추가

        - 컬럼 목록은 선택사항이지만 포함하는 것이 권장됨.

    3. VALUES 키워드 뒤에 쉼표로 구분된 값 목록 추가

        - 컬럼 목록을 생략하는 경우 값 목록의 모든 컬럼에 대한 값을 지정해야 함

        - 값 목록의 갯수는 컬럼 목록의 컬럼 갯수와 같아야 함.

- 단일 행 삽입하기

    - `INSERT INTO classmates (name, age, address) VALUES ('홍길동', 23, '서울');`

    - `INSERT INTO classmates VALUES ('홍길동', 23, '서울');`

- 여러 행 삽입하기

```sql
INSERT INTO classmates 
VALUES 
    ('김철수', 30, '경기'),
    ('이영미', 31, '강원'),
    ('박진성', 26, '전라'),
    ('최지수', 12, '충청'),
    ('정요한', 28, '경상');
```

### UPDATE statement

```sql
UPDATE table_name
SET column_1 = new_value_1
    column_1 = new_value_2
WHERE
    search_condition;
```

- 테이블에 있는 기존 행의 데이터를 업데이트

- 문법규칙

    1. UPDATE 절 이후에 업데이트할 테이블을 지정

    2. SET 절에서 테이블의 각 컬럼에 대해 새 값을 지정

    3. WHERE 절의 조건을 사용하여 업데이트할 행을 지정

        - 선택사항이며, 생략하면 테이블의 모든 행에 대해 업데이트

    4. 선택적으로 ORDER BY 및 LIMIT 절을 사용하여 업데이트할 행 수를 지정할 수 있다.

- 2번 데이터의 이름을 '김철수한무두루미', 주소를 '제주도'로 수정하기

    - `UPDATE classmates SET name='김철수한무두루미', address='제주도' WHERE rowid=2;`

### DELETE statement

```SQL
DELETE FROM table_name
WHERE search_condition;
```

- 테이블에서 행 제거

- 테이블의 한 행, 여러 행, 모든 행을 삭제 가능

- 문법 규칙

    1. DELETE FROM 키워드 뒤에 행을 제거하려는 테이블의 이름을 지정

    2. WHERE 절에 검색 조건을 추가하여 제거할 행을 식별

        - 생략하면 모든 행을 삭제

    3. 선택적으로 ORDER BY, LIMIT 절을 사용하여 삭제할 행 수를 지정

- 5번 데이터 삭제하기

    - `DELETE FROM classmates WHERE rowid = 5;`

- 이믈에 '영'이 포함되는 데이터 삭제하기

    - `DELETE FROM classmates WHERE name LIKE '%영%';`

- 테이블의 모든 데이터 삭제하기

    - `DELETE FROM classmates;`