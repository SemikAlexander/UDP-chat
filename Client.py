import socket, time

def Main():
    host = input("Enter server ip: ")
    port = 0
    server = ("127.0.0.1", 5000)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))
    s.sendto("ilghaiughlisahgraliugWAOH;VLRIUBEIALIUEBAI".encode("utf-8"), server)
    alias = input("Enter your name: ")
    message = input("-> ")
    while message != "q":
        s.sendto("[{}]-> {}".format(alias,message).encode("utf-8"), server)
        message = input("-> ")
        if "liugliuaeghuire9uhg35oq9hg8ovubtg78oHAEP0GOwv87ubiyogbugWgo8yuo8BGV87BwoiegboIB" in message:
            print("Shutdown request sent...")
            print("Shutting down...")
            time.sleep(3)
            break
    if "liugliuaeghuire9uhg35oq9hg8ovubtg78oHAEP0GOwv87ubiyogbugWgo8yuo8BGV87BwoiegboIB" not in message:
        s.sendto("adfbheiuarbfjklaeglhuaerliguhadfliuvbaile".encode("utf-8"), server)
    s.close()
if __name__ == "__main__":
    Main()