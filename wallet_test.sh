#!/bin/bash

echo "=== 比特幣私有鏈錢包測試 ==="

# 1. 確保節點正在運行
if ! bitcoin-cli -regtest getblockchaininfo > /dev/null 2>&1; then
    echo "啟動比特幣節點..."
    bitcoind -regtest -daemon
    sleep 5
fi

# 2. 創建新錢包
echo -e "\n1. 創建新錢包..."
bitcoin-cli -regtest createwallet "mywallet" || echo "錢包可能已存在"

# 3. 生成新地址
echo -e "\n2. 生成新地址..."
NEW_ADDRESS=$(bitcoin-cli -regtest getnewaddress)
echo "新地址: $NEW_ADDRESS"

# 4. 生成區塊獲得測試幣
echo -e "\n3. 生成區塊..."
bitcoin-cli -regtest generatetoaddress 101 "$NEW_ADDRESS"
echo "已生成 101 個區塊"

# 5. 查看錢包信息
echo -e "\n4. 錢包信息:"
bitcoin-cli -regtest getwalletinfo

# 6. 查看餘額
echo -e "\n5. 當前餘額:"
BALANCE=$(bitcoin-cli -regtest getbalance)
echo "$BALANCE BTC"

# 7. 生成第二個地址用於測試交易
echo -e "\n6. 生成第二個地址用於測試..."
SECOND_ADDRESS=$(bitcoin-cli -regtest getnewaddress)
echo "第二個地址: $SECOND_ADDRESS"

# 8. 發送測試交易
echo -e "\n7. 發送測試交易..."
TXID=$(bitcoin-cli -regtest sendtoaddress "$SECOND_ADDRESS" 1.0)
echo "交易ID: $TXID"

# 9. 生成新區塊確認交易
echo -e "\n8. 確認交易..."
bitcoin-cli -regtest generatetoaddress 1 "$NEW_ADDRESS"

# 10. 查看交易詳情
echo -e "\n9. 交易詳情:"
bitcoin-cli -regtest gettransaction "$TXID"

# 11. 列出未花費的交易輸出
echo -e "\n10. 未花費的交易輸出 (UTXO):"
bitcoin-cli -regtest listunspent

echo -e "\n=== 測試完成 ==="