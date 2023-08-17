import socket

def fuzzer(target_ip, target_port):
    payload = b"A" * 1000  # Örnek olarak 1000 baytlık "A" karakterleri ile doldurulmuş bir payload
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))
        print("Bağlantı başarılı.")
        
        s.send(payload)
        print(f"{len(payload)} bayt veri gönderildi.")
        
        response = s.recv(1024)
        print("Cevap alındı:", response)
    except Exception as e:
        print("Hata:", e)
    finally:
        s.close()

if __name__ == "__main__":
    target_ip = input("Hedef IP adresini girin: ")
    target_port = int(input("Hedef port numarasını girin: "))
    
    fuzzer(target_ip, target_port)
