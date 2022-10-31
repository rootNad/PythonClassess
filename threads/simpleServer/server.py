from argparse import ArgumentParser
from threading import Lock, Thread
from socket import SO_REUSEADDR, SOCK_STREAM, socket, SOL_SOCKET, AF_INET


parser = ArgumentParser(description="MultiThread TCP Server")

parser.add_argument("-p", "--port", default=9000, type=int, help="Port over which to connect")

args = parser.parse_args()

counter = 0
response_message = "Now serving, number: "
thread_lock = Lock()

s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(("localhost", args.port))

threads = []

class ClientHandler(Thread):
    def __init__(self, address, port, socket, response_message, )