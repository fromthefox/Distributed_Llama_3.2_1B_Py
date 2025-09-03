"""
this file is used to finish the inference task for worker node
"""
import socket
from socket_client import TCPClient

def inference_main_for_worker():
    """
    this function is used to finish the inference task for worker node
    """
    host, port = "127.0.0.1", 34567
    client = TCPClient(host, port)
    client.start_handling()

inference_main_for_worker()