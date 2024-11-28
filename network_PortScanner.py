# import socket

# def port_scan(target, ports):
    # for port in ports:
        # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # sock.settimeout(1)
        # result = sock.connect_ex((target, port))
        # if result == 0:
            # print(f"Port {port} is open")
        # sock.close()

# target = "31.13.71.36"
# ports = [80, 443, 21, 22, 25]
# port_scan(target, ports)

## To update: UDP socket connection not properly working

import socket, sys, datetime, time

startTime = time.time()
ip_addr = ""
hostname = ""

def port_scan(target , ports):
    global hostname, ip_addr, domain
    print(f"Network scan report for [{ip_addr}]")
    # print(f"Hostname: {hostname}")
    # print(f"IP Address: {ip_addr}")
    if not ports:
        print("Scanning all ports...")
        for port in range(65536):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout()
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is open")
            sock.close()
        print("Time taken: %.lf" % (time.time() - startTime))
    else:
        print("Scanning specified port/s...")
        print("PORT         STATE   SERVICE")
        for port in ports:
            flag_TCP = 0
            
            sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock_tcp.settimeout()
            result_TCP = sock_tcp.connect_ex((target, port))
            if result_TCP == 0:
                # print(f"Port {port} is open")
                print(f"{port}/tcp          open    http")
                flag_TCP = 1
            sock_tcp.close()
            
            if flag_TCP == 0:
                sock_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock_udp.settimeout(1)
                result_UDP = sock_udp.connect_ex((target, port))
                if result_UDP == 0:
                    print(f"{port}/udp          open    http")
                sock_udp.close()
        print("Time taken: %.lf" % (time.time() - startTime))
def main():
    if len(sys.argv) < 2:
        print("Usage: python portscanner.py <target> <flag> [port1,port2,port3,...]")
        return
    
    print(f"Starting Network Port Scanner (https://rvin1228.github.io/) at {datetime.datetime.now()}")
    target = sys.argv[1]
    get_info(target)
    
    if "-D" in sys.argv:#Default ports
        ports = range(1,1001)
    elif len(sys.argv) > 2: #Specific ports
        ports = [int(port) for port in sys.argv[2].split(",")]
    else: #Default ports
        ports = []
    
    port_scan(target, ports) #Main execution
    

def get_info(address):
    global hostname, ip_addr
    try:
        ip_addr = socket.gethostbyname(address)
        hostname = socket.gethostbyaddr(ip_addr)[0]
    except socket.gaierror:
        print(f"Could not resolve the address: {address}")
        sys.exit(0)
    
if __name__ == "__main__":
    main()