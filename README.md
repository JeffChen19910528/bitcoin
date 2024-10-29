install bitcoin:
https://bitcoin.org/en/download

Unzip:
tar xzf bitcoin-27.0-x86_64-linux-gnu.tar.gz

install bitcoin:
sudo install -m 0755 -o root -g root -t /usr/bin bitcoin-27.0/bin/*

set environmental variables:
vi ~/.bitcoin/bitcoin.conf

server=1
daemon=1

rpcuser=testuser
rpcpassword=testpassword123
rpcallowip=127.0.0.1

[regtest]
regtest=1


give permission:
chmod 600 ~/.bitcoin/bitcoin.conf


test bitcoin:
./wallet_test.sh

get bitcoin:
python3 explore_bitcoin.py

