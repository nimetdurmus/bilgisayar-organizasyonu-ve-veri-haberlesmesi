import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 5000))

print("4000 bayt veri bekleniyor...")

data, address = sock.recvfrom(65535)

print("Gonderen:", address)
print("Alinan uygulama verisi:", len(data), "bayt")
print("Ilk 40 bayt:", data[:40])

sock.close()
#Nimet Durmuş
