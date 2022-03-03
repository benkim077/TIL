# Media query

미디어의 상태에 따라 다른 디자인을 할 수 있게 한다.

다양한 장치들이 생겨나는 상황에서, 미디어 쿼리는 해당 장치에 적합한 표현을 할 수 있게 해주는 기술이다. 

## Example

```css
@media (max-width:500px){
    body{
    background-color: red;
    }
}
@media (mㅁ-width:501px){
    body{
    background-color: green;
    }
}
@media (min-width:601px){
    body{
    background-color: blue;
    }
}
```

## Cascading

둘 다 영향을 주는 상황에서, 브라우저의 선택은?

나중에 오는 코드가 우선 순위가 높아진다.
