import csv
import random

direction = ["inbound", "outbound"]
protocol = ["tcp", "udp"]
port = [ _ for _ in range(1,120)]

def main():
    size = 1000000
    row_list = []
    #count = 0
    with open('test1.csv', 'w') as csv_out:
        writer = csv.writer(csv_out, delimiter=',')
        for i in range(size):
            dire = direction[random.randint(0,1)]
            proto = protocol[random.randint(0,1)]
            port = -123123
            ip = ""
            if random.randint(0,1):
                port = random.randint(1,65535)
            else:
                start_port = random.randint(1,40000)
                end_port = random.randint(start_port, 65535)
                port = "{}-{}".format(str(start_port), str(end_port))
            if random.randint(0,1):
                ip_list = [ str(random.randint(1,255)) for _ in range(4)]
                ip = ".".join(ip_list)
            else:
                start_ip_list = [ str(random.randint(1,200)) for _ in range(4)]
                start_ip = ".".join(start_ip_list)
                end_ip_list = [ str(random.randint(int(i),255)) for i in start_ip_list]
                end_ip = ".".join(end_ip_list)
                ip = "{}-{}".format(start_ip,end_ip)

            row = [dire, proto, port, ip]
            writer.writerow(row)
            #count += 1
            #print(count)

if __name__ == "__main__":
    main()
