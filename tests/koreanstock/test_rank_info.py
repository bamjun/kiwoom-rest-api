from dotenv import load_dotenv
import json

# 환경 변수 로드
load_dotenv("C:/projects/pypi/kiwoom-rest-api/.env")

from kiwoom_rest_api.koreanstock.rank_info import RankInfo
from kiwoom_rest_api.auth.token import TokenManager

# 토큰 매니저 초기화
token_manager = TokenManager()

# RankInfo 인스턴스 생성
rank_info = RankInfo(base_url="https://api.kiwoom.com", token_manager=token_manager)

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
    
    print_result("ka10020_result", rank_info.top_order_book_volume_request_ka10020(
        mrkt_tp="001",  # 코스피
        sort_tp="1",  # 순매수잔량순
        trde_qty_tp="0000",  # 장시작전(0주이상)
        stk_cnd="0",  # 전체조회
        crd_cnd="0",  # 전체조회
        stex_tp="1"  # KRX
    ), print_result=False)
    
    print_result("ka10021_result", rank_info.sudden_increase_order_book_volume_request_ka10021(
        mrkt_tp="001",  # 코스피
        trde_tp="1",  # 매수잔량
        sort_tp="1",  # 급증량
        tm_tp="30",  # 30분
        trde_qty_tp="1",  # 천주이상
        stk_cnd="0",  # 전체조회
        stex_tp="3"  # 통합
    ), print_result=False)
    
    print_result("ka10022_result", rank_info.sudden_increase_order_ratio_request_ka10022(
        mrkt_tp="001",  # 코스피
        rt_tp="1",  # 매수/매도비율
        tm_tp="1",  # 1분
        trde_qty_tp="5",  # 5천주이상
        stk_cnd="0",  # 전체조회
        stex_tp="3"  # 통합
    ), print_result=False)
    
    print_result("ka10023_result", rank_info.sudden_increase_trading_volume_request_ka10023(
        mrkt_tp="000",  # 전체
        sort_tp="1",  # 급증량
        tm_tp="2",  # 전일
        trde_qty_tp="5",  # 5천주이상
        stk_cnd="0",  # 전체조회
        pric_tp="0",  # 전체조회
        stex_tp="3"  # 통합
    ), print_result=False)
    
    print_result("ka10027_result", rank_info.top_day_over_day_change_rate_request_ka10027(
        mrkt_tp="000",  # 전체
        sort_tp="1",  # 상승률
        trde_qty_cnd="0000",  # 전체조회
        stk_cnd="0",  # 전체조회
        crd_cnd="0",  # 전체조회
        updown_incls="1",  # 포함
        pric_cnd="0",  # 전체조회
        trde_prica_cnd="0",  # 전체조회
        stex_tp="3"  # 통합
    ), print_result=False)
    
    print_result("ka10029_result", rank_info.top_expected_execution_change_rate_request_ka10029(
        mrkt_tp="000",  # 전체
        sort_tp="1",  # 상승률
        trde_qty_cnd="0",  # 전체조회
        stk_cnd="0",  # 전체조회
        crd_cnd="0",  # 전체조회
        pric_cnd="0",  # 전체조회
        stex_tp="3"  # 통합
    ), print_result=False)
    
    print_result("ka10030_result", rank_info.top_trading_volume_today_request_ka10030(
        mrkt_tp="000",  # 전체
        sort_tp="1",  # 거래량
        mang_stk_incls="0",  # 관리종목 포함
        crd_tp="0",  # 전체조회
        trde_qty_tp="0",  # 전체조회
        pric_tp="0",  # 전체조회
        trde_prica_tp="0",  # 전체조회
        mrkt_open_tp="0",  # 전체조회
        stex_tp="3"  # 통합
    ), print_result=False)
    
    print_result("ka10031_result", rank_info.top_trading_volume_yesterday_request_ka10031(
        mrkt_tp="101",  # 코스닥
        qry_tp="1",  # 전일거래량 상위100종목
        rank_strt="0",  # 0번째부터
        rank_end="10",  # 10번째까지
        stex_tp="3"  # 통합
    ), print_result=False)
    
    print_result("ka10032_result", rank_info.top_trading_value_request_ka10032(
        mrkt_tp="001",  # 코스피
        mang_stk_incls="1",  # 관리종목 포함
        stex_tp="3"  # 통합
    ), print_result=False)
    
    print_result("ka10033_result", rank_info.top_credit_ratio_request_ka10033(
        mrkt_tp="000",  # 전체
        trde_qty_tp="0",  # 전체조회
        stk_cnd="0",  # 전체조회
        updown_incls="1",  # 상하한포함
        crd_cnd="0",  # 전체조회
        stex_tp="3"  # 통합
    ), print_result=False)
    
    print_result("ka10034_result", rank_info.top_foreign_investor_trades_by_period_request_ka10034(
        mrkt_tp="001",  # 코스피
        trde_tp="2",  # 순매수
        dt="0",  # 당일
        stex_tp="1"  # KRX
    ), print_result=False)
    
    print_result("ka10035_result", rank_info.top_foreign_consecutive_net_buy_request_ka10035(
        mrkt_tp="000",  # 전체
        trde_tp="2",  # 연속순매수
        base_dt_tp="1",  # 전일기준
        stex_tp="1"  # KRX
    ), print_result=False)
    
    print_result("ka10036_result", rank_info.top_foreign_limit_utilization_increase_request_ka10036(
        mrkt_tp="000",  # 전체
        dt="1",  # 전일
        stex_tp="1"  # KRX
    ), print_result=False)
    
    print_result("ka10037_result", rank_info.top_foreign_broker_trading_request_ka10037(
        mrkt_tp="000",  # 전체
        dt="0",  # 당일
        trde_tp="1",  # 순매수
        sort_tp="2",  # 수량
        stex_tp="1"  # KRX
    ), print_result=False)
    
    print_result("ka10038_result", rank_info.broker_ranking_by_stock_request_ka10038(
        stk_cd="005930",  # 삼성전자
        strt_dt="20241106",  # 시작일자
        end_dt="20241107",  # 종료일자
        qry_tp="2",  # 순매수순위정렬
        dt="1"  # 전일
    ), print_result=False)
    
    print_result("ka10039_result", rank_info.top_broker_trading_request_ka10039(
        mmcm_cd="001",  # 회원사코드
        trde_qty_tp="0",  # 전체
        trde_tp="1",  # 순매수
        dt="1",  # 전일
        stex_tp="3"  # 통합
    ), print_result=False)
    
    print_result("ka10040_result", rank_info.main_trading_brokers_today_request_ka10040(
        stk_cd="005930"  # 삼성전자
    ), print_result=False)
    
    print_result("ka10042_result", rank_info.top_net_buying_brokers_request_ka10042(
        stk_cd="005930",  # 삼성전자
        qry_dt_tp="0",  # 기간으로 조회
        pot_tp="0",  # 당일
        sort_base="1",  # 종가순
        dt="5"  # 5일
    ), print_result=False)
    
    print_result("ka10053_result", rank_info.top_departed_trading_brokers_today_request_ka10053(
        stk_cd="005930",  # 삼성전자
    ), print_result=False)
    
    print_result("ka10062_result", rank_info.same_day_net_buying_ranking_request_ka10062(
        strt_dt="20241106",  # 시작일자
        mrkt_tp="000",  # 전체
        trde_tp="1",  # 순매수
        sort_cnd="1",  # 순매수순위정렬
        unit_tp="0",  # 전체
        stex_tp="3"  # 통합
    ), print_result=False)
    
    print_result("ka10065_result", rank_info.top_intraday_investor_trading_request_ka10065(
        trde_tp="1",  # 순매수
        mrkt_tp="000",  # 전체
        orgn_tp="9000"  # 외국인
    ), print_result=False)
    
    print_result("ka10098_result", rank_info.after_market_price_change_rate_ranking_request_ka10098(
        mrkt_tp="000",  # 전체
        sort_base="1",  # 종가순
        stk_cnd="0",  # 전체조회
        trde_qty_cnd="0",  # 전체조회
        crd_cnd="0",  # 전체조회
        trde_prica="0",  # 전체조회
    ), print_result=False)
    
    print_result("ka90009_result", rank_info.top_foreign_institution_trades_request_ka90009(
        mrkt_tp="000",  # 전체
        amt_qty_tp="0",  # 전체조회
        qry_dt_tp="0",  # 기간으로 조회
        stex_tp="3"  # 통합
    ), print_result=False)

except Exception as e:
    print("에러 발생:", str(e))