def subnetMask(cidr):
    return "1" * cidr + "0" * (32-cidr)

def main():
    ip_address=["192.168.222.0/27","192,168.100.0/24","192.168.200.0/28","192.168.50.0/22"]
    ip1 = str(ip_address[0])
    ip2 = str(ip_address[1])
    ip3 = str(ip_address[2])
    ip4 = str(ip_address[3])
    cidr1 = int(ip1[14:])
    cidr2 = int(ip2[14:])
    cidr3 = int(ip3[14:])
    cidr4 = int(ip4[14:])
    subnetMask1 = subnetMask(cidr1)
    subnetMask2 = subnetMask(cidr2)
    subnetMask3 = subnetMask(cidr3)
    subnetMask4 = subnetMask(cidr4)
    listaSubnet = [subnetMask1, subnetMask2, subnetMask3, subnetMask4]
    with open("esVerifica2.3.txt", 'w') as file:
        file.write(str(ip_address))
        file.write("\n")
        file.write(str(listaSubnet))

if __name__ == "__main__":
    main()