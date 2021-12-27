def consumer():
    print('4. 开始执行消费者生成器代码')
    response = None
    while True:
        print('5. yield 终端，保存上下文')
        n = yield response
        print(f'n -> {n}')
        print('8. 获取上下文，继续往下执行')
        if not n:
            return
        print("[Consumer]: consuming {} ..".format(n))
        response = 'ok'


def produce(c):
    print('3. 启动生产者生成器，开始执行 consumer 生成器')
    # 启动生成器，开始执行生成器consumer
    c.send(None)
    print('6. 继续往下执行')
    n = 0
    while n < 5:
        n += 1
        print("[Producer]: producing {} ..".format(n))
        print("7、第{}次唤醒生成器，从yield位置继续往下执行！--".format(n + 1))
        r = c.send(n)
        print("9、从第8步往下--")
        print("[Producer]: consumer return {} ..".format(r))
    c.close()


if __name__ == '__main__':
    c = consumer()
    produce(c)
