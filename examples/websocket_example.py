#!/usr/bin/env python3
"""
키움증권 웹소켓 클라이언트 사용 예제

이 예제는 키움증권의 실시간 웹소켓 API를 사용하는 방법을 보여줍니다.
"""

import asyncio
import os
import logging
from typing import Dict, Any

# 환경변수에서 액세스 토큰 가져오기
ACCESS_TOKEN = os.environ.get("KIWOOM_ACCESS_TOKEN", "your_access_token_here")

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def example_simple_client():
    """간단한 웹소켓 클라이언트 사용 예제"""
    print("=== 간단한 웹소켓 클라이언트 예제 ===")
    
    from kiwoom_rest_api import SimpleWebSocketClient, format_balance_data
    
    # 클라이언트 생성
    client = SimpleWebSocketClient(access_token=ACCESS_TOKEN)
    
    # 데이터 핸들러 등록 (선택사항)
    def on_balance_data(data: Dict[str, Any]):
        print("잔고 데이터 수신:")
        print(format_balance_data(data))
    
    client.register_data_handler('04', on_balance_data)
    
    # 동기적으로 실행 (Ctrl+C로 중단 가능)
    try:
        client.run_sync(type_list=['04'])  # 잔고 데이터만 수신
    except KeyboardInterrupt:
        print("\n사용자에 의해 중단되었습니다")

async def example_advanced_client():
    """고급 웹소켓 클라이언트 사용 예제"""
    print("=== 고급 웹소켓 클라이언트 예제 ===")
    
    from kiwoom_rest_api import WebSocketClient, RealTimeData
    
    # 클라이언트 생성
    client = WebSocketClient(access_token=ACCESS_TOKEN)
    
    # 콜백 함수들 설정
    async def on_data_received(realtime_data: RealTimeData):
        """실시간 데이터 수신 시 호출"""
        if realtime_data.trnm == 'REAL':
            print(f"실시간 데이터 수신: {len(realtime_data.data)}개 항목")
            for item in realtime_data.data:
                print(f"  - {item.get('type')}: {item.get('item')}")
    
    async def on_connected():
        """연결 성공 시 호출"""
        print("웹소켓 서버에 연결되었습니다")
    
    async def on_logged_in():
        """로그인 성공 시 호출"""
        print("웹소켓 서버 로그인 성공")
        # 잔고 데이터 등록
        await client.register_realtime(type_list=['04'])
    
    async def on_error(error: Exception):
        """오류 발생 시 호출"""
        print(f"오류 발생: {error}")
    
    # 콜백 함수들 등록
    client.on_data = on_data_received
    client.on_connect = on_connected
    client.on_login = on_logged_in
    client.on_error = on_error
    
    # 클라이언트 시작
    await client.start()
    
    # 30초간 실행
    try:
        await asyncio.sleep(30)
    finally:
        await client.stop()

async def example_multiple_clients():
    """여러 웹소켓 클라이언트 관리 예제"""
    print("=== 여러 웹소켓 클라이언트 관리 예제 ===")
    
    from kiwoom_rest_api import WebSocketManager
    
    # 매니저 생성
    manager = WebSocketManager()
    
    # 여러 클라이언트 추가
    await manager.add_client(
        client_id="balance_client",
        access_token=ACCESS_TOKEN,
        type_list=['04']  # 잔고
    )
    
    await manager.add_client(
        client_id="stock_client", 
        access_token=ACCESS_TOKEN,
        type_list=['0B'],  # 주식체결
        item_list=['005930']  # 삼성전자
    )
    
    print(f"실행 중인 클라이언트: {manager.list_clients()}")
    
    # 20초간 실행
    try:
        await asyncio.sleep(20)
    finally:
        await manager.stop_all()

async def example_custom_data_processing():
    """커스텀 데이터 처리 예제"""
    print("=== 커스텀 데이터 처리 예제 ===")
    
    from kiwoom_rest_api import WebSocketClient, RealTimeData, get_field_name
    
    async def custom_data_handler(realtime_data: RealTimeData):
        """커스텀 데이터 핸들러"""
        if realtime_data.trnm != 'REAL':
            return
            
        for item_data in realtime_data.data:
            type_code = item_data.get('type')
            item_code = item_data.get('item')
            values = item_data.get('values', {})
            
            if type_code == '04':  # 잔고
                print(f"잔고 업데이트 - 종목: {item_code}")
                for field_code, value in values.items():
                    field_name = get_field_name('04', field_code)
                    print(f"  {field_name}: {value}")
                    
            elif type_code == '0B':  # 주식체결
                print(f"주식체결 - 종목: {item_code}")
                current_price = values.get('10', 'N/A')
                change_rate = values.get('12', 'N/A')
                print(f"  현재가: {current_price}, 등락율: {change_rate}%")
    
    # 클라이언트 생성 및 설정
    client = WebSocketClient(access_token=ACCESS_TOKEN)
    client.on_data = custom_data_handler
    
    # 시작
    await client.start()
    await client.register_realtime(type_list=['04', '0B'])
    
    # 15초간 실행
    try:
        await asyncio.sleep(15)
    finally:
        await client.stop()

async def main():
    """메인 함수"""
    print("키움증권 웹소켓 클라이언트 예제")
    print("=" * 50)
    
    if ACCESS_TOKEN == "your_access_token_here":
        print("⚠️  경고: ACCESS_TOKEN이 설정되지 않았습니다.")
        print("환경변수 KIWOOM_ACCESS_TOKEN을 설정하거나 코드에서 직접 설정하세요.")
        return
    
    # 예제들 실행
    examples = [
        ("고급 클라이언트", example_advanced_client),
        ("여러 클라이언트 관리", example_multiple_clients),
        ("커스텀 데이터 처리", example_custom_data_processing),
    ]
    
    for name, example_func in examples:
        print(f"\n{name} 예제 실행 중...")
        try:
            await example_func()
        except Exception as e:
            print(f"예제 실행 중 오류 발생: {e}")
        
        print(f"{name} 예제 완료")
        await asyncio.sleep(2)  # 예제 간 간격
    
    print("\n모든 예제 완료!")

if __name__ == "__main__":
    # 비동기 예제들 실행
    asyncio.run(main())
    
    # 동기 예제 실행 (별도로 실행하려면 주석 해제)
    # example_simple_client() 