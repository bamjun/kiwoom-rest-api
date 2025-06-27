from dotenv import load_dotenv
import json
# import logging


# # 로깅 설정
# logging.basicConfig(level=logging.DEBUG)
# 환경 변수 로드
load_dotenv("C:/projects/pypi/kiwoom-rest-api/.env")

from kiwoom_rest_api.koreanstock.slb import SecuritiesLendingAndBorrowing
from kiwoom_rest_api.auth.token import TokenManager

# 토큰 매니저 초기화
token_manager = TokenManager()

# StockInfo 인스턴스 생성 (base_url 수정)
slb = SecuritiesLendingAndBorrowing(base_url="https://api.kiwoom.com", token_manager=token_manager)

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
    
    print_result("ka10068_result", slb.stock_lending_trend_request_ka10068(
        strt_dt="20250401",
        end_dt="20250430",
        all_tp="1"
    ), print_result=False)
    
    print_result("ka10069_result", slb.top10_stock_lending_request_ka10069(
        strt_dt="20241110",
        end_dt="20241125",
        mrkt_tp="001"
    ), print_result=False)
    
    print_result("ka20068_result", slb.stockwise_lending_trend_request_ka20068(
        stk_cd="005930",
        strt_dt="20250401",
        end_dt="20250430",
        all_tp="0"
    ), print_result=False)
    
    print_result("ka90012_result", slb.stock_lending_details_request_ka90012(
        dt="20241101",
        mrkt_tp="101"
    ), print_result=False)
    
    
except Exception as e:
    print("에러 발생:", str(e))



