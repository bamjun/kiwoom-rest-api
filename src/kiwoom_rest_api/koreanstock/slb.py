from kiwoom_rest_api.core.base_api import KiwoomBaseAPI
from typing import Union, Dict, Any, Awaitable

class SecuritiesLendingAndBorrowing(KiwoomBaseAPI):
    """한국 주식 대차거래 관련 API를 제공하는 클래스"""
    
    def __init__(
        self, 
        base_url: str = None, 
        token_manager=None, 
        use_async: bool = False,
        resource_url: str = "/api/dostk/slb"
    ):
        """
        SecuritiesLendingAndBorrowing 클래스 초기화
        
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
             
    def stock_lending_trend_request_ka10068(
        self,
        strt_dt: str = "",
        end_dt: str = "",
        all_tp: str = "1",
        cont_yn: str = "N",
        next_key: str = "",
    ) -> dict:
        """대차거래추이를 요청합니다.

        Args:
            strt_dt (str, optional): 시작일자 (YYYYMMDD). Defaults to "".
            end_dt (str, optional): 종료일자 (YYYYMMDD). Defaults to "".
            all_tp (str, optional): 전체구분 (1: 전체표시). Defaults to "1".
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 대차거래추이 데이터
                {
                    "dbrt_trde_trnsn": list,  # 대차거래추이 리스트
                        [
                            {
                                "dt": str,  # 일자
                                "dbrt_trde_cntrcnt": str,  # 대차거래체결주수
                                "dbrt_trde_rpy": str,  # 대차거래상환주수
                                "dbrt_trde_irds": str,  # 대차거래증감
                                "rmnd": str,  # 잔고주수
                                "remn_amt": str,  # 잔고금액
                            }
                        ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.slb.stock_lending_trend_request_ka10068(
            ...     strt_dt="20250401",
            ...     end_dt="20250430",
            ...     all_tp="1"
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10068",
        }

        data = {
            "strt_dt": strt_dt,
            "end_dt": end_dt,
            "all_tp": all_tp,
        }

        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
        
    def top10_stock_lending_request_ka10069(
        self,
        strt_dt: str,
        end_dt: str = "",
        mrkt_tp: str = "001",
        cont_yn: str = "N",
        next_key: str = "",
    ) -> dict:
        """대차거래상위10종목을 요청합니다.

        Args:
            strt_dt (str): 시작일자 (YYYYMMDD 형식)
            end_dt (str, optional): 종료일자 (YYYYMMDD 형식). Defaults to "".
            mrkt_tp (str, optional): 시장구분 (001:코스피, 101:코스닥). Defaults to "001".
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 대차거래상위10종목 데이터
                {
                    "dbrt_trde_cntrcnt_sum": str,  # 대차거래체결주수합
                    "dbrt_trde_rpy_sum": str,  # 대차거래상환주수합
                    "rmnd_sum": str,  # 잔고주수합
                    "remn_amt_sum": str,  # 잔고금액합
                    "dbrt_trde_cntrcnt_rt": str,  # 대차거래체결주수비율
                    "dbrt_trde_rpy_rt": str,  # 대차거래상환주수비율
                    "rmnd_rt": str,  # 잔고주수비율
                    "remn_amt_rt": str,  # 잔고금액비율
                    "dbrt_trde_upper_10stk": list,  # 대차거래상위10종목 리스트
                        [
                            {
                                "stk_nm": str,  # 종목명
                                "stk_cd": str,  # 종목코드
                                "dbrt_trde_cntrcnt": str,  # 대차거래체결주수
                                "dbrt_trde_rpy": str,  # 대차거래상환주수
                                "rmnd": str,  # 잔고주수
                                "remn_amt": str,  # 잔고금액
                            }
                        ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.slb.top10_stock_lending_request_ka10069(
            ...     strt_dt="20241110",
            ...     end_dt="20241125",
            ...     mrkt_tp="001"
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka10069",
        }

        data = {
            "strt_dt": strt_dt,
            "end_dt": end_dt,
            "mrkt_tp": mrkt_tp,
        }

        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
        
    def stockwise_lending_trend_request_ka20068(
        self,
        stk_cd: str,
        strt_dt: str = "",
        end_dt: str = "",
        all_tp: str = "0",
        cont_yn: str = "N",
        next_key: str = "",
    ) -> dict:
        """종목별 대차거래추이를 요청합니다.

        Args:
            stk_cd (str): 종목코드
            strt_dt (str, optional): 시작일자 (YYYYMMDD). Defaults to "".
            end_dt (str, optional): 종료일자 (YYYYMMDD). Defaults to "".
            all_tp (str, optional): 전체구분 (0:종목코드 입력종목만 표시). Defaults to "0".
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 종목별 대차거래추이 데이터
                {
                    "dbrt_trde_trnsn": list,  # 대차거래추이 리스트
                        [
                            {
                                "dt": str,  # 일자
                                "dbrt_trde_cntrcnt": str,  # 대차거래체결주수
                                "dbrt_trde_rpy": str,  # 대차거래상환주수
                                "dbrt_trde_irds": str,  # 대차거래증감
                                "rmnd": str,  # 잔고주수
                                "remn_amt": str,  # 잔고금액
                            }
                        ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.slb.stockwise_lending_trend_request_ka20068(
            ...     stk_cd="005930",
            ...     strt_dt="20250401",
            ...     end_dt="20250430",
            ...     all_tp="0"
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka20068",
        }

        data = {
            "stk_cd": stk_cd,
            "strt_dt": strt_dt,
            "end_dt": end_dt,
            "all_tp": all_tp,
        }

        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )
        
    def stock_lending_details_request_ka90012(
        self,
        dt: str,
        mrkt_tp: str,
        cont_yn: str = "N",
        next_key: str = "",
    ) -> dict:
        """대차거래내역을 요청합니다.

        Args:
            dt (str): 일자 (YYYYMMDD 형식)
            mrkt_tp (str): 시장구분 (001:코스피, 101:코스닥)
            cont_yn (str, optional): 연속조회여부. Defaults to "N".
            next_key (str, optional): 연속조회키. Defaults to "".

        Returns:
            dict: 대차거래내역 데이터
                {
                    "dbrt_trde_prps": list,  # 대차거래내역 리스트
                        [
                            {
                                "stk_nm": str,  # 종목명
                                "stk_cd": str,  # 종목코드
                                "dbrt_trde_cntrcnt": str,  # 대차거래체결주수
                                "dbrt_trde_rpy": str,  # 대차거래상환주수
                                "rmnd": str,  # 잔고주수
                                "remn_amt": str,  # 잔고금액
                            }
                        ],
                    "return_code": int,  # 응답코드
                    "return_msg": str,  # 응답메시지
                }

        Example:
            >>> from kiwoom_rest_api import KiwoomRestAPI
            >>> api = KiwoomRestAPI()
            >>> result = api.slb.stock_lending_details_request_ka90012(
            ...     dt="20241101",
            ...     mrkt_tp="101"
            ... )
            >>> print(result)
        """
        headers = {
            "cont-yn": cont_yn,
            "next-key": next_key,
            "api-id": "ka90012",
        }

        data = {
            "dt": dt,
            "mrkt_tp": mrkt_tp,
        }

        return self._execute_request(
            "POST",
            json=data,
            headers=headers,
        )