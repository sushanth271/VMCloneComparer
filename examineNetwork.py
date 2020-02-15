import network_pb2

vm1network = network_pb2.networkConfig()
vm1network.autonegation = "true"
print vm1network.autonegation

