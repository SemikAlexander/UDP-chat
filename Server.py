import socket
from time import gmtime, strftime
import time

def Main():
    host = "localhost"
    port = 5000
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))
    listeners = []
    clients = []
    log = open("Log.txt", "w")
    log.write("--------------Server started at {}--------------".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()))+ "\n")
    print("Server Started")
    while True:
        try:
            data, addr = s.recvfrom(1024)
            data = data.decode("utf-8")
            if "luhgauhlgahughahilgauifgaliurGH;AUOGHO;BVA" in data:
                if addr not in listeners:
                    listeners.append(addr)
                    print("({})New listner connected: {}".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()),addr)+ "\n")
                    log.write("({})New listner connected: {}".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()),addr)+ "\n")
            elif "ilghaiughlisahgraliugWAOH;VLRIUBEIALIUEBAI" in data:
                if addr not in clients:
                    clients.append(addr)
                    print("({})New client connected: {}".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()),addr)+ "\n")
                    log.write("({})New client connected: {}".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()),addr)+"\n")
            elif "liugliuaeghuire9uhg35oq9hg8ovubtg78oHAEP0GOwv87ubiyogbugWgo8yuo8BGV87BwoiegboIB" in data:
                print("Shutdown request recieved from {} at {}".format(addr,strftime("%Y-%m-%d %H:%M:%S", gmtime())+ "\n"))
                log.write("Shutdown request recieved from {} at {}".format(addr,strftime("%Y-%m-%d %H:%M:%S", gmtime())+ "\n"))
                for i in range(len(listeners)):
                    s.sendto("Server: Shutting down in five seconds.".encode("utf-8"), listeners[i])
                    s.sendto("dfiasgheoivuhaeoiufgahoiguvhaeoifuegoiufgaf7483q4ogv".encode("utf-8"), listeners[i])
                time.sleep(5)
                break
            elif "adfbheiuarbfjklaeglhuaerliguhadfliuvbaile" in data:
                if addr in clients:
                    clients.remove(addr)
                    print("({}) has disconnected: {}".format(addr,strftime("%Y-%m-%d %H:%M:%S", gmtime()))+ "\n")
                    for i in range(len(listeners)):
                        s.sendto("({}) has disconnected: {}".format(addr,strftime("%Y-%m-%d %H:%M:%S", gmtime()))+ "\n".encode("utf-8"),listeners[i])             
            else:
                print("{} ({}) {}".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()), addr, data))
                log.write("{} ({}) {}".format(addr, strftime("%Y-%m-%d %H:%M:%S", gmtime()), data)+ "\n")
                for i in range(len(listeners)):
                    s.sendto(data.encode("utf-8"),listeners[i])
        except:
            pass
    s.close()
    log.close()
if __name__ == "__main__":
    Main()
