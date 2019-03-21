import socket, time

def Main():
    host = input("Enter server ip: ")
    port = 0
    server = ("127.0.0.1", 5000)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))
    s.sendto("luhgauhlgahughahilgauifgaliurGH;AUOGHO;BVA".encode("utf-8"), server)
    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode("utf-8")
        if "dfiasgheoivuhaeoiufgahoiguvhaeoifuegoiufgaf7483q4ogv" in data:
            time.sleep(5)
        print(str(data))
if __name__ == "__main__":
    Main()