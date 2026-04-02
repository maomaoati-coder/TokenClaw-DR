import json
import uuid
import os
from datetime import datetime, timedelta

TOKEN_DB = "token_database.json"

def save_token(token_data):
    # 加载现有数据库或创建新数据库
    if os.path.exists(TOKEN_DB):
        with open(TOKEN_DB, 'r') as f:
            db = json.load(f)
    else:
        db = {}
    
    # 将新 Token 加入数据库
    db.update(token_data)
    
    with open(TOKEN_DB, 'w') as f:
        json.dump(db, f, indent=4)

def generate_dr_token():
    print("="*50)
    print("TokenClaw-DR: Distribution Rights Issuance Panel")
    print("="*50)
    
    # 1. 输入客户或合作伙伴名称
    client_name = input("[?] Enter Client Name (e.g. Dan_Intel): ")
    
    # 2. 输入授权的资产名称
    asset_id = input("[?] Enter Asset ID (e.g. ChaKou_3nm_Core): ")
    
    # 3. 设置有效期
    days = int(input("[?] Enter validity period (Days): "))
    expiry_date = (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%d")
    
    # 4. 生成唯一的 Token (带 MAO- 前缀)
    unique_id = str(uuid.uuid4()).split('-')[0].upper()
    token = f"MAO-{unique_id}"
    
    # 5. 构建授权数据结构
    auth_info = {
        token: {
            "client_name": client_name,
            "asset": asset_id,
            "expiry": expiry_date,
            "issued_at": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
    }
    
    # 6. 保存并输出结果
    save_token(auth_info)
    
    print("\n" + "*"*50)
    print(f"SUCCESS: Distribution Rights Granted to {client_name}")
    print(f"ASSET  : {asset_id}")
    print(f"EXPIRY : {expiry_date}")
    print(f"TOKEN  : {token}")
    print("*"*50)
    print("\n[!] Please COPY the TOKEN and provide it to the client.")

if __name__ == '__main__':
    generate_dr_token()
