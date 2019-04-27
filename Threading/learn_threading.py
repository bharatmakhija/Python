import threading

class Messenger(threading.Thread):

    def run(self):
        for _ in range(1000):
            print(threading.current_thread().getName())


x = Messenger(name='send out messages')
y = Messenger(name = 'receive messages')
x.start() # start kicks of a thread and thread looks for a
y.start()