# Selectors 심화

## 결합자

- 자손 결합자

    `selectorA selectorB`
    
    - selectorA 하위의 모든 selectorB 요소

- 자식 결합자

    - `selectorA > selectorB`

    - selectorA 바로 아래의 selectorB 요소

- 일반 형제 결합자

    - selectorA의 형제 요소 중 바로 뒤에 위치하는 selectorB 요소를 선택

    - `selectorA + selectorB`