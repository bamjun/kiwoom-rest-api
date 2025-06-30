import asyncio
import logging
from typing import Any, Callable, Dict, List, Optional, Union
from datetime import datetime

from .websocket import WebSocketClient, RealTimeData, WebSocketError
from .websocket_constants import get_field_name, get_type_name, REALTIME_TYPES

logger = logging.getLogger(__name__)

class RealTimeDataProcessor:
    """실시간 데이터 처리기"""
    
    def __init__(self):
        self.data_handlers: Dict[str, Callable] = {}
        self.balance_data: Dict[str, Dict] = {}  # 계좌별 잔고 데이터
        self.stock_data: Dict[str, Dict] = {}    # 종목별 시세 데이터
        
    def register_handler(self, type_code: str, handler: Callable):
        """특정 타입의 데이터 핸들러 등록"""
        self.data_handlers[type_code] = handler
        
    def process_data(self, realtime_data: RealTimeData) -> Dict[str, Any]:
        """실시간 데이터 처리"""
        if realtime_data.trnm != 'REAL':
            return {}
            
        processed_data = {}
        
        for item_data in realtime_data.data:
            type_code = item_data.get('type', '')
            item_code = item_data.get('item', '')
            values = item_data.get('values', {})
            
            # 데이터 타입별 처리
            if type_code == '04':  # 잔고
                processed = self._process_balance_data(item_code, values)
                self.balance_data[item_code] = processed
                processed_data[item_code] = processed
                
            elif type_code in ['0A', '0B', '0C']:  # 주식 관련
                processed = self._process_stock_data(type_code, item_code, values)
                self.stock_data[item_code] = processed
                processed_data[item_code] = processed
                
            # 등록된 핸들러 호출
            if type_code in self.data_handlers:
                try:
                    self.data_handlers[type_code](processed_data)
                except Exception as e:
                    logger.error(f"데이터 핸들러 오류 ({type_code}): {e}")
                    
        return processed_data
    
    def _process_balance_data(self, item_code: str, values: Dict) -> Dict[str, Any]:
        """잔고 데이터 처리"""
        processed = {
            '종목코드': item_code,
            '처리시간': datetime.now().isoformat(),
            '데이터타입': '잔고'
        }
        
        # 필드 매핑 적용
        for field_code, value in values.items():
            field_name = get_field_name('04', field_code)
            processed[field_name] = value
            
        return processed
    
    def _process_stock_data(self, type_code: str, item_code: str, values: Dict) -> Dict[str, Any]:
        """주식 데이터 처리"""
        processed = {
            '종목코드': item_code,
            '처리시간': datetime.now().isoformat(),
            '데이터타입': get_type_name(type_code)
        }
        
        # 필드 매핑 적용
        for field_code, value in values.items():
            field_name = get_field_name(type_code, field_code)
            processed[field_name] = value
            
        return processed
    
    def get_balance_data(self, item_code: str = None) -> Dict:
        """잔고 데이터 조회"""
        if item_code:
            return self.balance_data.get(item_code, {})
        return self.balance_data
    
    def get_stock_data(self, item_code: str = None) -> Dict:
        """주식 데이터 조회"""
        if item_code:
            return self.stock_data.get(item_code, {})
        return self.stock_data

class SimpleWebSocketClient:
    """간단한 웹소켓 클라이언트 (사용하기 쉬운 인터페이스)"""
    
    def __init__(
        self,
        access_token: str,
        ws_url: Optional[str] = None,
        auto_reconnect: bool = True
    ):
        self.client = WebSocketClient(
            access_token=access_token,
            ws_url=ws_url,
            auto_reconnect=auto_reconnect
        )
        self.processor = RealTimeDataProcessor()
        self._setup_default_handlers()
        
    def _setup_default_handlers(self):
        """기본 핸들러 설정"""
        self.client.on_data = self._on_data_received
        self.client.on_connect = self._on_connected
        self.client.on_login = self._on_logged_in
        self.client.on_error = self._on_error
        
    async def _on_data_received(self, realtime_data: RealTimeData):
        """데이터 수신 시 호출"""
        processed_data = self.processor.process_data(realtime_data)
        if processed_data:
            logger.info(f"실시간 데이터 처리 완료: {len(processed_data)}개 항목")
            
    async def _on_connected(self):
        """연결 성공 시 호출"""
        logger.info("웹소켓 서버에 연결되었습니다")
        
    async def _on_logged_in(self):
        """로그인 성공 시 호출"""
        logger.info("웹소켓 서버 로그인 성공")
        
    async def _on_error(self, error: Exception):
        """오류 발생 시 호출"""
        logger.error(f"웹소켓 오류: {error}")
        
    def register_data_handler(self, type_code: str, handler: Callable):
        """데이터 핸들러 등록"""
        self.processor.register_handler(type_code, handler)
        
    async def start(self, type_list: List[str] = None, item_list: List[str] = None):
        """웹소켓 클라이언트 시작"""
        if type_list is None:
            type_list = ['04']  # 기본값: 잔고
            
        await self.client.start()
        await self.client.register_realtime(type_list=type_list, item_list=item_list)
        
    async def stop(self):
        """웹소켓 클라이언트 중지"""
        await self.client.stop()
        
    def run_sync(self, type_list: List[str] = None, item_list: List[str] = None):
        """동기적으로 실행"""
        async def run():
            await self.start(type_list, item_list)
            await self.client.run_forever()
            
        try:
            asyncio.run(run())
        except KeyboardInterrupt:
            logger.info("사용자에 의해 중단되었습니다")
            asyncio.run(self.stop())
            
    def get_balance_data(self, item_code: str = None) -> Dict:
        """잔고 데이터 조회"""
        return self.processor.get_balance_data(item_code)
        
    def get_stock_data(self, item_code: str = None) -> Dict:
        """주식 데이터 조회"""
        return self.processor.get_stock_data(item_code)

