"""
this file is used to finish the inference task for worker node
"""
import socket
from socket_client import TCPClient

def inference_main_for_worker():
    """
    this function is used to finish the inference task for worker node
    """
    host_self, port_self, host_tar, port_tar = "127.0.0.1", 34567, "127.0.0.1", 44444
    client = TCPClient(host_self, port_self, host_tar, port_tar)
    client.start_handling()

inference_main_for_worker()