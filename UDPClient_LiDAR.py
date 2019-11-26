import socket
import rospy
import struct
from sensor_msgs.msg import LaserScan
import statistics

serverAddressPort = ("127.0.0.1", 9001)

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#get
def callback(msg):
	bytesToSend = struct.pack('%sf' % len(msg.ranges), *msg.ranges)
	# Send to server using created UDP socket
	UDPClientSocket.sendto(bytesToSend, serverAddressPort)
	


rospy.init_node('laser_data')
sub = rospy.Subscriber('scan', LaserScan, callback)
rospy.spin()