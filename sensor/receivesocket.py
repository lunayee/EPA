
import datetime
import socket
import time
import DBmysql
import requests


HEADER = 2048 # 指定要接收的數據大小
PORT = 3333
SERVER = "192.168.3.107"
#SERVER = socket.gethostbyname(socket.gethostname())# 對server端為主機位置
ADDR = (SERVER,PORT)
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(ADDR)

CLIENT = "192.168.3.80"
CLIENT_PORT = 8000

def getData():
    conn,addr = server.recvfrom(HEADER)# 接受遠程計算機的連接請求，建立起與客戶機之間的通信連接
    change_dict = str(conn, encoding = "utf-8")
    data=eval(change_dict)
    #print(f"[CONNCTION] {addr}  {data}")
    return data


def main():
    DATA = getData()
    Table = DATA.get('TABLE')
    Database = DATA.get('DATABASE')
    print(Table,DATA['Time'])
    del DATA['ID']
    del DATA['TABLE']
    del DATA['DATABASE']
    DBmysql.write_mysql(Database, Table, DATA)
        
    

if __name__ == '__main__':         
    print(f"[LISTENING] Server is listening on {SERVER}")  
    while(1):
        main()
