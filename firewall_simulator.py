import random


class Packet:
    def __init__(self, protocol, port, source_ip):
        self.protocol = protocol
        self.port = port
        self.source_ip = source_ip

    def __repr__(self):
        return f"Packet(protocol={self.protocol}, port={self.port}, source_ip={self.source_ip})"



class Firewall:
    def __init__(self):
        
        self.rules = []

    def add_rule(self, protocol, port, action):
        """
        Add a rule to the firewall.
        :param protocol: Protocol to filter (e.g., "TCP", "UDP")
        :param port: Port to filter (e.g., 80, 443)
        :param action: Action for the rule ("allow" or "deny")
        """
        self.rules.append((protocol, port, action))

    def check_packet(self, packet):
        """
        Check the packet against the firewall rules.
        :param packet: The packet to check
        :return: "Allowed" or "Denied"
        """
        for rule in self.rules:
            rule_protocol, rule_port, rule_action = rule

           
            if packet.protocol == rule_protocol and packet.port == rule_port:
                return f"Packet {packet} is {rule_action.upper()}"
       
        return f"Packet {packet} is DENIED"

    def simulate_packets(self, num_packets=5):
        """
        Simulate random packets passing through the firewall.
        :param num_packets: Number of packets to simulate
        """
        protocols = ['TCP', 'UDP']
        ports = [80, 443, 22, 8080, 53]
        source_ips = ['192.168.1.1', '10.0.0.1', '172.16.0.1']

        for _ in range(num_packets):
            protocol = random.choice(protocols)
            port = random.choice(ports)
            source_ip = random.choice(source_ips)
            packet = Packet(protocol, port, source_ip)
            result = self.check_packet(packet)
            print(result)


firewall = Firewall()

firewall.add_rule('TCP', 80, 'allow')    
firewall.add_rule('UDP', 53, 'allow')    
firewall.add_rule('TCP', 22, 'deny')     


print("Simulating packets:")
firewall.simulate_packets(10) 

