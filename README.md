# Kiwoom REST API
Python client for interacting with [Kiwoom REST API](https://openapi.kiwoom.com/) and WebSocket real-time data.


## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
  - [Using pip](#using-pip)
  - [Using uv](#using-uv)
  - [Using Poetry](#using-poetry)
- [Usage](#Usage)
  - [REST API Usage](#rest-api-usage)
  - [WebSocket Usage](#websocket-usage)
- [CLI Usage](#CLI-Usage)
  - [Using uvx](#Using-uvx)
  - [Set API Key](#Set-API-Key)
- [Docs](#Docs)
- [License](#license)

## Features

- **REST API Client**: 키움증권 REST API를 위한 Python 클라이언트
- **WebSocket Client**: 실시간 데이터 수신을 위한 웹소켓 클라이언트
- **Real-time Data**: 잔고, 주식체결, 호가 등 실시간 데이터 지원
- **Easy to Use**: 간단하고 직관적인 API
- **Auto Reconnect**: 자동 재연결 기능
- **Multiple Clients**: 여러 웹소켓 클라이언트 동시 관리

## Installation

### using pip
```bash
pip install kiwoom-rest-api
```

### using uv
```
uv add kiwoom-rest-api
```

### using poetry
```
poetry add kiwoom-rest-api
```

## Usage

### REST API Usage

```python
import os
os.environ["KIWOOM_API_KEY"] = "your_api_key"
os.environ["KIWOOM_API_SECRET"] = "your_api_secret"

from kiwoom_rest_api.koreanstock.stockinfo import StockInfo
from kiwoom_rest_api.auth.token import TokenManager

# 토큰 매니저 초기화
token_manager = TokenManager()

# StockInfo 인스턴스 생성 (base_url 수정)
stock_info = StockInfo(base_url="https://api.kiwoom.com", token_manager=token_manager)

try:
    result = stock_info.basic_stock_information_request_ka10001("005930")
    print("API 응답:", result)
except Exception as e:
    print("에러 발생:", str(e))
```

### WebSocket Usage

#### 간단한 사용법

```python
import os
from kiwoom_rest_api import SimpleWebSocketClient

# 액세스 토큰 설정
ACCESS_TOKEN = os.environ.get("KIWOOM_ACCESS_TOKEN", "your_access_token")

# 클라이언트 생성
client = SimpleWebSocketClient(access_token=ACCESS_TOKEN)

# 데이터 핸들러 등록 (선택사항)
def on_balance_data(data):
    print("잔고 데이터 수신:", data)

client.register_data_handler('04', on_balance_data)

# 실행 (Ctrl+C로 중단 가능)
client.run_sync(type_list=['04'])  # 잔고 데이터만 수신
```

#### 고급 사용법

```python
import asyncio
from kiwoom_rest_api import WebSocketClient, RealTimeData

async def main():
    # 클라이언트 생성
    client = WebSocketClient(access_token="your_access_token")
    
    # 콜백 함수들 설정
    async def on_data_received(realtime_data: RealTimeData):
        if realtime_data.trnm == 'REAL':
            print(f"실시간 데이터 수신: {len(realtime_data.data)}개 항목")
    
    async def on_logged_in():
        print("로그인 성공")
        # 잔고 데이터 등록
        await client.register_realtime(type_list=['04'])
    
    # 콜백 함수들 등록
    client.on_data = on_data_received
    client.on_login = on_logged_in
    
    # 클라이언트 시작
    await client.start()
    
    # 30초간 실행
    await asyncio.sleep(30)
    await client.stop()

# 실행
asyncio.run(main())
```

#### 여러 클라이언트 관리

```python
import asyncio
from kiwoom_rest_api import WebSocketManager

async def main():
    # 매니저 생성
    manager = WebSocketManager()
    
    # 여러 클라이언트 추가
    await manager.add_client(
        client_id="balance_client",
        access_token="your_access_token",
        type_list=['04']  # 잔고
    )
    
    await manager.add_client(
        client_id="stock_client", 
        access_token="your_access_token",
        type_list=['0B'],  # 주식체결
        item_list=['005930']  # 삼성전자
    )
    
    # 20초간 실행
    await asyncio.sleep(20)
    await manager.stop_all()

asyncio.run(main())
```

#### 실시간 데이터 타입

| 코드 | 설명 |
|------|------|
| `04` | 잔고 |
| `0A` | 주식기세 |
| `0B` | 주식체결 |
| `0C` | 주식우선호가 |
| `0D` | 주식호가잔량 |
| `0E` | 주식시간외호가 |
| `0F` | 주식당일거래원 |
| `0G` | ETF NAV |
| `0H` | 주식예상체결 |
| `0J` | 업종지수 |
| `0U` | 업종등락 |

## CLI Usage

### Using uvx
```bash
uvx --from kiwoom-rest-api kiwoom -k "YOUR_KEY" -s "YOUR_SECRET" ka10001 005930
```

### Set API Key
```bash
# Linux/macOS/Windows(git bash)
export KIWOOM_API_KEY="YOUR_ACTUAL_API_KEY"
export KIWOOM_API_SECRET="YOUR_ACTUAL_API_SECRET"
export KIWOOM_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"  # 웹소켓용

# Windows (CMD)
set KIWOOM_API_KEY="YOUR_ACTUAL_API_KEY"
set KIWOOM_API_SECRET="YOUR_ACTUAL_API_SECRET"
set KIWOOM_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

# Windows (PowerShell)
$env:KIWOOM_API_KEY="YOUR_ACTUAL_API_KEY"
$env:KIWOOM_API_SECRET="YOUR_ACTUAL_API_SECRET"
$env:KIWOOM_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
```

```bash
# 가상 환경 활성화 (필요시)
poetry shell

# 도움말 보기
kiwoom --help
kiwoom ka10001 --help

# ka10001 명령어 실행 (환경 변수 사용 시)
kiwoom ka10001 005930 # 삼성전자 예시

# ka10001 명령어 실행 (옵션 사용 시)
kiwoom --api-key "YOUR_KEY" --api-secret "YOUR_SECRET" ka10001 005930

# 다른 base URL 사용 시
kiwoom --base-url "https://mockapi.kiwoom.com" ka10001 005930
```

## Examples

웹소켓 사용 예제는 `examples/websocket_example.py` 파일을 참조하세요.

```bash
# 예제 실행
python examples/websocket_example.py
```

# Docs
[pypi](https://pypi.org/project/kiwoom-rest-api/)
[github](https://github.com/bamjun/kiwoom-rest-api)

# License

This project is licensed under the terms of the MIT license.