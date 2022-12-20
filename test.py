import time

h = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
listeners = ['9000', '9001', '9002', '9003', '9004', '9005']
ipAdress = ['10.10.101.2', '10.10.101.2', '10.10.102.2', '10.10.102.2', '10.10.103.2', '10.10.103.2']
ipAdressRegion = ['10.10.1.1', '10.10.2.1', '10.10.3.1']
selfIp = '10.10.200.1'


def test(net):
    # on first server start the listener
    # net.get("h1").sendCmd("python3 -m http.server 9000 &")

    # Start all the clients
    for i in range(6):
        net.get(h[i]).sendCmd("python3 -m http.server " + listeners[i] + " &")
        print("Done")

    # print("Running base test with only one server")
    # time.sleep(4)
    # print("Done")
    return