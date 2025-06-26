from kiwoom_rest_api.core.base_api import KiwoomBaseAPI
from typing import Union, Dict, Any, Awaitable

class RankInfo(KiwoomBaseAPI):
    """한국 주식 랭크 정보 API를 제공하는 클래스"""
    
    def __init__(
        self, 
        base_url: str = None, 
        token_manager=None, 
        use_async: bool = False,
        resource_url: str = "/api/dostk/rkinfo"
    ):
        """
        RankInfo 클래스 초기화
        
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
        
   
        

    def top_order_book_volume_request_ka10020(
        self,
        mrkt_tp: str,
        sort_tp: str,
        trde_qty_tp: str,
        stk_cnd: str,
        crd_cnd: str,
        stex_tp: str,
        cont_yn: str = "N",
        next_key: str = "",
    ) -> dict:
        """호가잔량상위를 조회합니다.

        Args:
            mrkt_tp (str): 시장구분 (001:코스피, 101:코스닥)
            sort_tp (str): 정렬구분
                - 1: 순매수잔량순
                - 2: 순매도잔량순
                - 3: 매수비율순
                - 4: 매도비율순
            trde_qty_tp (str): 거래량구분
                - 0000: 장시작전(0주이상)
                - 0010: 만주이상
                - 0050: 5만주이상
                - 00100: 10만주이상
            stk_cnd (str): 종목조건
                - 0: 전체조회
                - 1: 관리종목제외
                - 5: 증100제외
                - 6: 증100만보기
                - 7: 증40만보기
                - 8: 증30만보기
                - 9: 증20만보기
            crd_cnd (str): 신용조건
                - 0: 전체조회
                - 1: 신용융자A군
                - 2: 신용융자B군
                - 3: 신용융자C군
                - 4: 신용융자D군
                - 9: 신용융자전체
            stex_tp (str): 거래소구분 (1:KRX, 2:NXT, 3:통합)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 호가잔량상위 데이터
                {
                    "bid_req_upper": [  # 호가잔량상위
                        {
                            "stk_cd": str,  # 종목코드
                            "stk_nm": str,  # 종목명
                            "cur_prc": str,  # 현재가
                            "pred_pre_sig": str,  # 전일대비기호
                            "pred_pre": str,  # 전일대비
                            "trde_qty": str,  # 거래량
                            "tot_sel_req": str,  # 총매도잔량
                            "tot_buy_req": str,  # 총매수잔량
                            "netprps_req": str,  # 순매수잔량
                            "buy_rt": str,  # 매수비율
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.rank_info.top_order_book_volume_request_ka10020(
            ...     mrkt_tp="001",
            ...     sort_tp="1",
            ...     trde_qty_tp="0000",
            ...     stk_cnd="0",
            ...     crd_cnd="0",
            ...     stex_tp="1"
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10020",
        }

        data = {
            "mrkt_tp": mrkt_tp,
            "sort_tp": sort_tp,
            "trde_qty_tp": trde_qty_tp,
            "stk_cnd": stk_cnd,
            "crd_cnd": crd_cnd,
            "stex_tp": stex_tp,
        }

        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
        
    def sudden_increase_order_book_volume_request_ka10021(
        self,
        mrkt_tp: str,
        trde_tp: str,
        sort_tp: str,
        tm_tp: str,
        trde_qty_tp: str,
        stk_cnd: str,
        stex_tp: str,
        cont_yn: str = "N",
        next_key: str = "",
    ) -> dict:
        """호가잔량급증을 조회합니다.

        Args:
            mrkt_tp (str): 시장구분 (001:코스피, 101:코스닥)
            trde_tp (str): 매매구분
                - 1: 매수잔량
                - 2: 매도잔량
            sort_tp (str): 정렬구분
                - 1: 급증량
                - 2: 급증률
            tm_tp (str): 시간구분 (분 입력)
            trde_qty_tp (str): 거래량구분
                - 1: 천주이상
                - 5: 5천주이상
                - 10: 만주이상
                - 50: 5만주이상
                - 100: 10만주이상
            stk_cnd (str): 종목조건
                - 0: 전체조회
                - 1: 관리종목제외
                - 5: 증100제외
                - 6: 증100만보기
                - 7: 증40만보기
                - 8: 증30만보기
                - 9: 증20만보기
            stex_tp (str): 거래소구분 (1:KRX, 2:NXT, 3:통합)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 호가잔량급증 데이터
                {
                    "bid_req_sdnin": [  # 호가잔량급증
                        {
                            "stk_cd": str,  # 종목코드
                            "stk_nm": str,  # 종목명
                            "cur_prc": str,  # 현재가
                            "pred_pre_sig": str,  # 전일대비기호
                            "pred_pre": str,  # 전일대비
                            "int": str,  # 기준률
                            "now": str,  # 현재
                            "sdnin_qty": str,  # 급증수량
                            "sdnin_rt": str,  # 급증률
                            "tot_buy_qty": str,  # 총매수량
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.rank_info.sudden_increase_order_book_volume_request_ka10021(
            ...     mrkt_tp="001",
            ...     trde_tp="1",
            ...     sort_tp="1",
            ...     tm_tp="30",
            ...     trde_qty_tp="1",
            ...     stk_cnd="0",
            ...     stex_tp="3"
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10021",
        }

        data = {
            "mrkt_tp": mrkt_tp,
            "trde_tp": trde_tp,
            "sort_tp": sort_tp,
            "tm_tp": tm_tp,
            "trde_qty_tp": trde_qty_tp,
            "stk_cnd": stk_cnd,
            "stex_tp": stex_tp,
        }

        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
        
    def sudden_increase_order_ratio_request_ka10022(
        self,
        mrkt_tp: str,
        rt_tp: str,
        tm_tp: str,
        trde_qty_tp: str,
        stk_cnd: str,
        stex_tp: str,
        cont_yn: str = "N",
        next_key: str = "",
    ) -> dict:
        """잔량율급증을 조회합니다.

        Args:
            mrkt_tp (str): 시장구분 (001:코스피, 101:코스닥)
            rt_tp (str): 비율구분
                - 1: 매수/매도비율
                - 2: 매도/매수비율
            tm_tp (str): 시간구분 (분 입력)
            trde_qty_tp (str): 거래량구분
                - 5: 5천주이상
                - 10: 만주이상
                - 50: 5만주이상
                - 100: 10만주이상
            stk_cnd (str): 종목조건
                - 0: 전체조회
                - 1: 관리종목제외
                - 5: 증100제외
                - 6: 증100만보기
                - 7: 증40만보기
                - 8: 증30만보기
                - 9: 증20만보기
            stex_tp (str): 거래소구분 (1:KRX, 2:NXT, 3:통합)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 잔량율급증 데이터
                {
                    "req_rt_sdnin": [  # 잔량율급증
                        {
                            "stk_cd": str,  # 종목코드
                            "stk_nm": str,  # 종목명
                            "cur_prc": str,  # 현재가
                            "pred_pre_sig": str,  # 전일대비기호
                            "pred_pre": str,  # 전일대비
                            "int": str,  # 기준률
                            "now_rt": str,  # 현재비율
                            "sdnin_rt": str,  # 급증률
                            "tot_sel_req": str,  # 총매도잔량
                            "tot_buy_req": str,  # 총매수잔량
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.rank_info.sudden_increase_order_ratio_request_ka10022(
            ...     mrkt_tp="001",
            ...     rt_tp="1",
            ...     tm_tp="1",
            ...     trde_qty_tp="5",
            ...     stk_cnd="0",
            ...     stex_tp="3"
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10022",
        }

        data = {
            "mrkt_tp": mrkt_tp,
            "rt_tp": rt_tp,
            "tm_tp": tm_tp,
            "trde_qty_tp": trde_qty_tp,
            "stk_cnd": stk_cnd,
            "stex_tp": stex_tp,
        }

        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
    
    def sudden_increase_trading_volume_request_ka10023(
        self,
        mrkt_tp: str,
        sort_tp: str,
        tm_tp: str,
        trde_qty_tp: str,
        stk_cnd: str,
        pric_tp: str,
        stex_tp: str,
        tm: str = "",
        cont_yn: str = "N",
        next_key: str = "",
    ) -> dict:
        """거래량급증을 조회합니다.

        Args:
            mrkt_tp (str): 시장구분
                - 000: 전체
                - 001: 코스피
                - 101: 코스닥
            sort_tp (str): 정렬구분
                - 1: 급증량
                - 2: 급증률
                - 3: 급감량
                - 4: 급감률
            tm_tp (str): 시간구분
                - 1: 분
                - 2: 전일
            trde_qty_tp (str): 거래량구분
                - 5: 5천주이상
                - 10: 만주이상
                - 50: 5만주이상
                - 100: 10만주이상
                - 200: 20만주이상
                - 300: 30만주이상
                - 500: 50만주이상
                - 1000: 백만주이상
            stk_cnd (str): 종목조건
                - 0: 전체조회
                - 1: 관리종목제외
                - 3: 우선주제외
                - 11: 정리매매종목제외
                - 4: 관리종목,우선주제외
                - 5: 증100제외
                - 6: 증100만보기
                - 13: 증60만보기
                - 12: 증50만보기
                - 7: 증40만보기
                - 8: 증30만보기
                - 9: 증20만보기
                - 17: ETN제외
                - 14: ETF제외
                - 18: ETF+ETN제외
                - 15: 스팩제외
                - 20: ETF+ETN+스팩제외
            pric_tp (str): 가격구분
                - 0: 전체조회
                - 2: 5만원이상
                - 5: 1만원이상
                - 6: 5천원이상
                - 8: 1천원이상
                - 9: 10만원이상
            stex_tp (str): 거래소구분 (1:KRX, 2:NXT, 3:통합)
            tm (str, optional): 시간(분 입력). Defaults to "".
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 거래량급증 데이터
                {
                    "trde_qty_sdnin": [  # 거래량급증
                        {
                            "stk_cd": str,  # 종목코드
                            "stk_nm": str,  # 종목명
                            "cur_prc": str,  # 현재가
                            "pred_pre_sig": str,  # 전일대비기호
                            "pred_pre": str,  # 전일대비
                            "flu_rt": str,  # 등락률
                            "prev_trde_qty": str,  # 이전거래량
                            "now_trde_qty": str,  # 현재거래량
                            "sdnin_qty": str,  # 급증량
                            "sdnin_rt": str,  # 급증률
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.rank_info.sudden_increase_trading_volume_request_ka10023(
            ...     mrkt_tp="000",
            ...     sort_tp="1",
            ...     tm_tp="2",
            ...     trde_qty_tp="5",
            ...     stk_cnd="0",
            ...     pric_tp="0",
            ...     stex_tp="3"
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10023",
        }

        data = {
            "mrkt_tp": mrkt_tp,
            "sort_tp": sort_tp,
            "tm_tp": tm_tp,
            "trde_qty_tp": trde_qty_tp,
            "tm": tm,
            "stk_cnd": stk_cnd,
            "pric_tp": pric_tp,
            "stex_tp": stex_tp,
        }

        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
        
    def top_day_over_day_change_rate_request_ka10027(
        self,
        mrkt_tp: str,
        sort_tp: str,
        trde_qty_cnd: str,
        stk_cnd: str,
        crd_cnd: str,
        updown_incls: str,
        pric_cnd: str,
        trde_prica_cnd: str,
        stex_tp: str,
        cont_yn: str = "N",
        next_key: str = "",
    ) -> dict:
        """전일대비 등락률 상위 종목을 조회합니다.

        Args:
            mrkt_tp (str): 시장구분
                - 000: 전체
                - 001: 코스피
                - 101: 코스닥
            sort_tp (str): 정렬구분
                - 1: 상승률
                - 2: 상승폭
                - 3: 하락률
                - 4: 하락폭
                - 5: 보합
            trde_qty_cnd (str): 거래량조건
                - 0000: 전체조회
                - 0010: 만주이상
                - 0050: 5만주이상
                - 0100: 10만주이상
                - 0150: 15만주이상
                - 0200: 20만주이상
                - 0300: 30만주이상
                - 0500: 50만주이상
                - 1000: 백만주이상
            stk_cnd (str): 종목조건
                - 0: 전체조회
                - 1: 관리종목제외
                - 4: 우선주+관리주제외
                - 3: 우선주제외
                - 5: 증100제외
                - 6: 증100만보기
                - 7: 증40만보기
                - 8: 증30만보기
                - 9: 증20만보기
                - 11: 정리매매종목제외
                - 12: 증50만보기
                - 13: 증60만보기
                - 14: ETF제외
                - 15: 스펙제외
                - 16: ETF+ETN제외
            crd_cnd (str): 신용조건
                - 0: 전체조회
                - 1: 신용융자A군
                - 2: 신용융자B군
                - 3: 신용융자C군
                - 4: 신용융자D군
                - 9: 신용융자전체
            updown_incls (str): 상하한포함
                - 0: 불 포함
                - 1: 포함
            pric_cnd (str): 가격조건
                - 0: 전체조회
                - 1: 1천원미만
                - 2: 1천원~2천원
                - 3: 2천원~5천원
                - 4: 5천원~1만원
                - 5: 1만원이상
                - 8: 1천원이상
                - 10: 1만원미만
            trde_prica_cnd (str): 거래대금조건
                - 0: 전체조회
                - 3: 3천만원이상
                - 5: 5천만원이상
                - 10: 1억원이상
                - 30: 3억원이상
                - 50: 5억원이상
                - 100: 10억원이상
                - 300: 30억원이상
                - 500: 50억원이상
                - 1000: 100억원이상
                - 3000: 300억원이상
                - 5000: 500억원이상
            stex_tp (str): 거래소구분 (1:KRX, 2:NXT, 3:통합)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 전일대비 등락률 상위 종목 데이터
                {
                    "pred_pre_flu_rt_upper": [  # 전일대비등락률상위
                        {
                            "stk_cls": str,  # 종목분류
                            "stk_cd": str,  # 종목코드
                            "stk_nm": str,  # 종목명
                            "cur_prc": str,  # 현재가
                            "pred_pre_sig": str,  # 전일대비기호
                            "pred_pre": str,  # 전일대비
                            "flu_rt": str,  # 등락률
                            "sel_req": str,  # 매도잔량
                            "buy_req": str,  # 매수잔량
                            "now_trde_qty": str,  # 현재거래량
                            "cntr_str": str,  # 체결강도
                            "cnt": str,  # 횟수
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.rank_info.top_day_over_day_change_rate_request_ka10027(
            ...     mrkt_tp="000",
            ...     sort_tp="1",
            ...     trde_qty_cnd="0000",
            ...     stk_cnd="0",
            ...     crd_cnd="0",
            ...     updown_incls="1",
            ...     pric_cnd="0",
            ...     trde_prica_cnd="0",
            ...     stex_tp="3"
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10027",
        }

        data = {
            "mrkt_tp": mrkt_tp,
            "sort_tp": sort_tp,
            "trde_qty_cnd": trde_qty_cnd,
            "stk_cnd": stk_cnd,
            "crd_cnd": crd_cnd,
            "updown_incls": updown_incls,
            "pric_cnd": pric_cnd,
            "trde_prica_cnd": trde_prica_cnd,
            "stex_tp": stex_tp,
        }

        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
        
    def top_expected_execution_change_rate_request_ka10029(
        self,
        mrkt_tp: str,
        sort_tp: str,
        trde_qty_cnd: str,
        stk_cnd: str,
        crd_cnd: str,
        pric_cnd: str,
        stex_tp: str,
        cont_yn: str = "N",
        next_key: str = "",
    ) -> dict:
        """예상체결 등락률 상위 종목을 조회합니다.

        Args:
            mrkt_tp (str): 시장구분
                - 000: 전체
                - 001: 코스피
                - 101: 코스닥
            sort_tp (str): 정렬구분
                - 1: 상승률
                - 2: 상승폭
                - 3: 보합
                - 4: 하락률
                - 5: 하락폭
                - 6: 체결량
                - 7: 상한
                - 8: 하한
            trde_qty_cnd (str): 거래량조건
                - 0: 전체조회
                - 1: 천주이상
                - 3: 3천주
                - 5: 5천주
                - 10: 만주이상
                - 50: 5만주이상
                - 100: 10만주이상
            stk_cnd (str): 종목조건
                - 0: 전체조회
                - 1: 관리종목제외
                - 3: 우선주제외
                - 4: 관리종목,우선주제외
                - 5: 증100제외
                - 6: 증100만보기
                - 7: 증40만보기
                - 8: 증30만보기
                - 9: 증20만보기
                - 11: 정리매매종목제외
                - 12: 증50만보기
                - 13: 증60만보기
                - 14: ETF제외
                - 15: 스팩제외
                - 16: ETF+ETN제외
            crd_cnd (str): 신용조건
                - 0: 전체조회
                - 1: 신용융자A군
                - 2: 신용융자B군
                - 3: 신용융자C군
                - 4: 신용융자D군
                - 5: 신용한도초과제외
                - 8: 신용대주
                - 9: 신용융자전체
            pric_cnd (str): 가격조건
                - 0: 전체조회
                - 1: 1천원미만
                - 2: 1천원~2천원
                - 3: 2천원~5천원
                - 4: 5천원~1만원
                - 5: 1만원이상
                - 8: 1천원이상
                - 10: 1만원미만
            stex_tp (str): 거래소구분 (1:KRX, 2:NXT, 3:통합)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 예상체결 등락률 상위 종목 데이터
                {
                    "exp_cntr_flu_rt_upper": [  # 예상체결등락률상위
                        {
                            "stk_cd": str,  # 종목코드
                            "stk_nm": str,  # 종목명
                            "exp_cntr_pric": str,  # 예상체결가
                            "base_pric": str,  # 기준가
                            "pred_pre_sig": str,  # 전일대비기호
                            "pred_pre": str,  # 전일대비
                            "flu_rt": str,  # 등락률
                            "exp_cntr_qty": str,  # 예상체결량
                            "sel_req": str,  # 매도잔량
                            "sel_bid": str,  # 매도호가
                            "buy_bid": str,  # 매수호가
                            "buy_req": str,  # 매수잔량
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.rank_info.top_expected_execution_change_rate_request_ka10029(
            ...     mrkt_tp="000",
            ...     sort_tp="1",
            ...     trde_qty_cnd="0",
            ...     stk_cnd="0",
            ...     crd_cnd="0",
            ...     pric_cnd="0",
            ...     stex_tp="3"
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10029",
        }

        data = {
            "mrkt_tp": mrkt_tp,
            "sort_tp": sort_tp,
            "trde_qty_cnd": trde_qty_cnd,
            "stk_cnd": stk_cnd,
            "crd_cnd": crd_cnd,
            "pric_cnd": pric_cnd,
            "stex_tp": stex_tp,
        }

        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )

    def top_trading_volume_today_request_ka10030(
        self,
        mrkt_tp: str,
        sort_tp: str,
        mang_stk_incls: str,
        crd_tp: str,
        trde_qty_tp: str,
        pric_tp: str,
        trde_prica_tp: str,
        mrkt_open_tp: str,
        stex_tp: str,
        cont_yn: str = "N",
        next_key: str = "",
    ) -> dict:
        """당일 거래량 상위 종목을 조회합니다.

        Args:
            mrkt_tp (str): 시장구분
                - 000: 전체
                - 001: 코스피
                - 101: 코스닥
            sort_tp (str): 정렬구분
                - 1: 거래량
                - 2: 거래회전율
                - 3: 거래대금
            mang_stk_incls (str): 관리종목포함
                - 0: 관리종목 포함
                - 1: 관리종목 미포함
                - 3: 우선주제외
                - 11: 정리매매종목제외
                - 4: 관리종목, 우선주제외
                - 5: 증100제외
                - 6: 증100만보기
                - 13: 증60만보기
                - 12: 증50만보기
                - 7: 증40만보기
                - 8: 증30만보기
                - 9: 증20만보기
                - 14: ETF제외
                - 15: 스팩제외
                - 16: ETF+ETN제외
            crd_tp (str): 신용구분
                - 0: 전체조회
                - 9: 신용융자전체
                - 1: 신용융자A군
                - 2: 신용융자B군
                - 3: 신용융자C군
                - 4: 신용융자D군
                - 8: 신용대주
            trde_qty_tp (str): 거래량구분
                - 0: 전체조회
                - 5: 5천주이상
                - 10: 1만주이상
                - 50: 5만주이상
                - 100: 10만주이상
                - 200: 20만주이상
                - 300: 30만주이상
                - 500: 500만주이상
                - 1000: 백만주이상
            pric_tp (str): 가격구분
                - 0: 전체조회
                - 1: 1천원미만
                - 2: 1천원이상
                - 3: 1천원~2천원
                - 4: 2천원~5천원
                - 5: 5천원이상
                - 6: 5천원~1만원
                - 10: 1만원미만
                - 7: 1만원이상
                - 8: 5만원이상
                - 9: 10만원이상
            trde_prica_tp (str): 거래대금구분
                - 0: 전체조회
                - 1: 1천만원이상
                - 3: 3천만원이상
                - 4: 5천만원이상
                - 10: 1억원이상
                - 30: 3억원이상
                - 50: 5억원이상
                - 100: 10억원이상
                - 300: 30억원이상
                - 500: 50억원이상
                - 1000: 100억원이상
                - 3000: 300억원이상
                - 5000: 500억원이상
            mrkt_open_tp (str): 장운영구분
                - 0: 전체조회
                - 1: 장중
                - 2: 장전시간외
                - 3: 장후시간외
            stex_tp (str): 거래소구분 (1:KRX, 2:NXT, 3:통합)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 당일 거래량 상위 종목 데이터
                {
                    "tdy_trde_qty_upper": [  # 당일거래량상위
                        {
                            "stk_cd": str,  # 종목코드
                            "stk_nm": str,  # 종목명
                            "cur_prc": str,  # 현재가
                            "pred_pre_sig": str,  # 전일대비기호
                            "pred_pre": str,  # 전일대비
                            "flu_rt": str,  # 등락률
                            "trde_qty": str,  # 거래량
                            "pred_rt": str,  # 전일비
                            "trde_tern_rt": str,  # 거래회전율
                            "trde_amt": str,  # 거래금액
                            "opmr_trde_qty": str,  # 장중거래량
                            "opmr_pred_rt": str,  # 장중전일비
                            "opmr_trde_rt": str,  # 장중거래회전율
                            "opmr_trde_amt": str,  # 장중거래금액
                            "af_mkrt_trde_qty": str,  # 장후거래량
                            "af_mkrt_pred_rt": str,  # 장후전일비
                            "af_mkrt_trde_rt": str,  # 장후거래회전율
                            "af_mkrt_trde_amt": str,  # 장후거래금액
                            "bf_mkrt_trde_qty": str,  # 장전거래량
                            "bf_mkrt_pred_rt": str,  # 장전전일비
                            "bf_mkrt_trde_rt": str,  # 장전거래회전율
                            "bf_mkrt_trde_amt": str,  # 장전거래금액
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.rank_info.top_trading_volume_today_request_ka10030(
            ...     mrkt_tp="000",
            ...     sort_tp="1",
            ...     mang_stk_incls="0",
            ...     crd_tp="0",
            ...     trde_qty_tp="0",
            ...     pric_tp="0",
            ...     trde_prica_tp="0",
            ...     mrkt_open_tp="0",
            ...     stex_tp="3"
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10030",
        }

        data = {
            "mrkt_tp": mrkt_tp,
            "sort_tp": sort_tp,
            "mang_stk_incls": mang_stk_incls,
            "crd_tp": crd_tp,
            "trde_qty_tp": trde_qty_tp,
            "pric_tp": pric_tp,
            "trde_prica_tp": trde_prica_tp,
            "mrkt_open_tp": mrkt_open_tp,
            "stex_tp": stex_tp,
        }

        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
        
    def top_trading_volume_yesterday_request_ka10031(
        self,
        mrkt_tp: str,
        qry_tp: str,
        rank_strt: str,
        rank_end: str,
        stex_tp: str,
        cont_yn: str = "N",
        next_key: str = "",
    ) -> dict:
        """전일 거래량 상위 종목을 조회합니다.

        Args:
            mrkt_tp (str): 시장구분
                - 000: 전체
                - 001: 코스피
                - 101: 코스닥
            qry_tp (str): 조회구분
                - 1: 전일거래량 상위100종목
                - 2: 전일거래대금 상위100종목
            rank_strt (str): 순위시작 (0 ~ 100 값 중에 조회를 원하는 순위 시작값)
            rank_end (str): 순위끝 (0 ~ 100 값 중에 조회를 원하는 순위 끝값)
            stex_tp (str): 거래소구분 (1:KRX, 2:NXT, 3:통합)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 전일 거래량 상위 종목 데이터
                {
                    "pred_trde_qty_upper": [  # 전일거래량상위
                        {
                            "stk_cd": str,  # 종목코드
                            "stk_nm": str,  # 종목명
                            "cur_prc": str,  # 현재가
                            "pred_pre_sig": str,  # 전일대비기호
                            "pred_pre": str,  # 전일대비
                            "trde_qty": str,  # 거래량
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.rank_info.top_trading_volume_yesterday_request_ka10031(
            ...     mrkt_tp="101",
            ...     qry_tp="1",
            ...     rank_strt="0",
            ...     rank_end="10",
            ...     stex_tp="3"
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10031",
        }

        data = {
            "mrkt_tp": mrkt_tp,
            "qry_tp": qry_tp,
            "rank_strt": rank_strt,
            "rank_end": rank_end,
            "stex_tp": stex_tp,
        }

        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
        
    def top_trading_value_request_ka10032(
        self,
        mrkt_tp: str,
        mang_stk_incls: str,
        stex_tp: str,
        cont_yn: str = "N",
        next_key: str = "",
    ) -> dict:
        """거래대금 상위 종목을 조회합니다.

        Args:
            mrkt_tp (str): 시장구분
                - 000: 전체
                - 001: 코스피
                - 101: 코스닥
            mang_stk_incls (str): 관리종목포함
                - 0: 관리종목 미포함
                - 1: 관리종목 포함
            stex_tp (str): 거래소구분 (1:KRX, 2:NXT, 3:통합)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 거래대금 상위 종목 데이터
                {
                    "trde_prica_upper": [  # 거래대금상위
                        {
                            "stk_cd": str,  # 종목코드
                            "now_rank": str,  # 현재순위
                            "pred_rank": str,  # 전일순위
                            "stk_nm": str,  # 종목명
                            "cur_prc": str,  # 현재가
                            "pred_pre_sig": str,  # 전일대비기호
                            "pred_pre": str,  # 전일대비
                            "flu_rt": str,  # 등락률
                            "sel_bid": str,  # 매도호가
                            "buy_bid": str,  # 매수호가
                            "now_trde_qty": str,  # 현재거래량
                            "pred_trde_qty": str,  # 전일거래량
                            "trde_prica": str,  # 거래대금
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.rank_info.top_trading_value_request_ka10032(
            ...     mrkt_tp="001",
            ...     mang_stk_incls="1",
            ...     stex_tp="3"
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10032",
        }

        data = {
            "mrkt_tp": mrkt_tp,
            "mang_stk_incls": mang_stk_incls,
            "stex_tp": stex_tp,
        }

        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
        
    def top_credit_ratio_request_ka10033(
        self,
        mrkt_tp: str,
        trde_qty_tp: str,
        stk_cnd: str,
        updown_incls: str,
        crd_cnd: str,
        stex_tp: str,
        cont_yn: str = "N",
        next_key: str = "",
    ) -> dict:
        """신용비율 상위 종목을 조회합니다.

        Args:
            mrkt_tp (str): 시장구분
                - 000: 전체
                - 001: 코스피
                - 101: 코스닥
            trde_qty_tp (str): 거래량구분
                - 0: 전체조회
                - 10: 만주이상
                - 50: 5만주이상
                - 100: 10만주이상
                - 200: 20만주이상
                - 300: 30만주이상
                - 500: 50만주이상
                - 1000: 백만주이상
            stk_cnd (str): 종목조건
                - 0: 전체조회
                - 1: 관리종목제외
                - 5: 증100제외
                - 6: 증100만보기
                - 7: 증40만보기
                - 8: 증30만보기
                - 9: 증20만보기
            updown_incls (str): 상하한포함
                - 0: 상하한 미포함
                - 1: 상하한포함
            crd_cnd (str): 신용조건
                - 0: 전체조회
                - 1: 신용융자A군
                - 2: 신용융자B군
                - 3: 신용융자C군
                - 4: 신용융자D군
                - 9: 신용융자전체
            stex_tp (str): 거래소구분 (1:KRX, 2:NXT, 3:통합)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 신용비율 상위 종목 데이터
                {
                    "crd_rt_upper": [  # 신용비율상위
                        {
                            "stk_infr": str,  # 종목정보
                            "stk_cd": str,  # 종목코드
                            "stk_nm": str,  # 종목명
                            "cur_prc": str,  # 현재가
                            "pred_pre_sig": str,  # 전일대비기호
                            "pred_pre": str,  # 전일대비
                            "flu_rt": str,  # 등락률
                            "crd_rt": str,  # 신용비율
                            "sel_req": str,  # 매도잔량
                            "buy_req": str,  # 매수잔량
                            "now_trde_qty": str,  # 현재거래량
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.rank_info.top_credit_ratio_request_ka10033(
            ...     mrkt_tp="000",
            ...     trde_qty_tp="0",
            ...     stk_cnd="0",
            ...     updown_incls="1",
            ...     crd_cnd="0",
            ...     stex_tp="3"
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10033",
        }

        data = {
            "mrkt_tp": mrkt_tp,
            "trde_qty_tp": trde_qty_tp,
            "stk_cnd": stk_cnd,
            "updown_incls": updown_incls,
            "crd_cnd": crd_cnd,
            "stex_tp": stex_tp,
        }

        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
        
    def top_foreign_investor_trades_by_period_request_ka10034(
        self,
        mrkt_tp: str,
        trde_tp: str,
        dt: str,
        stex_tp: str,
        cont_yn: str = "N",
        next_key: str = "",
    ) -> dict:
        """외국인 기간별 매매 상위 종목을 조회합니다.

        Args:
            mrkt_tp (str): 시장구분
                - 000: 전체
                - 001: 코스피
                - 101: 코스닥
            trde_tp (str): 매매구분
                - 1: 순매도
                - 2: 순매수
                - 3: 순매매
            dt (str): 기간
                - 0: 당일
                - 1: 전일
                - 5: 5일
                - 10: 10일
                - 20: 20일
                - 60: 60일
            stex_tp (str): 거래소구분 (1:KRX, 2:NXT, 3:통합)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 외국인 기간별 매매 상위 종목 데이터
                {
                    "for_dt_trde_upper": [  # 외인기간별매매상위
                        {
                            "rank": str,  # 순위
                            "stk_cd": str,  # 종목코드
                            "stk_nm": str,  # 종목명
                            "cur_prc": str,  # 현재가
                            "pred_pre_sig": str,  # 전일대비기호
                            "pred_pre": str,  # 전일대비
                            "sel_bid": str,  # 매도호가
                            "buy_bid": str,  # 매수호가
                            "trde_qty": str,  # 거래량
                            "netprps_qty": str,  # 순매수량
                            "gain_pos_stkcnt": str,  # 취득가능주식수
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.rank_info.top_foreign_investor_trades_by_period_request_ka10034(
            ...     mrkt_tp="001",
            ...     trde_tp="2",
            ...     dt="0",
            ...     stex_tp="1"
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10034",
        }

        data = {
            "mrkt_tp": mrkt_tp,
            "trde_tp": trde_tp,
            "dt": dt,
            "stex_tp": stex_tp,
        }

        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
        
    def top_foreign_consecutive_net_buy_request_ka10035(
        self,
        mrkt_tp: str,
        trde_tp: str,
        base_dt_tp: str,
        stex_tp: str,
        cont_yn: str = "N",
        next_key: str = "",
    ) -> dict:
        """외국인 연속 순매매 상위 종목을 조회합니다.

        Args:
            mrkt_tp (str): 시장구분
                - 000: 전체
                - 001: 코스피
                - 101: 코스닥
            trde_tp (str): 매매구분
                - 1: 연속순매도
                - 2: 연속순매수
            base_dt_tp (str): 기준일구분
                - 0: 당일기준
                - 1: 전일기준
            stex_tp (str): 거래소구분 (1:KRX, 2:NXT, 3:통합)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 외국인 연속 순매매 상위 종목 데이터
                {
                    "for_cont_nettrde_upper": [  # 외인연속순매매상위
                        {
                            "stk_cd": str,  # 종목코드
                            "stk_nm": str,  # 종목명
                            "cur_prc": str,  # 현재가
                            "pred_pre_sig": str,  # 전일대비기호
                            "pred_pre": str,  # 전일대비
                            "dm1": str,  # D-1
                            "dm2": str,  # D-2
                            "dm3": str,  # D-3
                            "tot": str,  # 합계
                            "limit_exh_rt": str,  # 한도소진율
                            "pred_pre_1": str,  # 전일대비1
                            "pred_pre_2": str,  # 전일대비2
                            "pred_pre_3": str,  # 전일대비3
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.rank_info.top_foreign_consecutive_net_buy_request_ka10035(
            ...     mrkt_tp="000",
            ...     trde_tp="2",
            ...     base_dt_tp="1",
            ...     stex_tp="1"
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10035",
        }

        data = {
            "mrkt_tp": mrkt_tp,
            "trde_tp": trde_tp,
            "base_dt_tp": base_dt_tp,
            "stex_tp": stex_tp,
        }

        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
        
    def top_foreign_limit_utilization_increase_request_ka10036(
        self,
        mrkt_tp: str,
        dt: str,
        stex_tp: str,
        cont_yn: str = "N",
        next_key: str = "",
    ) -> dict:
        """외국인 한도소진율 증가 상위 종목을 조회합니다.

        Args:
            mrkt_tp (str): 시장구분
                - 000: 전체
                - 001: 코스피
                - 101: 코스닥
            dt (str): 기간
                - 0: 당일
                - 1: 전일
                - 5: 5일
                - 10: 10일
                - 20: 20일
                - 60: 60일
            stex_tp (str): 거래소구분 (1:KRX, 2:NXT, 3:통합)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 외국인 한도소진율 증가 상위 종목 데이터
                {
                    "for_limit_exh_rt_incrs_upper": [  # 외인한도소진율증가상위
                        {
                            "rank": str,  # 순위
                            "stk_cd": str,  # 종목코드
                            "stk_nm": str,  # 종목명
                            "cur_prc": str,  # 현재가
                            "pred_pre_sig": str,  # 전일대비기호
                            "pred_pre": str,  # 전일대비
                            "trde_qty": str,  # 거래량
                            "poss_stkcnt": str,  # 보유주식수
                            "gain_pos_stkcnt": str,  # 취득가능주식수
                            "base_limit_exh_rt": str,  # 기준한도소진율
                            "limit_exh_rt": str,  # 한도소진율
                            "exh_rt_incrs": str,  # 소진율증가
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.rank_info.top_foreign_limit_utilization_increase_request_ka10036(
            ...     mrkt_tp="000",
            ...     dt="1",
            ...     stex_tp="1"
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10036",
        }

        data = {
            "mrkt_tp": mrkt_tp,
            "dt": dt,
            "stex_tp": stex_tp,
        }

        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
        
    def top_foreign_broker_trading_request_ka10037(
        self,
        mrkt_tp: str,
        dt: str,
        trde_tp: str,
        sort_tp: str,
        stex_tp: str,
        cont_yn: str = "N",
        next_key: str = "",
    ) -> dict:
        """외국계 창구 매매 상위 종목을 조회합니다.

        Args:
            mrkt_tp (str): 시장구분
                - 000: 전체
                - 001: 코스피
                - 101: 코스닥
            dt (str): 기간
                - 0: 당일
                - 1: 전일
                - 5: 5일
                - 10: 10일
                - 20: 20일
                - 60: 60일
            trde_tp (str): 매매구분
                - 1: 순매수
                - 2: 순매도
            sort_tp (str): 정렬구분
                - 1: 금액
                - 2: 수량
            stex_tp (str): 거래소구분 (1:KRX, 2:NXT, 3:통합)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 외국계 창구 매매 상위 종목 데이터
                {
                    "frgn_wicket_trde_upper": [  # 외국계창구매매상위
                        {
                            "rank": str,  # 순위
                            "stk_cd": str,  # 종목코드
                            "stk_nm": str,  # 종목명
                            "cur_prc": str,  # 현재가
                            "pred_pre_sig": str,  # 전일대비기호
                            "pred_pre": str,  # 전일대비
                            "flu_rt": str,  # 등락율
                            "sel_trde_qty": str,  # 매도거래량
                            "buy_trde_qty": str,  # 매수거래량
                            "netprps_trde_qty": str,  # 순매수거래량
                            "netprps_prica": str,  # 순매수대금
                            "trde_qty": str,  # 거래량
                            "trde_prica": str,  # 거래대금
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.rank_info.top_foreign_broker_trading_request_ka10037(
            ...     mrkt_tp="000",
            ...     dt="0",
            ...     trde_tp="1",
            ...     sort_tp="2",
            ...     stex_tp="1"
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10037",
        }

        data = {
            "mrkt_tp": mrkt_tp,
            "dt": dt,
            "trde_tp": trde_tp,
            "sort_tp": sort_tp,
            "stex_tp": stex_tp,
        }

        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
        
    def broker_ranking_by_stock_request_ka10038(
        self,
        stk_cd: str,
        strt_dt: str,
        end_dt: str,
        qry_tp: str,
        dt: str,
        cont_yn: str = "N",
        next_key: str = "",
    ) -> dict:
        """종목별 증권사 순위를 조회합니다.

        Args:
            stk_cd (str): 종목코드 (거래소별 종목코드)
                - KRX: 039490
                - NXT: 039490_NX
                - SOR: 039490_AL
            strt_dt (str): 시작일자 (YYYYMMDD 형식)
            end_dt (str): 종료일자 (YYYYMMDD 형식)
            qry_tp (str): 조회구분
                - 1: 순매도순위정렬
                - 2: 순매수순위정렬
            dt (str): 기간
                - 1: 전일
                - 4: 5일
                - 9: 10일
                - 19: 20일
                - 39: 40일
                - 59: 60일
                - 119: 120일
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 종목별 증권사 순위 데이터
                {
                    "rank_1": str,  # 순위1
                    "rank_2": str,  # 순위2
                    "rank_3": str,  # 순위3
                    "prid_trde_qty": str,  # 기간중거래량
                    "stk_sec_rank": [  # 종목별증권사순위
                        {
                            "rank": str,  # 순위
                            "mmcm_nm": str,  # 회원사명
                            "buy_qty": str,  # 매수수량
                            "sell_qty": str,  # 매도수량
                            "acc_netprps_qty": str,  # 누적순매수수량
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.rank_info.broker_ranking_by_stock_request_ka10038(
            ...     stk_cd="005930",
            ...     strt_dt="20241106",
            ...     end_dt="20241107",
            ...     qry_tp="2",
            ...     dt="1"
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10038",
        }

        data = {
            "stk_cd": stk_cd,
            "strt_dt": strt_dt,
            "end_dt": end_dt,
            "qry_tp": qry_tp,
            "dt": dt,
        }

        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
        
    def top_broker_trading_request_ka10039(
        self,
        mmcm_cd: str,
        trde_qty_tp: str,
        trde_tp: str,
        dt: str,
        stex_tp: str,
        cont_yn: str = "N",
        next_key: str = "",
    ) -> dict:
        """증권사별 매매 상위 종목을 조회합니다.

        Args:
            mmcm_cd (str): 회원사코드 (ka10102 API로 조회 가능)
            trde_qty_tp (str): 거래량구분
                - 0: 전체
                - 5: 5000주
                - 10: 1만주
                - 50: 5만주
                - 100: 10만주
                - 500: 50만주
                - 1000: 100만주
            trde_tp (str): 매매구분
                - 1: 순매수
                - 2: 순매도
            dt (str): 기간
                - 1: 전일
                - 5: 5일
                - 10: 10일
                - 60: 60일
            stex_tp (str): 거래소구분
                - 1: KRX
                - 2: NXT
                - 3: 통합
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 증권사별 매매 상위 종목 데이터
                {
                    "sec_trde_upper": [  # 증권사별매매상위
                        {
                            "rank": str,  # 순위
                            "stk_cd": str,  # 종목코드
                            "stk_nm": str,  # 종목명
                            "prid_stkpc_flu": str,  # 기간중주가등락
                            "flu_rt": str,  # 등락율
                            "prid_trde_qty": str,  # 기간중거래량
                            "netprps": str,  # 순매수
                            "buy_trde_qty": str,  # 매수거래량
                            "sel_trde_qty": str,  # 매도거래량
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.rank_info.top_broker_trading_request_ka10039(
            ...     mmcm_cd="001",
            ...     trde_qty_tp="0",
            ...     trde_tp="1",
            ...     dt="1",
            ...     stex_tp="3"
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10039",
        }

        data = {
            "mmcm_cd": mmcm_cd,
            "trde_qty_tp": trde_qty_tp,
            "trde_tp": trde_tp,
            "dt": dt,
            "stex_tp": stex_tp,
        }

        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
        
    def main_trading_brokers_today_request_ka10040(
        self,
        stk_cd: str,
        cont_yn: str = "N",
        next_key: str = "",
    ) -> dict:
        """당일 주요 거래원 정보를 조회합니다.

        Args:
            stk_cd (str): 종목코드
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 당일 주요 거래원 데이터
                {
                    # 매도 거래원 정보 (1~5위)
                    "sel_trde_ori_irds_1": str,  # 매도거래원별증감1
                    "sel_trde_ori_qty_1": str,  # 매도거래원수량1
                    "sel_trde_ori_1": str,  # 매도거래원1
                    "sel_trde_ori_cd_1": str,  # 매도거래원코드1
                    # ... (2~5위 동일한 패턴)
                    
                    # 매수 거래원 정보 (1~5위)
                    "buy_trde_ori_1": str,  # 매수거래원1
                    "buy_trde_ori_cd_1": str,  # 매수거래원코드1
                    "buy_trde_ori_qty_1": str,  # 매수거래원수량1
                    "buy_trde_ori_irds_1": str,  # 매수거래원별증감1
                    # ... (2~5위 동일한 패턴)
                    
                    # 외국계 거래 정보
                    "frgn_sel_prsm_sum_chang": str,  # 외국계매도추정합변동
                    "frgn_sel_prsm_sum": str,  # 외국계매도추정합
                    "frgn_buy_prsm_sum": str,  # 외국계매수추정합
                    "frgn_buy_prsm_sum_chang": str,  # 외국계매수추정합변동
                    
                    # 당일 주요 거래원 상세 정보
                    "tdy_main_trde_ori": [  # 당일주요거래원
                        {
                            "sel_scesn_tm": str,  # 매도이탈시간
                            "sell_qty": str,  # 매도수량
                            "sel_upper_scesn_ori": str,  # 매도상위이탈원
                            "buy_scesn_tm": str,  # 매수이탈시간
                            "buy_qty": str,  # 매수수량
                            "buy_upper_scesn_ori": str,  # 매수상위이탈원
                            "qry_dt": str,  # 조회일자
                            "qry_tm": str,  # 조회시간
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.rank_info.main_trading_brokers_today_request_ka10040(
            ...     stk_cd="005930"  # 삼성전자
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10040",
        }

        data = {
            "stk_cd": stk_cd,
        }

        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
        
    def top_net_buying_brokers_request_ka10042(
        self,
        stk_cd: str,
        qry_dt_tp: str,
        pot_tp: str,
        sort_base: str,
        strt_dt: str = "",
        end_dt: str = "",
        dt: str = "",
        cont_yn: str = "N",
        next_key: str = "",
    ) -> dict:
        """순매수거래원순위를 조회합니다.

        Args:
            stk_cd (str): 종목코드 (거래소별 종목코드)
                - KRX: 039490
                - NXT: 039490_NX
                - SOR: 039490_AL
            qry_dt_tp (str): 조회기간구분
                - 0: 기간으로 조회
                - 1: 시작일자, 종료일자로 조회
            pot_tp (str): 시점구분
                - 0: 당일
                - 1: 전일
            sort_base (str): 정렬기준
                - 1: 종가순
                - 2: 날짜순
            strt_dt (str, optional): 시작일자 (YYYYMMDD 형식). Defaults to "".
            end_dt (str, optional): 종료일자 (YYYYMMDD 형식). Defaults to "".
            dt (str, optional): 기간
                - 5: 5일
                - 10: 10일
                - 20: 20일
                - 40: 40일
                - 60: 60일
                - 120: 120일
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 순매수거래원순위 데이터
                {
                    "netprps_trde_ori_rank": [  # 순매수거래원순위
                        {
                            "rank": str,  # 순위
                            "mmcm_cd": str,  # 회원사코드
                            "mmcm_nm": str,  # 회원사명
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.rank_info.top_net_buying_brokers_request_ka10042(
            ...     stk_cd="005930",
            ...     qry_dt_tp="0",
            ...     pot_tp="0",
            ...     sort_base="1",
            ...     dt="5"
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10042",
        }

        data = {
            "stk_cd": stk_cd,
            "qry_dt_tp": qry_dt_tp,
            "pot_tp": pot_tp,
            "sort_base": sort_base,
        }

        # Optional parameters
        if strt_dt:
            data["strt_dt"] = strt_dt
        if end_dt:
            data["end_dt"] = end_dt
        if dt:
            data["dt"] = dt

        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
        
    def top_departed_trading_brokers_today_request_ka10053(
        self,
        stk_cd: str,
        cont_yn: str = "N",
        next_key: str = "",
    ) -> dict:
        """당일 상위 이탈원 정보를 조회합니다.

        Args:
            stk_cd (str): 종목코드 (거래소별 종목코드)
                - KRX: 039490
                - NXT: 039490_NX
                - SOR: 039490_AL
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 당일 상위 이탈원 데이터
                {
                    "tdy_upper_scesn_ori": [  # 당일상위이탈원
                        {
                            "sel_scesn_tm": str,  # 매도이탈시간
                            "sell_qty": str,  # 매도수량
                            "sel_upper_scesn_ori": str,  # 매도상위이탈원
                            "buy_scesn_tm": str,  # 매수이탈시간
                            "buy_qty": str,  # 매수수량
                            "buy_upper_scesn_ori": str,  # 매수상위이탈원
                            "qry_dt": str,  # 조회일자
                            "qry_tm": str,  # 조회시간
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.rank_info.top_departed_trading_brokers_today_request_ka10053(
            ...     stk_cd="005930"  # 삼성전자
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10053",
        }

        data = {
            "stk_cd": stk_cd,
        }

        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )

    def same_day_net_buying_ranking_request_ka10062(
        self,
        strt_dt: str,
        mrkt_tp: str,
        trde_tp: str,
        sort_cnd: str,
        unit_tp: str,
        stex_tp: str,
        end_dt: str = "",
        cont_yn: str = "N",
        next_key: str = "",
    ) -> dict:
        """동일순매매순위를 조회합니다.

        Args:
            strt_dt (str): 시작일자 (YYYYMMDD 형식)
            mrkt_tp (str): 시장구분
                - 000: 전체
                - 001: 코스피
                - 101: 코스닥
            trde_tp (str): 매매구분
                - 1: 순매수
                - 2: 순매도
            sort_cnd (str): 정렬조건
                - 1: 수량
                - 2: 금액
        unit_tp (str): 단위구분
            - 1: 단주
            - 1000: 천주
        stex_tp (str): 거래소구분
            - 1: KRX
            - 2: NXT
            - 3: 통합
        end_dt (str, optional): 종료일자 (YYYYMMDD 형식). Defaults to "".
        cont_yn (str, optional): 연속조회여부. Defaults to "N".
        next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 동일순매매순위 데이터
                {
                    "eql_nettrde_rank": [  # 동일순매매순위
                        {
                            "stk_cd": str,  # 종목코드
                            "rank": str,  # 순위
                            "stk_nm": str,  # 종목명
                            "cur_prc": str,  # 현재가
                            "pre_sig": str,  # 대비기호
                            "pred_pre": str,  # 전일대비
                            "flu_rt": str,  # 등락율
                            "acc_trde_qty": str,  # 누적거래량
                            "orgn_nettrde_qty": str,  # 기관순매매수량
                            "orgn_nettrde_amt": str,  # 기관순매매금액
                            "orgn_nettrde_avg_pric": str,  # 기관순매매평균가
                            "for_nettrde_qty": str,  # 외인순매매수량
                            "for_nettrde_amt": str,  # 외인순매매금액
                            "for_nettrde_avg_pric": str,  # 외인순매매평균가
                            "nettrde_qty": str,  # 순매매수량
                            "nettrde_amt": str,  # 순매매금액
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.rank_info.same_day_net_buying_ranking_request_ka10062(
            ...     strt_dt="20241106",
            ...     mrkt_tp="000",
            ...     trde_tp="1",
            ...     sort_cnd="1",
            ...     unit_tp="1",
            ...     stex_tp="3",
            ...     end_dt="20241107"
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10062",
        }

        data = {
            "strt_dt": strt_dt,
            "mrkt_tp": mrkt_tp,
            "trde_tp": trde_tp,
            "sort_cnd": sort_cnd,
            "unit_tp": unit_tp,
            "stex_tp": stex_tp,
        }

        # Optional parameter
        if end_dt:
            data["end_dt"] = end_dt

        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
        
    def top_intraday_investor_trading_request_ka10065(
        self,
        trde_tp: str,
        mrkt_tp: str,
        orgn_tp: str,
        cont_yn: str = "N",
        next_key: str = "",
    ) -> dict:
        """장중 투자자별 매매 상위 종목을 조회합니다.

        Args:
            trde_tp (str): 매매구분
                - 1: 순매수
                - 2: 순매도
            mrkt_tp (str): 시장구분
                - 000: 전체
                - 001: 코스피
                - 101: 코스닥
            orgn_tp (str): 기관구분
                - 9000: 외국인
                - 9100: 외국계
                - 1000: 금융투자
                - 3000: 투신
                - 5000: 기타금융
                - 4000: 은행
                - 2000: 보험
                - 6000: 연기금
                - 7000: 국가
                - 7100: 기타법인
                - 9999: 기관계
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 장중 투자자별 매매 상위 종목 데이터
                {
                    "opmr_invsr_trde_upper": [  # 장중투자자별매매상위
                        {
                            "stk_cd": str,  # 종목코드
                            "stk_nm": str,  # 종목명
                            "sel_qty": str,  # 매도량
                            "buy_qty": str,  # 매수량
                            "netslmt": str,  # 순매도
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.rank_info.top_intraday_investor_trading_request_ka10065(
            ...     trde_tp="1",  # 순매수
            ...     mrkt_tp="000",  # 전체
            ...     orgn_tp="9000"  # 외국인
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10065",
        }

        data = {
            "trde_tp": trde_tp,
            "mrkt_tp": mrkt_tp,
            "orgn_tp": orgn_tp,
        }

        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
        
    def after_market_price_change_rate_ranking_request_ka10098(
        self,
        mrkt_tp: str,
        sort_base: str,
        stk_cnd: str,
        trde_qty_cnd: str,
        crd_cnd: str,
        trde_prica: str,
        cont_yn: str = "N",
        next_key: str = "",
    ) -> dict:
        """시간외 단일가 등락율 순위를 조회합니다.

        Args:
            mrkt_tp (str): 시장구분
                - 000: 전체
                - 001: 코스피
                - 101: 코스닥
            sort_base (str): 정렬기준
                - 1: 상승률
                - 2: 상승폭
                - 3: 하락률
                - 4: 하락폭
                - 5: 보합
            stk_cnd (str): 종목조건
                - 0: 전체조회
                - 1: 관리종목제외
                - 2: 정리매매종목제외
                - 3: 우선주제외
                - 4: 관리종목우선주제외
                - 5: 증100제외
                - 6: 증100만보기
                - 7: 증40만보기
                - 8: 증30만보기
                - 9: 증20만보기
                - 12: 증50만보기
                - 13: 증60만보기
                - 14: ETF제외
                - 15: 스팩제외
                - 16: ETF+ETN제외
                - 17: ETN제외
            trde_qty_cnd (str): 거래량조건
                - 0: 전체조회
                - 10: 백주이상
                - 50: 5백주이상
                - 100: 천주이상
                - 500: 5천주이상
                - 1000: 만주이상
                - 5000: 5만주이상
                - 10000: 10만주이상
            crd_cnd (str): 신용조건
                - 0: 전체조회
                - 9: 신용융자전체
                - 1: 신용융자A군
                - 2: 신용융자B군
                - 3: 신용융자C군
                - 4: 신용융자D군
                - 8: 신용대주
                - 5: 신용한도초과제외
            trde_prica (str): 거래대금
                - 0: 전체조회
                - 5: 5백만원이상
                - 10: 1천만원이상
                - 30: 3천만원이상
                - 50: 5천만원이상
                - 100: 1억원이상
                - 300: 3억원이상
                - 500: 5억원이상
                - 1000: 10억원이상
                - 3000: 30억원이상
                - 5000: 50억원이상
                - 10000: 100억원이상
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 시간외 단일가 등락율 순위 데이터
                {
                    "ovt_sigpric_flu_rt_rank": [  # 시간외단일가등락율순위
                        {
                            "rank": str,  # 순위
                            "stk_cd": str,  # 종목코드
                            "stk_nm": str,  # 종목명
                            "cur_prc": str,  # 현재가
                            "pred_pre_sig": str,  # 전일대비기호
                            "pred_pre": str,  # 전일대비
                            "flu_rt": str,  # 등락률
                            "sel_tot_req": str,  # 매도총잔량
                            "buy_tot_req": str,  # 매수총잔량
                            "acc_trde_qty": str,  # 누적거래량
                            "acc_trde_prica": str,  # 누적거래대금
                            "tdy_close_pric": str,  # 당일종가
                            "tdy_close_pric_flu_rt": str,  # 당일종가등락률
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.rank_info.after_market_price_change_rate_ranking_request_ka10098(
            ...     mrkt_tp="000",  # 전체
            ...     sort_base="5",  # 보합
            ...     stk_cnd="0",  # 전체조회
            ...     trde_qty_cnd="0",  # 전체조회
            ...     crd_cnd="0",  # 전체조회
            ...     trde_prica="0"  # 전체조회
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10098",
        }

        data = {
            "mrkt_tp": mrkt_tp,
            "sort_base": sort_base,
            "stk_cnd": stk_cnd,
            "trde_qty_cnd": trde_qty_cnd,
            "crd_cnd": crd_cnd,
            "trde_prica": trde_prica,
        }

        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )

    def top_foreign_institution_trades_request_ka90009(
        self,
        mrkt_tp: str,
        amt_qty_tp: str,
        qry_dt_tp: str,
        stex_tp: str,
        date: str = "",
        cont_yn: str = "N",
        next_key: str = "",
    ) -> dict:
        """외국인/기관 매매 상위 종목을 조회합니다.

        Args:
            mrkt_tp (str): 시장구분
                - 000: 전체
                - 001: 코스피
                - 101: 코스닥
            amt_qty_tp (str): 금액수량구분
                - 1: 금액(천만)
                - 2: 수량(천)
            qry_dt_tp (str): 조회일자구분
                - 0: 조회일자 미포함
                - 1: 조회일자 포함
            stex_tp (str): 거래소구분
                - 1: KRX
                - 2: NXT
                - 3: 통합
            date (str, optional): 날짜 (YYYYMMDD 형식). Defaults to "".
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 외국인/기관 매매 상위 종목 데이터
                {
                    "frgnr_orgn_trde_upper": [  # 외국인기관매매상위
                        {
                            "for_netslmt_stk_cd": str,  # 외인순매도종목코드
                            "for_netslmt_stk_nm": str,  # 외인순매도종목명
                            "for_netslmt_amt": str,  # 외인순매도금액
                            "for_netslmt_qty": str,  # 외인순매도수량
                            "for_netprps_stk_cd": str,  # 외인순매수종목코드
                            "for_netprps_stk_nm": str,  # 외인순매수종목명
                            "for_netprps_amt": str,  # 외인순매수금액
                            "for_netprps_qty": str,  # 외인순매수수량
                            "orgn_netslmt_stk_cd": str,  # 기관순매도종목코드
                            "orgn_netslmt_stk_nm": str,  # 기관순매도종목명
                            "orgn_netslmt_amt": str,  # 기관순매도금액
                            "orgn_netslmt_qty": str,  # 기관순매도수량
                            "orgn_netprps_stk_cd": str,  # 기관순매수종목코드
                            "orgn_netprps_stk_nm": str,  # 기관순매수종목명
                            "orgn_netprps_amt": str,  # 기관순매수금액
                            "orgn_netprps_qty": str,  # 기관순매수수량
                        },
                        ...
                    ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.rank_info.top_foreign_institution_trades_request_ka90009(
            ...     mrkt_tp="000",  # 전체
            ...     amt_qty_tp="1",  # 금액(천만)
            ...     qry_dt_tp="1",  # 조회일자 포함
            ...     stex_tp="1",  # KRX
            ...     date="20241101"
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka90009",
        }

        data = {
            "mrkt_tp": mrkt_tp,
            "amt_qty_tp": amt_qty_tp,
            "qry_dt_tp": qry_dt_tp,
            "stex_tp": stex_tp,
        }

        # Optional parameter
        if date:
            data["date"] = date

        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )