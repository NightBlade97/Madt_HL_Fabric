from madt_lib.network import Network


def main():
    net = Network('16.0.0.0/8')
    # create network nodes that will represent client and server

    node_count = 5
    nodes = []
    for counter in range(node_count):
        node = net.create_node('Node'+str(counter), 
                               image='yeasy/hyperledger-fabric', entrypoint='sh -c "while true; do wget -O - -T 3 $SERVER; sleep 1; done"')
        nodes.append(node)
        
    # create a local network that will connect all those nodes
    net.create_subnet('hyperledger fabric', nodes)
    # distribute IP addresses
    net.configure(verbose=True)

    # save lab
    net.render('../labs/hyperledger_fabric', verbose=True)


if __name__ == "__main__":
    main()
