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