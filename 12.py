#지정가 매도
import pybithumb
con_key = ""
sec_key = ""
bithumb = pybithumb.Bithumb(con_key, sec_key)
order = bithumb.buy_limit_order()#큰 따옴표 안의 티거, 금액, 수량 순서로 입력
print(order)
#책에 시장가 매도 코드가 있다. p.260부터