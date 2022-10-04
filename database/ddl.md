# DDL Data Definition Language

- 데이터 정의

- CREATE 생성, ALTER 수정, DROP 삭제

## CREATE TABLE statement

- 데이터베이스에 새로운 테이블을 만든다.

```sql
CREATE TABLE table_name(
    column_1 data_type constraints,
    column_2 data_type constraints,
    column_2 data_type constraints,
);
```

- id 컬럼은 자동으로 rowid라는 이름으로 만들어진다.

## Data Type

1. NULL

    - NULL 값

    - 정보가 없거나 알 수 없음

2. INTEGER

    - 정수

    - 가변 크기를 가짐

3. REAL

    - 실수

4. TEXT

    - 문자 데이터

5. BLOB(Binary Large Object)

    - 타입 없이 **입력된 데이터 그대로 저장**된 데이터 덩어리

    - 멀티미디어 파일, 이미지 데이터 등

- Boolean, Date & Time Datatype 등

    - 타입은 없지만 TEXT, REAL, INTEGER으로 대체해서 저장해준다.

    - 내장 함수들을 통해서 형태를 저장해주는 방식

### SQLite의 데이터 타입 결정

- 값에 둘러싸는 따옴표나 소수점 또는 지수가 없으면 - INTEGER

- 값이 작은 따옴표나 큰따옴표를 묶이면 - TEXT

- 값에 따옴표나 소수점, 지수가 있으며 - REAL

- 값이 따옴표 없이 NULL이면 - NULL

### SQLite Datatypes 특징

- 다른 모든 SQL 데이터베이스 엔진은 정적이고 엄격함(static, rigid typing)

- SQLite는 동적 타입 시스템(dynamic type system)을 사용

    - 컬럼에 선언된 데이터 타입에 의해서가 아니라, 컬럼에 저장된 값에 따라 데이터 타입에 결정

- 다른 데이터베이스와 호환성 문제가 있기 때문에, 테이블 생성 시 데이터 타입을 지정하는 것을 권장

- 데이터 타입을 지정하면, SQLite는 입력된 데이터의 타입을 지정된 데이터 타입으로 변환(자동 형 변환)

### Type Affinity 타입 선호도

- 특정 컬럼에 저장된 데이터에 권장되는 타입

- 데이터 타입 작성 시 SQLite의 5가지 데이터 타입이 아닌 다른 데이터 타입을 선언한다면, 내부적으로 각 타입의 지정된 선호도에 따라 5가지 선호도로 인식됨

- 타입 선호도 존재 이유 : 다른 데이터베이스 엔진 간의 호환성 최대화

## Constraint 제약조건

- 입력하는 자료에 대해 제약

- 제약에 맞지 않다면 입력 거부

- 데이터의 무결성 유지 목적

### 데이터 무결성

- 데이터베이스 내 데이터에 대한 정확성, 일관성을 보장하는 것

- 일관되게 유지하는 것이 목적

### Constraints 종류

1. NOT NULL

    - NULL 값을 허용하지 않도록 지정

    - 기본은 NULL값을 허용

2. UNIQUE

    - 컬럼의 모든 값이 고유한 값이 되도록 함

3. PRIMARY KEY

    - 레코드를 식별하는 데 사용되는 컬럼

    - 암시적으로 NOT NULL 제약조건 포함

    - INTEGER 타입에만 사용 가능

    - UNIQUE와는 좀 다르다.

4. AUTOINCREMENT

    - 사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용하는 것을 방지

    - SQLite는 기본적으로 재사용 함. 장고는 재사용 안함.

### rowid의 특징

- 테이블을 생성할 때 마다 rowid라는 암시적 자동 증가 컬럼(자동으로 증가)이 자동으로 생성

- 새 행을 삽입할 때 마다 정수 값을 자동으로 할당

- 값은 1에서 시작

- 다음 순차 정수를 자동으로 할당(이전 것 보다 하나 큰 rowid가 다음)

- 만약 INTEGER PRIMARY KEY 키워드를 가진 컬럼을 직접 만들면 이 컬럼은 rowid 컬럼의 별칭(alias)가 됨

## ALTER TABLE

- 기존 테이블의 구조를 수정

1. 테이블 이름 수정 `ALTER TABLE table_name RENAME TO new_table_name;`

2. 컬럼 이름 수정 `ALTER TABLE new_contacts RENAME COLUMN name TO last_name;`

3. 새로운 컬럼 추가 `ALTER TABLE new_contacts ADD COLUMN address TEXT NOT NULL;`

    - 테이블에 기존 데이터가 있을 경우 에러 발생

    - `Cannot add NOT NULL column with default value NULL`

    - 새로 추가되는 컬럼에 NOT NULL 제약조건이 있기 때문에.

    - 해결 방법

        - DEFAULT 제약 조건 사용

        - `ALTER TABLE new_contacts ADD COLUMN address TEXT NOT NULL DEFAULT 'no address';`

4. 컬럼 삭제

    - `ALTER TABLE new_contacts DROP COLUMN address;`

    - 삭제하지 못하는 경우

        - 컬럼이 다른 테이블에서 참조되는 경우(관계가 맺어져있는 경우)

            - FOREIGN KEY(외래키) 제약조건에서 사용되는 경우

        - PK 인 경우

        - UNIQUE 제약 조건이 있는 경우(email)

## DROP TABLE

- `DROP TABLE new_contacts;`

- 데이터베이스에서 테이블을 제거

- 한 번에 하나의 테이블만 삭제

- 취소하거나 복구할 수 없음