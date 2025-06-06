from dotenv import load_dotenv
import json
# import logging


# # 로깅 설정
# logging.basicConfig(level=logging.DEBUG)
# 환경 변수 로드
load_dotenv("C:/projects/pypi/kiwoom-rest-api/.env")

from kiwoom_rest_api.koreanstock.account import Account
from kiwoom_rest_api.auth.token import TokenManager

# 토큰 매니저 초기화
token_manager = TokenManager()

# StockInfo 인스턴스 생성 (base_url 수정)
account = Account(base_url="https://api.kiwoom.com", token_manager=token_manager)

def print_result(result_name, result, print_result):
    if isinstance(result, dict):
        if str(result.get("return_code")) == "0":
            if print_result:
                print(f"{result_name} 응답:\n", json.dumps(result, indent=4, ensure_ascii=False))
            else:
                print(f"{result_name} 응답: 성공")
        else:
            print(f"{result_name} 응답: 실패\n", json.dumps(result, indent=4, ensure_ascii=False))
    else:
        print(f"{result_name} is not a dictionary.")


try:
    print("\n\n test 실행")
    
    print_result("ka10072_result", account.realized_profit_by_date_stock_request_ka10072(
        stock_code="005930",
        start_date="20241128"
    ), print_result=False)
    
    print_result("ka10073_result", account.realized_profit_by_period_stock_request_ka10073(
        stock_code="005930",
        start_date="20241128",
        end_date="20241128"
    ), print_result=False)

    print_result("ka10074_result", account.daily_realized_profit_request_ka10074(
        start_date="20240301",
        end_date="20240331"
    ), print_result=False)
    
    print_result("ka10075_result", account.unfilled_orders_request_ka10075(
        all_stk_tp="1",
        trde_tp="0",
        stex_tp="0",
        stock_code="005930"
    ), print_result=False)
    
    print_result("ka10076_result", account.filled_orders_request_ka10076(
        qry_tp="1",
        sell_tp="0",
        stex_tp="0",
        stock_code="005930"
    ), print_result=False)
    
    print_result("ka10077_result", account.today_realized_profit_detail_request_ka10077(
        stock_code="005930"
    ), print_result=False)
    
    print_result("ka10085_result", account.account_return_rate_request_ka10085(
        stex_tp="0"  # 통합 거래소
    ), print_result=False)
    
except Exception as e:
    print("에러 발생:", str(e))



