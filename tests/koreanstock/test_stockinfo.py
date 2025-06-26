from dotenv import load_dotenv
import json
# import logging


# # 로깅 설정
# logging.basicConfig(level=logging.DEBUG)
# 환경 변수 로드
load_dotenv("C:/projects/pypi/kiwoom-rest-api/.env")

from kiwoom_rest_api.koreanstock.stockinfo import StockInfo
from kiwoom_rest_api.auth.token import TokenManager

# 토큰 매니저 초기화
token_manager = TokenManager()

# StockInfo 인스턴스 생성 (base_url 수정)
stock_info = StockInfo(base_url="https://api.kiwoom.com", token_manager=token_manager)

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
    print_result("ka10001_result", stock_info.basic_stock_information_request_ka10001("005930"), False)
    print_result("ka10002_result", stock_info.stock_trading_agent_request_ka10002("005930"), False)
    print_result("ka10003_result", stock_info.daily_stock_price_request_ka10003("005930"), False)
    print_result("ka10013_result", stock_info.credit_trading_trend_request_ka10013("005930", "20241101", "1"), False)
    print_result("ka10015_result", stock_info.daily_transaction_details_request_ka10015("005930", "20241101"), False)
    print_result("ka10016_result", stock_info.reported_low_price_request_ka10016("000", "1", "1", "0", "00000", "0", "0", "5", "1"), False)
    print_result("ka10017_result", stock_info.upper_lower_limit_price_request_ka10017("000", "1", "1", "0", "00000", "0", "0", "5", "1"), False)
    print_result("ka10018_result", stock_info.near_high_low_price_request_ka10018("000", "1", "1", "0", "00000", "0", "0", "5", "1"), False)
    print_result("ka10019_result", stock_info.rapid_price_change_request_ka10019("000", "1", "1", "0", "00000", "0", "0", "5", "0", "1"), False)
    print_result("ka10024_result", stock_info.trading_volume_update_request_ka10024("000", "5", "5", "1"), False)

    
    # 50% 이상 매물이 집중된 종목 조회 (50일 주기)
    print_result("ka10025_result", stock_info.supply_concentration_request_ka10025(
        market_type="000",               # 전체 시장
        supply_concentration_rate="50",  # 50% 이상 집중
        current_price_entry="0",         # 현재가 매물대 진입 포함안함
        supply_count="10",               # 매물대수 10개
        cycle_type="50",                 # 50일 주기
        stock_exchange_type="3"          # 통합 거래소
    ), False)
    
    # 저PBR 종목 조회
    print_result("ka10026_result", stock_info.high_low_per_request_ka10026(
        per_type="1",                # 1: 저PBR
        stock_exchange_type="3"      # 통합 거래소
    ), False)
    
    print_result("ka10028_result", stock_info.rate_of_change_compared_to_opening_price_request_ka10028(
        sort_type               ="1",    # 시가 기준
        trade_quantity_condition="0000", # 전체 거래량
        market_type             ="000",  # 전체 시장
        updown_include          ="1",    # 상하한 포함
        stock_condition         ="0",    # 전체 종목
        credit_condition        ="0",    # 전체 신용조건
        trade_price_condition   ="0",    # 전체 거래대금
        fluctuation_condition   ="1",    # 상위 등락률
        stock_exchange_type     ="3"     # 통합 거래소
    ), print_result=False)
    
    print_result("ka10043_result", stock_info.trading_agent_supply_demand_analysis_request_ka10043(
    stock_code         ="005930",   # 종목코드
    start_date         ="20241031", # 시작일자
    end_date           ="20241107", # 종료일자
    query_date_type    ="0",        # 기간으로 조회
    point_type         ="0",        # 당일 기준
    period             ="5",        # 5일 기간
    sort_base          ="1",        # 종가순 정렬
    member_code        ="36",       # 회원사코드
    stock_exchange_type="3"         # 통합 거래소
    ), print_result=False)
    
    print_result("ka10052_result-1", stock_info.trading_agent_instant_trading_volume_request_ka10052(
    member_code="888",          # 회원사코드 (다이와)
    stock_code="",              # 전체 종목
    market_type="0",            # 전체 시장
    quantity_type="0",          # 전체 수량
    price_type="0",             # 전체 가격대
    stock_exchange_type="3"     # 통합 거래소
    ), print_result=False)
    
    print_result("ka10052_result-2", stock_info.trading_agent_instant_trading_volume_request_ka10052(
    member_code="888",
    stock_code="005930",        # 삼성전자
    market_type="3"             # 종목 지정
    ), print_result=False)
    
    print_result("ka10054_result", stock_info.volatility_mitigation_device_triggered_stocks_request_ka10054(
    market_type="000",  # 전체 시장
    before_market_type="0",  # 전체
    stock_code="",  # 전체 종목
    motion_type="0",  # 전체 발동
    skip_stock="000000000",  # 전종목 포함
    stock_exchange_type="3"  # 통합
    ), print_result=False)
    
    print_result("ka10055_result", stock_info.today_vs_previous_day_execution_volume_request_ka10055(
        stock_code="005930",        # 삼성전자
        today_or_previous="2",      # 전일 데이터
        stock_exchange_type="3"     # 통합 거래소
    ), print_result=False)

    print_result("ka10058_result", stock_info.daily_trading_stocks_by_investor_type_request_ka10058(
        start_date="20241106",     # 2024년 11월 6일
        end_date="20241107",       # 2024년 11월 7일
        trade_type="2",            # 순매수
        market_type="101",         # 코스닥
        investor_type="8000",      # 개인투자자
        stock_exchange_type="3"    # 통합 거래소
    ), print_result=False)

    print_result("ka10059_result", stock_info.stock_data_by_investor_institution_request_ka10059(
        date="20241107",           # 2024년 11월 7일
        stock_code="005930",       # 삼성전자
        amount_quantity_type="1",  # 금액기준
        trade_type="0",            # 순매수
        unit_type="1000"           # 천주 단위
    ), print_result=False)

    print_result("ka10061_result", stock_info.aggregate_stock_data_by_investor_institution_request_ka10061(
        stock_code="005930",         # 삼성전자
        start_date="20241007",       # 2024년 10월 7일
        end_date="20241107",         # 2024년 11월 7일
        amount_quantity_type="1",    # 금액기준
        trade_type="0",              # 순매수
        unit_type="1000"             # 천주 단위
    ), print_result=False)

    print_result("ka10084_result", stock_info.today_vs_previous_day_execution_request_ka10084(
        stock_code="005930",        # 삼성전자
        today_or_previous="1",      # 당일 데이터
        tick_or_minute="0",         # 틱 단위
        time=""                     # 전체 시간
    ), print_result=False)
    
    print_result("ka10095_result", stock_info.watchlist_stock_information_request_ka10095(
        stock_code="005930|000660",  # 여러 종목코드 |로 구분
    ), print_result=False)
    
    print_result("ka10099_result", stock_info.stock_information_list_request_ka10099(
        market_type="0"  # 코스피
    ), print_result=False)

    print_result("ka10100_result", stock_info.stock_information_inquiry_request_ka10100(
        stock_code="005930"  # 삼성전자
    ), print_result=False)

    print_result("ka10101_result", stock_info.industry_code_list_request_ka10101(
        market_type="0"  # 코스피
    ), print_result=False)

    print_result("ka10102_result", stock_info.member_company_list_request_ka10102(), print_result=False)
    
    print_result("ka90003_result", stock_info.top_50_program_buy_request_ka90003(
        trade_upper_type="2",         # 순매수상위
        amount_quantity_type="1",     # 금액
        market_type="P00101",         # 코스피
        stock_exchange_type="1"       # KRX
    ), print_result=False)

    print_result("ka90004_result", stock_info.stock_wise_program_trading_status_request_ka90004(
        date="20241125",           # 일자
        market_type="P00101",      # 코스피
        stock_exchange_type="1"    # KRX
    ), print_result=False)

except Exception as e:
    print("에러 발생:", str(e))
