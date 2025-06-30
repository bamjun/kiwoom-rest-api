"""
웹소켓 클라이언트 테스트
"""

import pytest
import asyncio
from unittest.mock import Mock, patch, AsyncMock

from kiwoom_rest_api.websocket import WebSocketClient, RealTimeData, WebSocketError
from kiwoom_rest_api.websocket_helper import SimpleWebSocketClient, RealTimeDataProcessor
from kiwoom_rest_api.websocket_constants import get_field_name, get_type_name, REALTIME_TYPES

class TestWebSocketClient:
    """WebSocketClient 테스트"""
    
    def test_init(self):
        """초기화 테스트"""
        client = WebSocketClient(access_token="test_token")
        assert client.access_token == "test_token"
        assert client.connected == False
        assert client.is_logged_in == False
        assert client.keep_running == True
        
    def test_init_with_custom_url(self):
        """커스텀 URL로 초기화 테스트"""
        custom_url = "wss://custom.example.com/ws"
        client = WebSocketClient(access_token="test_token", ws_url=custom_url)
        assert client.ws_url == custom_url

class TestRealTimeData:
    """RealTimeData 테스트"""
    
    def test_init(self):
        """RealTimeData 초기화 테스트"""
        data = {
            'trnm': 'REAL',
            'return_code': 0,
            'return_msg': 'success',
            'data': []
        }
        realtime_data = RealTimeData(data)
        assert realtime_data.trnm == 'REAL'
        assert realtime_data.return_code == 0
        assert realtime_data.return_msg == 'success'
        assert realtime_data.data == []

class TestRealTimeDataProcessor:
    """RealTimeDataProcessor 테스트"""
    
    def test_init(self):
        """초기화 테스트"""
        processor = RealTimeDataProcessor()
        assert processor.data_handlers == {}
        assert processor.balance_data == {}
        assert processor.stock_data == {}
        
    def test_register_handler(self):
        """핸들러 등록 테스트"""
        processor = RealTimeDataProcessor()
        handler = Mock()
        processor.register_handler('04', handler)
        assert processor.data_handlers['04'] == handler
        
    def test_process_balance_data(self):
        """잔고 데이터 처리 테스트"""
        processor = RealTimeDataProcessor()
        values = {
            '9001': '005930',
            '302': '삼성전자',
            '10': '70000',
            '930': '100'
        }
        
        result = processor._process_balance_data('005930', values)
        assert result['종목코드'] == '005930'
        assert result['종목명'] == '삼성전자'
        assert result['현재가'] == '70000'
        assert result['보유수량'] == '100'
        assert result['데이터타입'] == '잔고'
        
    def test_process_stock_data(self):
        """주식 데이터 처리 테스트"""
        processor = RealTimeDataProcessor()
        values = {
            '9001': '005930',
            '900': '삼성전자',
            '10': '70000',
            '12': '2.5'
        }
        
        result = processor._process_stock_data('0B', '005930', values)
        assert result['종목코드'] == '005930'
        assert result['종목명'] == '삼성전자'
        assert result['현재가'] == '70000'
        assert result['등락율'] == '2.5'
        assert result['데이터타입'] == '주식체결'

class TestSimpleWebSocketClient:
    """SimpleWebSocketClient 테스트"""
    
    def test_init(self):
        """초기화 테스트"""
        client = SimpleWebSocketClient(access_token="test_token")
        assert client.client.access_token == "test_token"
        assert isinstance(client.processor, RealTimeDataProcessor)
        
    def test_register_data_handler(self):
        """데이터 핸들러 등록 테스트"""
        client = SimpleWebSocketClient(access_token="test_token")
        handler = Mock()
        client.register_data_handler('04', handler)
        assert client.processor.data_handlers['04'] == handler

class TestWebSocketConstants:
    """웹소켓 상수 테스트"""
    
    def test_get_field_name(self):
        """필드명 조회 테스트"""
        # 잔고 필드
        assert get_field_name('04', '9001') == '종목코드'
        assert get_field_name('04', '302') == '종목명'
        assert get_field_name('04', '10') == '현재가'
        
        # 주식체결 필드
        assert get_field_name('0B', '9001') == '종목코드'
        assert get_field_name('0B', '12') == '등락율'
        
        # 알 수 없는 필드
        assert get_field_name('04', '9999') == '9999'
        
    def test_get_type_name(self):
        """타입명 조회 테스트"""
        assert get_type_name('04') == '잔고'
        assert get_type_name('0B') == '주식체결'
        assert get_type_name('0C') == '주식우선호가'
        assert get_type_name('99') == '99'  # 알 수 없는 타입
        
    def test_realtime_types(self):
        """실시간 타입 상수 테스트"""
        assert '04' in REALTIME_TYPES
        assert '0B' in REALTIME_TYPES
        assert '0C' in REALTIME_TYPES
        assert REALTIME_TYPES['04'] == '잔고'
        assert REALTIME_TYPES['0B'] == '주식체결'

class TestWebSocketError:
    """WebSocketError 테스트"""
    
    def test_init(self):
        """초기화 테스트"""
        error = WebSocketError("테스트 오류")
        assert error.message == "테스트 오류"
        assert error.error_data == {}
        
    def test_init_with_error_data(self):
        """오류 데이터와 함께 초기화 테스트"""
        error_data = {'code': 1001, 'detail': '연결 실패'}
        error = WebSocketError("테스트 오류", error_data)
        assert error.message == "테스트 오류"
        assert error.error_data == error_data

# 통합 테스트
class TestIntegration:
    """통합 테스트"""
    
    @pytest.mark.asyncio
    async def test_websocket_client_lifecycle(self):
        """웹소켓 클라이언트 생명주기 테스트"""
        client = WebSocketClient(access_token="test_token")
        
        # 연결 전 상태 확인
        assert client.connected == False
        assert client.is_logged_in == False
        
        # 연결 시뮬레이션
        client.connected = True
        client.is_logged_in = True
        
        assert client.connected == True
        assert client.is_logged_in == True
        
        # 중지 시뮬레이션
        await client.stop()
        assert client.keep_running == False

if __name__ == "__main__":
    pytest.main([__file__]) 