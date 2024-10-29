from bitcoinrpc.authproxy import AuthServiceProxy
import json
import time

def print_json(data):
    """格式化輸出 JSON 數據"""
    print(json.dumps(data, indent=2, ensure_ascii=False))

def explore_bitcoin_network():
    """探索比特幣私有鏈網路"""
    
    # 連接設置
    rpc_connection = AuthServiceProxy(
        "http://testuser:testpassword123@127.0.0.1:18443"
    )
    
    try:
        print("\n=== 比特幣私有鏈探索工具 ===")
        
        # 1. 區塊鏈基本資訊
        print("\n1. 區塊鏈狀態:")
        blockchain_info = rpc_connection.getblockchaininfo()
        print(f"- 當前區塊高度: {blockchain_info['blocks']}")
        print(f"- 區塊鏈大小: {blockchain_info['size_on_disk']/1024/1024:.2f} MB")
        print(f"- 最佳區塊哈希: {blockchain_info['bestblockhash']}")
        
        # 2. 最新區塊詳細資訊
        print("\n2. 最新區塊詳情:")
        latest_block = rpc_connection.getblock(blockchain_info['bestblockhash'])
        print(f"- 區塊時間: {time.ctime(latest_block['time'])}")
        print(f"- 區塊交易數: {len(latest_block['tx'])}")
        print(f"- 區塊難度: {latest_block['difficulty']}")
        
        # 3. 挖礦資訊
        print("\n3. 挖礦資訊:")
        mining_info = rpc_connection.getmininginfo()
        print(f"- 網路難度: {mining_info['difficulty']}")
        print(f"- 網路哈希率: {mining_info.get('networkhashps', 'N/A')}")
        
        # 4. 錢包資訊
        print("\n4. 錢包資訊:")
        balance = rpc_connection.getbalance()
        print(f"- 當前餘額: {balance} BTC")
        
        # 生成新地址
        new_address = rpc_connection.getnewaddress()
        print(f"- 新生成的地址: {new_address}")
        
        # 5. 未花費的交易輸出
        print("\n5. 未花費的交易輸出(UTXO):")
        unspent = rpc_connection.listunspent()
        for utxo in unspent[:5]:  # 只顯示前5個
            print(f"- 金額: {utxo['amount']} BTC")
            print(f"  地址: {utxo['address']}")
            print(f"  確認數: {utxo['confirmations']}")
            print()
            
        # 6. 生成新區塊
        print("\n6. 生成新區塊:")
        new_blocks = rpc_connection.generatetoaddress(1, new_address)
        print(f"- 新區塊哈希: {new_blocks[0]}")
        
        # 7. 交易池資訊
        print("\n7. 交易池資訊:")
        mempool = rpc_connection.getmempoolinfo()
        print(f"- 交易池大小: {mempool['size']} 交易")
        print(f"- 交易池內存使用: {mempool['usage']/1024:.2f} KB")
        
        # 8. 網路連接資訊
        print("\n8. 網路連接資訊:")
        network_info = rpc_connection.getnetworkinfo()
        print(f"- 版本: {network_info['version']}")
        print(f"- 子版本: {network_info['subversion']}")
        print(f"- 協議版本: {network_info['protocolversion']}")
        
        print("\n=== 探索完成 ===")
        
    except Exception as e:
        print(f"錯誤: {str(e)}")

if __name__ == "__main__":
    explore_bitcoin_network()