class WebSocketManager:
    """웹소켓 클라이언트 관리자 (여러 클라이언트 관리)"""
    
    def __init__(self):
        self.clients: Dict[str, WebSocketClient] = {}
        self.tasks: Dict[str, asyncio.Task] = {}
        
    async def add_client(
        self,
        client_id: str,
        access_token: str,
        ws_url: Optional[str] = None,
        type_list: List[str] = None,
        item_list: List[str] = None
    ) -> WebSocketClient:
        """클라이언트 추가"""
        if client_id in self.clients:
            raise ValueError(f"클라이언트 ID '{client_id}'가 이미 존재합니다")
            
        client = WebSocketClient(access_token=access_token, ws_url=ws_url)
        self.clients[client_id] = client
        
        # 클라이언트 시작
        await client.start()
        if type_list:
            await client.register_realtime(type_list=type_list, item_list=item_list)
            
        # 태스크 생성
        task = asyncio.create_task(client.run_forever())
        self.tasks[client_id] = task
        
        return client
        
    async def remove_client(self, client_id: str):
        """클라이언트 제거"""
        if client_id not in self.clients:
            return
            
        # 태스크 취소
        if client_id in self.tasks:
            self.tasks[client_id].cancel()
            del self.tasks[client_id]
            
        # 클라이언트 중지
        await self.clients[client_id].stop()
        del self.clients[client_id]
        
    async def stop_all(self):
        """모든 클라이언트 중지"""
        for client_id in list(self.clients.keys()):
            await self.remove_client(client_id)
            
    def get_client(self, client_id: str) -> Optional[WebSocketClient]:
        """클라이언트 조회"""
        return self.clients.get(client_id)
        
    def list_clients(self) -> List[str]:
        """클라이언트 목록 조회"""
        return list(self.clients.keys())

# 유틸리티 함수들
def create_simple_client(
    access_token: str,
    ws_url: Optional[str] = None,
    type_list: List[str] = None,
    item_list: List[str] = None
) -> SimpleWebSocketClient:
    """간단한 웹소켓 클라이언트 생성"""
    client = SimpleWebSocketClient(access_token=access_token, ws_url=ws_url)
    
    if type_list:
        for type_code in type_list:
            if type_code not in REALTIME_TYPES:
                logger.warning(f"알 수 없는 실시간 타입: {type_code}")
                
    return client

def format_balance_data(balance_data: Dict) -> str:
    """잔고 데이터를 보기 좋게 포맷팅"""
    if not balance_data:
        return "잔고 데이터가 없습니다"
        
    lines = []
    for item_code, data in balance_data.items():
        lines.append(f"종목: {data.get('종목명', item_code)}")
        lines.append(f"  현재가: {data.get('현재가', 'N/A')}")
        lines.append(f"  보유수량: {data.get('보유수량', 'N/A')}")
        lines.append(f"  매입단가: {data.get('매입단가', 'N/A')}")
        lines.append(f"  손익률: {data.get('손익률', 'N/A')}%")
        lines.append("")
        
    return "\n".join(lines)

def format_stock_data(stock_data: Dict) -> str:
    """주식 데이터를 보기 좋게 포맷팅"""
    if not stock_data:
        return "주식 데이터가 없습니다"
        
    lines = []
    for item_code, data in stock_data.items():
        lines.append(f"종목: {data.get('종목명', item_code)}")
        lines.append(f"  현재가: {data.get('현재가', 'N/A')}")
        lines.append(f"  등락율: {data.get('등락율', 'N/A')}%")
        lines.append(f"  거래량: {data.get('거래량', 'N/A')}")
        lines.append(f"  매도호가: {data.get('매도호가', 'N/A')}")
        lines.append(f"  매수호가: {data.get('매수호가', 'N/A')}")
        lines.append("")
        
    return "\n".join(lines) 