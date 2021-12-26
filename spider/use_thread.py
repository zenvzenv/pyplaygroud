from threading import Thread


class MyThread(Thread):
    def run(self) -> None:
        for i in range(1000):
            print('thread', i)


def func():
    for i in range(1000):
        print('func', i)


if __name__ == '__main__':
    t = Thread(target=func())
    t.start()
    for i in range(1000):
        print('main', i)

    t2 = MyThread()
    t2.start()
