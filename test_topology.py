#!/usr/bin/python

from mininet.topo import Topo, SingleSwitchTopo
from mininet.net import Mininet
from mininet.log import lg, info
from mininet.cli import CLI

def main():
    lg.setLogLevel('info')

    net = Mininet(SingleSwitchTopo(k=2))
    net.start()

    h1 = net.get('h1')
    h2 = net.get('h2')
    s1 = net.get('s1')

    net.addLink(h1, s1)

    h1.setIP('10.0.1.1', intf='h1-eth0')
    h1.setIP('10.0.1.2', intf='h1-eth1')
    h2.setIP('10.0.1.3', intf='h2-eth0')
    CLI( net )
    net.stop()

if __name__ == '__main__':
    main()