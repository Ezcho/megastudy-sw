import socket
import threading
import sys

def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            if msg:
                print(msg)
            else:
                break
        except:
            break

def main():
    host = "192.168.10.4" #ip주소 입력
    port = 20001 #0~25565 번 중 아무거나 입력

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket 객체를 생성
    try:
        client.connect((host, port)) #연결 시도.
    except:
        print("서버에 연결할 수 없습니다.") #연결을 할 수 없을 때 띄우는 메시지
        sys.exit()

    print("서버에 연결되었습니다. 메시지를 입력하세요 (Ctrl+C로 종료).")

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.daemon = True
    receive_thread.start()

    try:
        while True: #무한 반복
            msg = input() #msg가 입력되길 기다린다.
            if msg:
                client.send(msg.encode()) 
    except KeyboardInterrupt:
        print("\n[!] 클라이언트를 종료합니다.")
        client.close()
        sys.exit()

if __name__ == "__main__":
    main()
