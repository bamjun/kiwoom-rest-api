from typing import Dict, Optional, Any, List, Union, Callable, Awaitable

from kiwoom_rest_api.core.sync_client import make_request
from kiwoom_rest_api.core.async_client import make_request_async
from kiwoom_rest_api.core.base_api import KiwoomBaseAPI

class StockInfo(KiwoomBaseAPI):
    """한국 주식 종목 정보 관련 API를 제공하는 클래스"""
    
    def __init__(
        self, 
        base_url: str = None, 
        token_manager=None, 
        use_async: bool = False,
        resource_url: str = "/api/dostk/stkinfo"
    ):
        """
        StockInfo 클래스 초기화
        
        Args:
            base_url (str, optional): API 기본 URL
            token_manager: 토큰 관리자 객체
            use_async (bool): 비동기 클라이언트 사용 여부 (기본값: False)
        """
        super().__init__(
            base_url=base_url,
            token_manager=token_manager,
            use_async=use_async,
            resource_url=resource_url
        )
    
    def basic_stock_information_request_ka10001(
        self, stock_code: str, cont_yn: str = "N", next_key: str = "0"
    ) -> Union[Dict[str, Any], Awaitable[Dict[str, Any]]]:
        """
        주식기본정보요청
        API ID: ka10001

        Args:
            stock_code (str): 종목코드 (예: '005930')

        Returns:
            Dict[str, Any] or Awaitable[Dict[str, Any]]: 주식 기본 정보
        """
        
        headers = {
            "cont-yn": cont_yn, 
            "next-key": next_key,
            "api-id": "ka10001"
        }

        body = {
            "stk_cd": stock_code, 
        }
        

        
        return self._execute_request("POST", json=body, headers=headers)
    
    def stock_trading_agent_request_ka10002(
        self, stock_code: str, cont_yn: str = "N", next_key: str = "0"
    ) -> Union[Dict[str, Any], Awaitable[Dict[str, Any]]]:
        """
        주식 거래원 요청
        API ID (TR_ID): ka10002 (명세서 예시 ID, 실제 TR ID 확인 필요)

        Args:
            stock_code (str): 종목코드 (예: '005930', 'KRX:039490')
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            Dict[str, Any] or Awaitable[Dict[str, Any]]: 현재가 정보 딕셔너리 또는 Awaitable 객체
        """
        
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10002"
        }
        
        body = {
            "stk_cd": stock_code,
        }

        return self._execute_request("POST", json=body, headers=headers)
    
    def daily_stock_price_request_ka10003(
        self,
        stock_code: str,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> Union[Dict[str, Any], Awaitable[Dict[str, Any]]]:
        """
        체결 정보 요청
        API ID (TR_ID): ka10003 (명세서 예시 ID, 실제 TR ID 확인 필요)

        Args:
            stock_code (str): 종목코드 (예: '005930', 'KRX:039490')
            cont_yn (str, optional): 연속조회여부. 응답 헤더의 값을 사용. Defaults to "N".
            next_key (str, optional): 연속조회키. 응답 헤더의 값을 사용. Defaults to "".

        Returns:
            Dict[str, Any] or Awaitable[Dict[str, Any]]: 체결 정보 딕셔너리 또는 Awaitable 객체
        """
        
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10003"
        }
        
        body = {
            "stk_cd": stock_code,
        }
        
        return self._execute_request("POST", json=body, headers=headers)

    def credit_trading_trend_request_ka10013(
        self,
        stock_code: str,
        date: str,
        query_type: str,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> Union[Dict[str, Any], Awaitable[Dict[str, Any]]]:
        """신용매매동향 요청

        Args:
            stock_code (str): 종목코드 (예: "005930")
            date (str): 조회 일자 (YYYYMMDD 형식)
            query_type (str): 조회구분 (1:융자, 2:대주)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            Union[Dict[str, Any], Awaitable[Dict[str, Any]]]: 응답 데이터
            {
                "crd_trde_trend": [
                    {
                        "dt": "20241101",
                        "cur_prc": "65100",
                        "pred_pre_sig": "0",
                        "pred_pre": "0",
                        "trde_qty": "0",
                        "new": "",
                        "rpya": "",
                        "remn": "",
                        "amt": "",
                        "pre": "",
                        "shr_rt": "",
                        "remn_rt": ""
                    },
                    ...
                ]
            }
        """
        
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10013"
        }
        
        body = {
            "stk_cd": stock_code,
            "dt": date,
            "qry_tp": query_type,
        }
        
        return self._execute_request("POST", json=body, headers=headers)
    
    def daily_transaction_details_request_ka10015(
        self,
        stock_code: str,
        start_date: str,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> Union[Dict[str, Any], Awaitable[Dict[str, Any]]]:
        """일별거래상세요청

        Args:
            stock_code (str): 종목코드 (예: "005930")
            start_date (str): 시작일자 (YYYYMMDD 형식)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            Union[Dict[str, Any], Awaitable[Dict[str, Any]]]: 응답 데이터
            {
                "daly_trde_dtl": [
                    {
                        "dt": "20241105",
                        "close_pric": "135300",
                        "pred_pre_sig": "0",
                        "pred_pre": "0",
                        "flu_rt": "0.00",
                        "trde_qty": "0",
                        "trde_prica": "0",
                        "bf_mkrt_trde_qty": "",
                        "bf_mkrt_trde_wght": "",
                        "opmr_trde_qty": "",
                        "opmr_trde_wght": "",
                        "af_mkrt_trde_qty": "",
                        "af_mkrt_trde_wght": "",
                        "tot_3": "0",
                        "prid_trde_qty": "0",
                        "cntr_str": "",
                        "for_poss": "",
                        "for_wght": "",
                        "for_netprps": "",
                        "orgn_netprps": "",
                        "ind_netprps": "",
                        "frgn": "",
                        "crd_remn_rt": "",
                        "prm": "",
                        "bf_mkrt_trde_prica": "",
                        "bf_mkrt_trde_prica_wght": "",
                        "opmr_trde_prica": "",
                        "opmr_trde_prica_wght": "",
                        "af_mkrt_trde_prica": "",
                        "af_mkrt_trde_prica_wght": ""
                    },
                    ...
                ]
            }
        """
        
        # 헤더 구성
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10015"
        }
        
        # 요청 데이터 구성
        data = {
            "stk_cd": stock_code,
            "strt_dt": start_date
        }

        return self._execute_request("POST", json=data, headers=headers)
    
    def reported_low_price_request_ka10016(
        self,
        market_type: str,
        report_type: str,
        high_low_close_type: str,
        stock_condition: str,
        trade_quantity_type: str,
        credit_condition: str,
        updown_include: str,
        period: str,
        stock_exchange_type: str,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> Union[Dict[str, Any], Awaitable[Dict[str, Any]]]:
        """신고저가 요청

        Args:
            market_type (str): 시장구분 (000:전체, 001:코스피, 101:코스닥)
            report_type (str): 신고저구분 (1:신고가, 2:신저가)
            high_low_close_type (str): 고저종구분 (1:고저기준, 2:종가기준)
            stock_condition (str): 종목조건 (0:전체조회, 1:관리종목제외, 3:우선주제외, 5:증100제외, 6:증100만보기, 7:증40만보기, 8:증30만보기)
            trade_quantity_type (str): 거래량구분 (00000:전체조회, 00010:만주이상, 00050:5만주이상, 00100:10만주이상, ...)
            credit_condition (str): 신용조건 (0:전체조회, 1:신용융자A군, 2:신용융자B군, 3:신용융자C군, 4:신용융자D군, 9:신용융자전체)
            updown_include (str): 상하한포함 (0:미포함, 1:포함)
            period (str): 기간 (5:5일, 10:10일, 20:20일, 60:60일, 250:250일)
            stock_exchange_type (str): 거래소구분 (1:KRX, 2:NXT, 3:통합)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            Union[Dict[str, Any], Awaitable[Dict[str, Any]]]: 응답 데이터
            {
                "ntl_pric": [
                    {
                        "stk_cd": "005930",
                        "stk_nm": "삼성전자",
                        "cur_prc": "334",
                        "pred_pre_sig": "3",
                        "pred_pre": "0",
                        "flu_rt": "0.00",
                        "trde_qty": "3",
                        "pred_trde_qty_pre_rt": "-0.00",
                        "sel_bid": "0",
                        "buy_bid": "0",
                        "high_pric": "334",
                        "low_pric": "320"
                    },
                    ...
                ]
            }
        """
        
        # 헤더 구성
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10016"
        }
        
        # 요청 데이터 구성
        data = {
            "mrkt_tp": market_type,
            "ntl_tp": report_type,
            "high_low_close_tp": high_low_close_type,
            "stk_cnd": stock_condition,
            "trde_qty_tp": trade_quantity_type,
            "crd_cnd": credit_condition,
            "updown_incls": updown_include,
            "dt": period,
            "stex_tp": stock_exchange_type
        }

        return self._execute_request("POST", json=data, headers=headers)

    def upper_lower_limit_price_request_ka10017(
        self,
        market_type: str,
        updown_type: str,
        sort_type: str,
        stock_condition: str,
        trade_quantity_type: str,
        credit_condition: str,
        trade_gold_type: str,
        stock_exchange_type: str,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> Union[Dict[str, Any], Awaitable[Dict[str, Any]]]:
        """상하한가 요청

        Args:
            market_type (str): 시장구분 (000:전체, 001:코스피, 101:코스닥)
            updown_type (str): 상하한구분 (1:상한, 2:상승, 3:보합, 4:하한, 5:하락, 6:전일상한, 7:전일하한)
            sort_type (str): 정렬구분 (1:종목코드순, 2:연속횟수순(상위100개), 3:등락률순)
            stock_condition (str): 종목조건 (0:전체조회, 1:관리종목제외, 3:우선주제외, ...)
            trade_quantity_type (str): 거래량구분 (00000:전체조회, 00010:만주이상, ...)
            credit_condition (str): 신용조건 (0:전체조회, 1:신용융자A군, ...)
            trade_gold_type (str): 매매금구분 (0:전체조회, 1:1천원미만, 2:1천원~2천원, ...)
            stock_exchange_type (str): 거래소구분 (1:KRX, 2:NXT, 3:통합)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            Union[Dict[str, Any], Awaitable[Dict[str, Any]]]: 응답 데이터
            {
                "updown_pric": [
                    {
                        "stk_cd": "005930",
                        "stk_infr": "",
                        "stk_nm": "삼성전자",
                        "cur_prc": "+235500",
                        "pred_pre_sig": "1",
                        "pred_pre": "+54200",
                        "flu_rt": "+29.90",
                        "trde_qty": "0",
                        "pred_trde_qty": "96197",
                        "sel_req": "0",
                        "sel_bid": "0",
                        "buy_bid": "+235500",
                        "buy_req": "4",
                        "cnt": "1"
                    },
                    ...
                ]
            }
        """
        # 헤더 구성
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10017"
        }
        
        # 요청 데이터 구성
        data = {
            "mrkt_tp": market_type,
            "updown_tp": updown_type,
            "sort_tp": sort_type,
            "stk_cnd": stock_condition,
            "trde_qty_tp": trade_quantity_type,
            "crd_cnd": credit_condition,
            "trde_gold_tp": trade_gold_type,
            "stex_tp": stock_exchange_type
        }

        return self._execute_request("POST", json=data, headers=headers)
    
    def near_high_low_price_request_ka10018(
        self,
        high_low_type: str,
        approach_rate: str,
        market_type: str,
        trade_quantity_type: str,
        stock_condition: str,
        credit_condition: str,
        stock_exchange_type: str,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> Union[Dict[str, Any], Awaitable[Dict[str, Any]]]:
        """고저가근접 요청

        Args:
            high_low_type (str): 고저구분 (1:고가, 2:저가)
            approach_rate (str): 근접율 (05:0.5, 10:1.0, 15:1.5, 20:2.0, 25:2.5, 30:3.0)
            market_type (str): 시장구분 (000:전체, 001:코스피, 101:코스닥)
            trade_quantity_type (str): 거래량구분 (00000:전체조회, 00010:만주이상, ...)
            stock_condition (str): 종목조건 (0:전체조회, 1:관리종목제외, ...)
            credit_condition (str): 신용조건 (0:전체조회, 1:신용융자A군, ...)
            stock_exchange_type (str): 거래소구분 (1:KRX, 2:NXT, 3:통합)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            Union[Dict[str, Any], Awaitable[Dict[str, Any]]]: 응답 데이터
            {
                "high_low_pric_alacc": [
                    {
                        "stk_cd": "004930",
                        "stk_nm": "삼성전자",
                        "cur_prc": "334",
                        "pred_pre_sig": "0",
                        "pred_pre": "0",
                        "flu_rt": "0.00",
                        "trde_qty": "3",
                        "sel_bid": "0",
                        "buy_bid": "0",
                        "tdy_high_pric": "334",
                        "tdy_low_pric": "334"
                    },
                    ...
                ]
            }
        """
        # 헤더 구성
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10018"
        }
        
        # 요청 데이터 구성
        data = {
            "high_low_tp": high_low_type,
            "alacc_rt": approach_rate,
            "mrkt_tp": market_type,
            "trde_qty_tp": trade_quantity_type,
            "stk_cnd": stock_condition,
            "crd_cnd": credit_condition,
            "stex_tp": stock_exchange_type
        }

        return self._execute_request("POST", json=data, headers=headers)

    def rapid_price_change_request_ka10019(
        self,
        market_type: str,
        fluctuation_type: str,
        time_type: str,
        time: str,
        trade_quantity_type: str,
        stock_condition: str,
        credit_condition: str,
        price_condition: str,
        updown_include: str,
        stock_exchange_type: str,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> Union[Dict[str, Any], Awaitable[Dict[str, Any]]]:
        """가격급등락 요청

        Args:
            market_type (str): 시장구분 (000:전체, 001:코스피, 101:코스닥, 201:코스피200)
            fluctuation_type (str): 등락구분 (1:급등, 2:급락)
            time_type (str): 시간구분 (1:분전, 2:일전)
            time (str): 시간 (분 혹은 일 입력)
            trade_quantity_type (str): 거래량구분 (00000:전체조회, 00010:만주이상, ...)
            stock_condition (str): 종목조건 (0:전체조회, 1:관리종목제외, ...)
            credit_condition (str): 신용조건 (0:전체조회, 1:신용융자A군, ...)
            price_condition (str): 가격조건 (0:전체조회, 1:1천원미만, ...)
            updown_include (str): 상하한포함 (0:미포함, 1:포함)
            stock_exchange_type (str): 거래소구분 (1:KRX, 2:NXT, 3:통합)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            Union[Dict[str, Any], Awaitable[Dict[str, Any]]]: 응답 데이터
            {
                "pric_jmpflu": [
                    {
                        "stk_cd": "005930",
                        "stk_cls": "",
                        "stk_nm": "삼성전자",
                        "pred_pre_sig": "2",
                        "pred_pre": "+300",
                        "flu_rt": "+0.57",
                        "base_pric": "51600",
                        "cur_prc": "+52700",
                        "base_pre": "1100",
                        "trde_qty": "2400",
                        "jmp_rt": "+2.13"
                    },
                    ...
                ]
            }
        """
        # 헤더 구성
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10019"
        }
        
        # 요청 데이터 구성
        data = {
            "mrkt_tp": market_type,
            "flu_tp": fluctuation_type,
            "tm_tp": time_type,
            "tm": time,
            "trde_qty_tp": trade_quantity_type,
            "stk_cnd": stock_condition,
            "crd_cnd": credit_condition,
            "pric_cnd": price_condition,
            "updown_incls": updown_include,
            "stex_tp": stock_exchange_type
        }

        return self._execute_request("POST", json=data, headers=headers)
    
    def trading_volume_update_request_ka10024(
        self,
        market_type: str,
        cycle_type: str,
        trade_quantity_type: str,
        stock_exchange_type: str,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> Union[Dict[str, Any], Awaitable[Dict[str, Any]]]:
        """거래량갱신 요청

        Args:
            market_type (str): 시장구분 (000:전체, 001:코스피, 101:코스닥)
            cycle_type (str): 주기구분 (5:5일, 10:10일, 20:20일, 60:60일, 250:250일)
            trade_quantity_type (str): 거래량구분 (5:5천주이상, 10:만주이상, 50:5만주이상, 100:10만주이상, ...)
            stock_exchange_type (str): 거래소구분 (1:KRX, 2:NXT, 3:통합)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            Union[Dict[str, Any], Awaitable[Dict[str, Any]]]: 응답 데이터
            {
                "trde_qty_updt": [
                    {
                        "stk_cd": "005930",
                        "stk_nm": "삼성전자",
                        "cur_prc": "+74800",
                        "pred_pre_sig": "1",
                        "pred_pre": "+17200",
                        "flu_rt": "+29.86",
                        "prev_trde_qty": "243520",
                        "now_trde_qty": "435771",
                        "sel_bid": "0",
                        "buy_bid": "+74800"
                    },
                    ...
                ]
            }
        """
        # 헤더 구성
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10024"
        }
        
        # 요청 데이터 구성
        data = {
            "mrkt_tp": market_type,
            "cycle_tp": cycle_type,
            "trde_qty_tp": trade_quantity_type,
            "stex_tp": stock_exchange_type
        }

        return self._execute_request("POST", json=data, headers=headers)
    
    def supply_concentration_request_ka10025(
        self,
        market_type: str,
        supply_concentration_rate: str,
        current_price_entry: str,
        supply_count: str,
        cycle_type: str,
        stock_exchange_type: str,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> Union[Dict[str, Any], Awaitable[Dict[str, Any]]]:
        """매물대집중 요청

        Args:
            market_type (str): 시장구분 (000:전체, 001:코스피, 101:코스닥)
            supply_concentration_rate (str): 매물집중비율 (0~100 입력)
            current_price_entry (str): 현재가진입 (0:현재가 매물대 진입 포함안함, 1:현재가 매물대 진입포함)
            supply_count (str): 매물대수 (숫자입력)
            cycle_type (str): 주기구분 (50:50일, 100:100일, 150:150일, 200:200일, 250:250일, 300:300일)
            stock_exchange_type (str): 거래소구분 (1:KRX, 2:NXT, 3:통합)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            Union[Dict[str, Any], Awaitable[Dict[str, Any]]]: 응답 데이터
            {
                "prps_cnctr": [
                    {
                        "stk_cd": "005930",
                        "stk_nm": "삼성전자",
                        "cur_prc": "30000",
                        "pred_pre_sig": "3",
                        "pred_pre": "0",
                        "flu_rt": "0.00",
                        "now_trde_qty": "0",
                        "pric_strt": "31350",
                        "pric_end": "31799",
                        "prps_qty": "4",
                        "prps_rt": "+50.00"
                    },
                    ...
                ]
            }
        """
        # 헤더 구성
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10025"
        }
        
        # 요청 데이터 구성
        data = {
            "mrkt_tp": market_type,
            "prps_cnctr_rt": supply_concentration_rate,
            "cur_prc_entry": current_price_entry,
            "prpscnt": supply_count,
            "cycle_tp": cycle_type,
            "stex_tp": stock_exchange_type
        }

        return self._execute_request("POST", json=data, headers=headers)
    
    def high_low_per_request_ka10026(
        self,
        per_type: str,
        stock_exchange_type: str,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> Union[Dict[str, Any], Awaitable[Dict[str, Any]]]:
        """고저PER 요청

        Args:
            per_type (str): PER구분 (1:저PBR, 2:고PBR, 3:저PER, 4:고PER, 5:저ROE, 6:고ROE)
            stock_exchange_type (str): 거래소구분 (1:KRX, 2:NXT, 3:통합)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            Union[Dict[str, Any], Awaitable[Dict[str, Any]]]: 응답 데이터
            {
                "high_low_per": [
                    {
                        "stk_cd": "005930",
                        "stk_nm": "삼성전자",
                        "per": "0.44",
                        "cur_prc": "4930",
                        "pred_pre_sig": "3",
                        "pred_pre": "0",
                        "flu_rt": "0.00",
                        "now_trde_qty": "0",
                        "sel_bid": "0"
                    },
                    ...
                ]
            }
        """
        # 헤더 구성
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10026"
        }
        
        # 요청 데이터 구성
        data = {
            "pertp": per_type,
            "stex_tp": stock_exchange_type
        }

        return self._execute_request("POST", json=data, headers=headers)

    def rate_of_change_compared_to_opening_price_request_ka10028(
        self,
        sort_type: str,
        trade_quantity_condition: str,
        market_type: str,
        updown_include: str,
        stock_condition: str,
        credit_condition: str,
        trade_price_condition: str,
        fluctuation_condition: str,
        stock_exchange_type: str,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> Union[Dict[str, Any], Awaitable[Dict[str, Any]]]:
        """시가대비등락률 요청

        Args:
            sort_type (str)                = 정렬구분 (1:시가, 2:고가, 3:저가, 4:기준가)
            trade_quantity_condition (str) = 거래량조건 (0000:전체조회, 0010:만주이상, ...)
            market_type (str)              = 시장구분 (000:전체, 001:코스피, 101:코스닥)
            updown_include (str)           = 상하한포함 (0:불포함, 1:포함)
            stock_condition (str)          = 종목조건 (0:전체조회, 1:관리종목제외, ...)
            credit_condition (str)         = 신용조건 (0:전체조회, 1:신용융자A군, ...)
            trade_price_condition (str)    = 거래대금조건 (0:전체조회, 3:3천만원이상, ...)
            fluctuation_condition (str)    = 등락조건 (1:상위, 2:하위)
            stock_exchange_type (str)      = 거래소구분 (1:KRX, 2:NXT, 3:통합)
            cont_yn (str, optional)        = 연속조회여부. Defaults to "N".
            next_key (str, optional)       = 연속조회키. Defaults to "".

        Returns:
            Union[Dict[str, Any], Awaitable[Dict[str, Any]]]: 응답 데이터
            {
                "open_pric_pre_flu_rt": [
                    {
                        "stk_cd": "005930",
                        "stk_nm": "삼성전자",
                        "cur_prc": "+74800",
                        "pred_pre_sig": "1",
                        "pred_pre": "+17200",
                        "flu_rt": "+29.86",
                        "open_pric": "+65000",
                        "high_pric": "+74800",
                        "low_pric": "-57000",
                        "open_pric_pre": "+15.08",
                        "now_trde_qty": "448203",
                        "cntr_str": "346.54"
                    },
                    ...
                ]
            }
        """
        # 헤더 구성
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10028"
        }
        
        # 요청 데이터 구성
        data = {
            "sort_tp": sort_type,
            "trde_qty_cnd": trade_quantity_condition,
            "mrkt_tp": market_type,
            "updown_incls": updown_include,
            "stk_cnd": stock_condition,
            "crd_cnd": credit_condition,
            "trde_prica_cnd": trade_price_condition,
            "flu_cnd": fluctuation_condition,
            "stex_tp": stock_exchange_type
        }

        return self._execute_request("POST", json=data, headers=headers)
    
    def trading_agent_supply_demand_analysis_request_ka10043(
        self,
        stock_code: str,
        start_date: str,
        end_date: str,
        query_date_type: str,
        point_type: str,
        period: str,
        sort_base: str,
        member_code: str,
        stock_exchange_type: str,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> Union[Dict[str, Any], Awaitable[Dict[str, Any]]]:
        """거래원매물대분석 요청

        Args:
            stock_code (str)          = 종목코드 (예: "005930")
            start_date (str)          = 시작일자 (YYYYMMDD 형식)
            end_date (str)            = 종료일자 (YYYYMMDD 형식)
            query_date_type (str)     = 조회기간구분 (0:기간으로 조회, 1:시작일자, 종료일자로 조회)
            point_type (str)          = 시점구분 (0:당일, 1:전일)
            period (str)              = 기간 (5:5일, 10:10일, 20:20일, 40:40일, 60:60일, 120:120일)
            sort_base (str)           = 정렬기준 (1:종가순, 2:날짜순)
            member_code (str)         = 회원사코드 (회원사 코드는 ka10102 조회)
            stock_exchange_type (str) = 거래소구분 (1:KRX, 2:NXT, 3:통합)
            cont_yn (str, optional)   = 연속조회여부. Defaults to "N".
            next_key (str, optional)  = 연속조회키. Defaults to "".

        Returns:
            Union[Dict[str, Any], Awaitable[Dict[str, Any]]]: 응답 데이터
            {
                "trde_ori_prps_anly": [
                    {
                        "dt": "20241105",
                        "close_pric": "135300",
                        "pre_sig": "2",
                        "pred_pre": "+1700",
                        "sel_qty": "43",
                        "buy_qty": "1090",
                        "netprps_qty": "1047",
                        "trde_qty_sum": "1133",
                        "trde_wght": "+1317.44"
                    },
                    ...
                ]
            }
        """
        # 헤더 구성
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10043"
        }
        
        # 요청 데이터 구성
        data = {
            "stk_cd": stock_code,
            "strt_dt": start_date,
            "end_dt": end_date,
            "qry_dt_tp": query_date_type,
            "pot_tp": point_type,
            "dt": period,
            "sort_base": sort_base,
            "mmcm_cd": member_code,
            "stex_tp": stock_exchange_type
        }

        return self._execute_request("POST", json=data, headers=headers)

    def trading_agent_instant_trading_volume_request_ka10052(
        self,
        member_code: str,
        stock_code: str = "",
        market_type: str = "0",
        quantity_type: str = "0",
        price_type: str = "0",
        stock_exchange_type: str = "3",
        cont_yn: str = "N",
        next_key: str = ""
    ) -> Union[Dict[str, Any], Awaitable[Dict[str, Any]]]:
        """거래원순간거래량 요청

        Args:
            member_code (str): 회원사코드 (회원사 코드는 ka10102 조회)
            stock_code (str, optional): 종목코드. Defaults to "".
            market_type (str, optional): 시장구분 (0:전체, 1:코스피, 2:코스닥, 3:종목). Defaults to "0".
            quantity_type (str, optional): 수량구분 (0:전체, 1:1000주, 2:2000주, 10:10000주, ...). Defaults to "0".
            price_type (str, optional): 가격구분 (0:전체, 1:1천원 미만, 8:1천원 이상, ...). Defaults to "0".
            stock_exchange_type (str, optional): 거래소구분 (1:KRX, 2:NXT, 3:통합). Defaults to "3".
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            Union[Dict[str, Any], Awaitable[Dict[str, Any]]]: 응답 데이터
            {
                "trde_ori_mont_trde_qty": [
                    {
                        "tm": "161437",
                        "stk_cd": "005930",
                        "stk_nm": "삼성전자",
                        "trde_ori_nm": "다이와",
                        "tp": "-매도",
                        "mont_trde_qty": "-399928",
                        "acc_netprps": "-1073004",
                        "cur_prc": "+57700",
                        "pred_pre_sig": "2",
                        "pred_pre": "400",
                        "flu_rt": "+0.70"
                    },
                    ...
                ]
            }
        """
        # 헤더 구성
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10052"
        }
        
        # 요청 데이터 구성
        data = {
            "mmcm_cd": member_code,
            "stk_cd": stock_code,
            "mrkt_tp": market_type,
            "qty_tp": quantity_type,
            "pric_tp": price_type,
            "stex_tp": stock_exchange_type
        }

        return self._execute_request("POST", json=data, headers=headers)
    
    def volatility_mitigation_device_triggered_stocks_request_ka10054(
        self,
        market_type: str,
        before_market_type: str,
        stock_code: str = "",
        motion_type: str = "0",
        skip_stock: str = "000000000",
        trade_quantity_type: str = "0",
        min_trade_quantity: str = "0",
        max_trade_quantity: str = "0",
        trade_price_type: str = "0",
        min_trade_price: str = "0",
        max_trade_price: str = "0",
        motion_direction: str = "0",
        stock_exchange_type: str = "3",
        cont_yn: str = "N",
        next_key: str = ""
    ) -> Union[Dict[str, Any], Awaitable[Dict[str, Any]]]:
        """변동성완화장치발동종목 요청

        Args:
            market_type (str): 시장구분 (000:전체, 001:코스피, 101:코스닥)
            before_market_type (str): 장전구분 (0:전체, 1:정규시장, 2:시간외단일가)
            stock_code (str, optional): 종목코드. Defaults to "".
            motion_type (str, optional): 발동구분 (0:전체, 1:정적VI, 2:동적VI, 3:동적VI + 정적VI). Defaults to "0".
            skip_stock (str, optional): 제외종목 (000000000:전종목포함, 111111111:전종목제외). Defaults to "000000000".
            trade_quantity_type (str, optional): 거래량구분 (0:사용안함, 1:사용). Defaults to "0".
            min_trade_quantity (str, optional): 최소거래량. Defaults to "0".
            max_trade_quantity (str, optional): 최대거래량. Defaults to "0".
            trade_price_type (str, optional): 거래대금구분 (0:사용안함, 1:사용). Defaults to "0".
            min_trade_price (str, optional): 최소거래대금. Defaults to "0".
            max_trade_price (str, optional): 최대거래대금. Defaults to "0".
            motion_direction (str, optional): 발동방향 (0:전체, 1:상승, 2:하락). Defaults to "0".
            stock_exchange_type (str, optional): 거래소구분 (1:KRX, 2:NXT, 3:통합). Defaults to "3".
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            Union[Dict[str, Any], Awaitable[Dict[str, Any]]]: 응답 데이터
            {
                "motn_stk": [
                    {
                        "stk_cd": "005930",
                        "stk_nm": "삼성전자",
                        "acc_trde_qty": "1105968",
                        "motn_pric": "67000",
                        "dynm_dispty_rt": "+9.30",
                        "trde_cntr_proc_time": "172311",
                        "virelis_time": "172511",
                        "viaplc_tp": "동적",
                        "dynm_stdpc": "61300",
                        "static_stdpc": "0",
                        "static_dispty_rt": "0.00",
                        "open_pric_pre_flu_rt": "+16.93",
                        "vimotn_cnt": "23",
                        "stex_tp": "NXT"
                    },
                    ...
                ]
            }
        """
        # 헤더 구성
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10054"
        }
        
        # 요청 데이터 구성
        data = {
            "mrkt_tp": market_type,
            "bf_mkrt_tp": before_market_type,
            "stk_cd": stock_code,
            "motn_tp": motion_type,
            "skip_stk": skip_stock,
            "trde_qty_tp": trade_quantity_type,
            "min_trde_qty": min_trade_quantity,
            "max_trde_qty": max_trade_quantity,
            "trde_prica_tp": trade_price_type,
            "min_trde_prica": min_trade_price,
            "max_trde_prica": max_trade_price,
            "motn_drc": motion_direction,
            "stex_tp": stock_exchange_type
        }

        return self._execute_request("POST", json=data, headers=headers)

    def today_vs_previous_day_execution_volume_request_ka10055(
        self,
        stock_code: str,
        today_or_previous: str,
        market_type: str = "",
        stock_exchange_type: str = "",
        cont_yn: str = "N",
        next_key: str = ""
    ) -> Union[Dict[str, Any], Awaitable[Dict[str, Any]]]:
        """당일전일체결량 요청

        Args:
            stock_code (str): 종목코드 (예: "005930", "KRX:039490")
            today_or_previous (str): 당일전일 (1:당일, 2:전일)
            market_type (str, optional): 시장구분. Defaults to "".
            stock_exchange_type (str, optional): 거래소구분. Defaults to "".
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            Union[Dict[str, Any], Awaitable[Dict[str, Any]]]: 응답 데이터
            {
                "tdy_pred_cntr_qty": [
                    {
                        "cntr_tm": "171945",
                        "cntr_pric": "+74800",
                        "pred_pre_sig": "1",
                        "pred_pre": "+17200",
                        "flu_rt": "+29.86",
                        "cntr_qty": "-1793",
                        "acc_trde_qty": "446203",
                        "acc_trde_prica": "33225"
                    },
                    ...
                ]
            }
        """
        # 헤더 구성
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10055"
        }
        
        # 요청 데이터 구성
        data = {
            "stk_cd": stock_code,
            "tdy_pred": today_or_previous
        }

        return self._execute_request("POST", json=data, headers=headers)

    def daily_trading_stocks_by_investor_type_request_ka10058(
        self,
        start_date: str,
        end_date: str,
        trade_type: str,
        market_type: str,
        investor_type: str,
        stock_exchange_type: str,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> Union[Dict[str, Any], Awaitable[Dict[str, Any]]]:
        """투자자별일별매매종목 요청

        Args:
            start_date (str): 시작일자 (YYYYMMDD)
            end_date (str): 종료일자 (YYYYMMDD)
            trade_type (str): 매매구분 (순매도:1, 순매수:2)
            market_type (str): 시장구분 (001:코스피, 101:코스닥)
            investor_type (str): 투자자구분 (8000:개인, 9000:외국인, 1000:금융투자, 3000:투신, 
                                5000:기타금융, 4000:은행, 2000:보험, 6000:연기금, 7000:국가, 
                                7100:기타법인, 9999:기관계)
            stock_exchange_type (str): 거래소구분 (1:KRX, 2:NXT, 3:통합)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            Union[Dict[str, Any], Awaitable[Dict[str, Any]]]: 응답 데이터
            {
                "invsr_daly_trde_stk": [
                    {
                        "stk_cd": "005930",
                        "stk_nm": "삼성전자",
                        "netslmt_qty": "+4464",
                        "netslmt_amt": "+25467",
                        "prsm_avg_pric": "57056",
                        "cur_prc": "+61300",
                        "pre_sig": "2",
                        "pred_pre": "+4000",
                        "avg_pric_pre": "+4244",
                        "pre_rt": "+7.43",
                        "dt_trde_qty": "1554171"
                    },
                    ...
                ]
            }
        """
        # 헤더 구성
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10058"
        }
        
        # 요청 데이터 구성
        data = {
            "strt_dt": start_date,
            "end_dt": end_date,
            "trde_tp": trade_type,
            "mrkt_tp": market_type,
            "invsr_tp": investor_type,
            "stex_tp": stock_exchange_type
        }

        return self._execute_request("POST", json=data, headers=headers)

    def stock_data_by_investor_institution_request_ka10059(
        self,
        date: str,
        stock_code: str,
        amount_quantity_type: str,
        trade_type: str,
        unit_type: str,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> Union[Dict[str, Any], Awaitable[Dict[str, Any]]]:
        """종목별투자자기관별 요청

        Args:
            date (str): 일자 (YYYYMMDD)
            stock_code (str): 종목코드 (예: "005930", "KRX:039490")
            amount_quantity_type (str): 금액수량구분 (1:금액, 2:수량)
            trade_type (str): 매매구분 (0:순매수, 1:매수, 2:매도)
            unit_type (str): 단위구분 (1000:천주, 1:단주)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            Union[Dict[str, Any], Awaitable[Dict[str, Any]]]: 응답 데이터
            {
                "stk_invsr_orgn": [
                    {
                        "dt": "20241107",
                        "cur_prc": "+61300",
                        "pre_sig": "2",
                        "pred_pre": "+4000",
                        "flu_rt": "+698",
                        "acc_trde_qty": "1105968",
                        "acc_trde_prica": "64215",
                        "ind_invsr": "1584",
                        "frgnr_invsr": "-61779",
                        "orgn": "60195",
                        "fnnc_invt": "25514",
                        "insrnc": "0",
                        "invtrt": "0",
                        "etc_fnnc": "34619",
                        "bank": "4",
                        "penfnd_etc": "-1",
                        "samo_fund": "58",
                        "natn": "0",
                        "etc_corp": "0",
                        "natfor": "1"
                    },
                    ...
                ]
            }
        """
        # 헤더 구성
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10059"
        }
        
        # 요청 데이터 구성
        data = {
            "dt": date,
            "stk_cd": stock_code,
            "amt_qty_tp": amount_quantity_type,
            "trde_tp": trade_type,
            "unit_tp": unit_type
        }

        return self._execute_request("POST", json=data, headers=headers)

    def aggregate_stock_data_by_investor_institution_request_ka10061(
        self,
        stock_code: str,
        start_date: str,
        end_date: str,
        amount_quantity_type: str,
        trade_type: str,
        unit_type: str,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> Union[Dict[str, Any], Awaitable[Dict[str, Any]]]:
        """종목별투자자기관별합계 요청

        Args:
            stock_code (str): 종목코드 (예: "005930", "KRX:039490")
            start_date (str): 시작일자 (YYYYMMDD)
            end_date (str): 종료일자 (YYYYMMDD)
            amount_quantity_type (str): 금액수량구분 (1:금액, 2:수량)
            trade_type (str): 매매구분 (0:순매수, 1:매수, 2:매도)
            unit_type (str): 단위구분 (1000:천주, 1:단주)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            Union[Dict[str, Any], Awaitable[Dict[str, Any]]]: 응답 데이터
            {
                "stk_invsr_orgn_tot": [
                    {
                        "ind_invsr": "--28837",
                        "frgnr_invsr": "--40142",
                        "orgn": "+64891",
                        "fnnc_invt": "+72584",
                        "insrnc": "--9071",
                        "invtrt": "--7790",
                        "etc_fnnc": "+35307",
                        "bank": "+526",
                        "penfnd_etc": "--22783",
                        "samo_fund": "--3881",
                        "natn": "0",
                        "etc_corp": "+1974",
                        "natfor": "+2114"
                    }
                ]
            }
        """
        # 헤더 구성
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10061"
        }
        
        # 요청 데이터 구성
        data = {
            "stk_cd": stock_code,
            "strt_dt": start_date,
            "end_dt": end_date,
            "amt_qty_tp": amount_quantity_type,
            "trde_tp": trade_type,
            "unit_tp": unit_type
        }

        return self._execute_request("POST", json=data, headers=headers)

    def today_vs_previous_day_execution_request_ka10084(
        self,
        stock_code: str,
        today_or_previous: str,
        tick_or_minute: str,
        time: str = "",
        cont_yn: str = "N",
        next_key: str = ""
    ) -> Union[Dict[str, Any], Awaitable[Dict[str, Any]]]:
        """당일전일체결 요청

        Args:
            stock_code (str): 종목코드 (예: "005930", "KRX:039490")
            today_or_previous (str): 당일전일 (당일:1, 전일:2)
            tick_or_minute (str): 틱분 (0:틱, 1:분)
            time (str, optional): 조회시간 4자리 (예: 0900, 1430). Defaults to "".
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            Union[Dict[str, Any], Awaitable[Dict[str, Any]]]: 응답 데이터
            {
                "tdy_pred_cntr": [
                    {
                        "tm": "112711",
                        "cur_prc": "+128300",
                        "pred_pre": "+700",
                        "pre_rt": "+0.55",
                        "pri_sel_bid_unit": "-0",
                        "pri_buy_bid_unit": "+128300",
                        "cntr_trde_qty": "-1",
                        "sign": "2",
                        "acc_trde_qty": "2",
                        "acc_trde_prica": "0",
                        "cntr_str": "0.00"
                    },
                    ...
                ]
            }
        """
        # 헤더 구성
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10084"
        }
        
        # 요청 데이터 구성
        data = {
            "stk_cd": stock_code,
            "tdy_pred": today_or_previous,
            "tic_min": tick_or_minute,
            "tm": time
        }

        return self._execute_request("POST", json=data, headers=headers)
    
    def watchlist_stock_information_request_ka10095(
        self,
        stock_code: str,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> Union[Dict[str, Any], Awaitable[Dict[str, Any]]]:
        """관심종목정보 요청

        Args:
            stock_code (str): 종목코드 (여러개 입력시 |로 구분)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            Union[Dict[str, Any], Awaitable[Dict[str, Any]]]: 응답 데이터
            {
                "atn_stk_infr": [
                    {
                        "stk_cd": "005930",
                        "stk_nm": "삼성전자",
                        "cur_prc": "+156600",
                        "base_pric": "121700",
                        "pred_pre": "+34900",
                        "pred_pre_sig": "2",
                        "flu_rt": "+28.68",
                        "trde_qty": "118636",
                        "trde_prica": "14889",
                        "cntr_qty": "-1",
                        "cntr_str": "172.01",
                        "pred_trde_qty_pre": "+1995.22",
                        "sel_bid": "+156700",
                        "buy_bid": "+156600",
                        ...
                    }
                ]
            }
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10095"
        }
        data = {
            "stk_cd": stock_code
        }
        return self._execute_request("POST", json=data, headers=headers)
        
    def stock_information_list_request_ka10099(
        self,
        market_type: str,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> Union[Dict[str, Any], Awaitable[Dict[str, Any]]]:
        """종목정보 리스트 요청

        Args:
            market_type (str): 시장구분 (0:코스피,10:코스닥,3:ELW,8:ETF,30:K-OTC,50:코넥스,5:신주인수권,4:뮤추얼펀드,6:리츠,9:하이일드)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            Union[Dict[str, Any], Awaitable[Dict[str, Any]]]: 응답 데이터
            {
                "list": [
                    {
                        "code": "005930",
                        "name": "삼성전자",
                        "listCount": "0000000123759593",
                        "auditInfo": "투자주의환기종목",
                        "regDay": "20091204",
                        "lastPrice": "00000197",
                        "state": "관리종목",
                        "marketCode": "10",
                        "marketName": "코스닥",
                        ...
                    }
                ]
            }
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10099"
        }
        data = {
            "mrkt_tp": market_type
        }
        return self._execute_request("POST", json=data, headers=headers)
        
    def stock_information_inquiry_request_ka10100(
        self,
        stock_code: str,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> Union[Dict[str, Any], Awaitable[Dict[str, Any]]]:
        """종목정보 조회 요청

        Args:
            stock_code (str): 종목코드 (6자리)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            Union[Dict[str, Any], Awaitable[Dict[str, Any]]]: 응답 데이터
            {
                "code": "005930",
                "name": "삼성전자",
                "listCount": "0000000026034239",
                "auditInfo": "정상",
                "regDay": "20090803",
                "lastPrice": "00136000",
                "state": "증거금20%|담보대출|신용가능",
                "marketCode": "0",
                "marketName": "거래소",
                "upName": "금융업",
                "upSizeName": "대형주",
                "companyClassName": "",
                "orderWarning": "0",
                "nxtEnable": "Y",
                "return_code": 0,
                "return_msg": "정상적으로 처리되었습니다"
            }
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10100"
        }
        data = {
            "stk_cd": stock_code
        }
        return self._execute_request("POST", json=data, headers=headers)
        
    def industry_code_list_request_ka10101(
        self,
        market_type: str,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> Union[Dict[str, Any], Awaitable[Dict[str, Any]]]:
        """산업코드 리스트 요청

        Args:
            market_type (str): 시장구분 (0:코스피, 1:코스닥, 2:KOSPI200, 4:KOSPI100, 7:KRX100)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            Union[Dict[str, Any], Awaitable[Dict[str, Any]]]: 응답 데이터
            {
                "list": [
                    {
                        "marketCode": "0",
                        "code": "001",
                        "name": "종합(KOSPI)",
                        "group": "1"
                    },
                    ...
                ]
            }
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10101"
        }
        data = {
            "mrkt_tp": market_type
        }
        return self._execute_request("POST", json=data, headers=headers)

    def member_company_list_request_ka10102(
        self,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> Union[Dict[str, Any], Awaitable[Dict[str, Any]]]:
        """회원사코드 리스트 요청

        Args:
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            Union[Dict[str, Any], Awaitable[Dict[str, Any]]]: 응답 데이터
            {
                "list": [
                    {
                        "code": "001",
                        "name": "교  보",
                        "gb": "0"
                    },
                    ...
                ]
            }
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10102"
        }
        data = {}
        return self._execute_request("POST", json=data, headers=headers)

    def top_50_program_buy_request_ka90003(
        self,
        trade_upper_type: str,
        amount_quantity_type: str,
        market_type: str,
        stock_exchange_type: str,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> Union[Dict[str, Any], Awaitable[Dict[str, Any]]]:
        """프로그램순매수상위50 요청

        Args:
            trade_upper_type (str): 매매상위구분 (1:순매도상위, 2:순매수상위)
            amount_quantity_type (str): 금액수량구분 (1:금액, 2:수량)
            market_type (str): 시장구분 (P00101:코스피, P10102:코스닥)
            stock_exchange_type (str): 거래소구분 (1:KRX, 2:NXT, 3:통합)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            Union[Dict[str, Any], Awaitable[Dict[str, Any]]]: 응답 데이터
            {
                "prm_netprps_upper_50": [
                    {
                        "rank": "1",
                        "stk_cd": "005930",
                        "stk_nm": "삼성전자",
                        "cur_prc": "123000",
                        "flu_sig": "+",
                        "pred_pre": "+1000",
                        "flu_rt": "+0.82",
                        "acc_trde_qty": "1234567",
                        "prm_sell_amt": "1000000",
                        "prm_buy_amt": "2000000",
                        "prm_netprps_amt": "1000000"
                    },
                    ...
                ]
            }
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka90003"
        }
        data = {
            "trde_upper_tp": trade_upper_type,
            "amt_qty_tp": amount_quantity_type,
            "mrkt_tp": market_type,
            "stex_tp": stock_exchange_type
        }
        return self._execute_request("POST", json=data, headers=headers)

    def stock_wise_program_trading_status_request_ka90004(
        self,
        date: str,
        market_type: str,
        stock_exchange_type: str,
        cont_yn: str = "N",
        next_key: str = ""
    ) -> Union[Dict[str, Any], Awaitable[Dict[str, Any]]]:
        """종목별 프로그램 매매상태 요청

        Args:
            date (str): 일자 (YYYYMMDD)
            market_type (str): 시장구분 (P00101:코스피, P10102:코스닥)
            stock_exchange_type (str): 거래소구분 (1:KRX, 2:NXT, 3:통합)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            Union[Dict[str, Any], Awaitable[Dict[str, Any]]]: 응답 데이터
            {
                "tot_1": "0",
                "tot_2": "2",
                "tot_3": "0",
                "tot_4": "2",
                "tot_5": "0",
                "tot_6": "",
                "stk_prm_trde_prst": [
                    {
                        "stk_cd": "005930",
                        "stk_nm": "삼성전자",
                        "cur_prc": "-75000",
                        "flu_sig": "5",
                        "pred_pre": "-2800",
                        "buy_cntr_qty": "0",
                        "buy_cntr_amt": "0",
                        "sel_cntr_qty": "0",
                        "sel_cntr_amt": "0",
                        "netprps_prica": "0",
                        "all_trde_rt": "+0.00"
                    },
                    ...
                ]
            }
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka90004"
        }
        data = {
            "dt": date,
            "mrkt_tp": market_type,
            "stex_tp": stock_exchange_type
        }
        return self._execute_request("POST", json=data, headers=headers)
