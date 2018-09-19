#!/usr/bin/env python

import websocket
import argparse

from multiprocessing import Pool

parser = argparse.ArgumentParser(description='connect to websocket')
parser.add_argument('--N', default=1, type=int, help='number of serial connection')
parser.add_argument('--M', default=3, type=int, help='number of serial queries') 
parser.add_argument('--delay', default=1, type=int, help='delay in seconds between queries') 
args = parser.parse_args()

n = args.N
m = args.M
delay = args.delay

try:
    import thread
except ImportError:
    import _thread as thread
import time

def on_message(ws, message):
    print('Answer from server %s' %  message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        for i in range(m):
	    time.sleep(delay)
            ws.send("Hello %d" % i)
        time.sleep(delay)
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())

def f(x):
    ws = websocket.WebSocketApp("ws://localhost/echo",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()

if __name__ == '__main__':
    websocket.enableTrace(True)
    p = Pool(n)
    results = [ p.map(f, range(n)) ]
