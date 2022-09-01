### DateTimeField()

- Python의 datetime.datetime 인스턴스로 표시되는 날짜 및 시간을 값으로 사용하는 필드

- DataField를 상속받는 클래스

- 선택 인자

> 주의, 시험

    1. auto_now_add

        - 최조 생성 일자 creation of timestamps

        - 데이터가 실제로 **만들어질 때** 현재 날짜와 시간으로 자동으로 초기화

    2. auto_now

        - 최종 수정 일자 last-modified

        - 데이터가 **수정될 때마다** 현재 날짜와 시간으로 자동으로 갱신되도록 함

