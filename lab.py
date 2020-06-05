from madt_lib.network import Network, Overlay


def main():
    net = Network('15.0.0.0/8')
    node1 = net.create_node('peer0.org1.example.com', image='hyperledger/fabric-peer:latest',enviroment={"","",""}, entrypoint="sleep infinity", ports={'7051/tcp': 7051}, privileged=True)
    node2 = net.create_node('peer0.org2.example.com', image='hyperledger/fabric-peer:latest',enviroment={"","",""}, entrypoint="sleep infinity", ports={'9051/tcp': 7051}, privileged=True)
    node3 = net.create_node('orderer.example.com', image='hyperledger/fabric-orderer:latest',enviroment={"","",""}, entrypoint="sleep infinity", ports={'7050/tcp': 7050}, privileged=True)
    net.create_subnet('net', (node1, node2, node3))

    net.configure(verbose=True)
    net.render('../../madt/labs/HL_Fabric', verbose=True)

if __name__ == "__main__":
    main()