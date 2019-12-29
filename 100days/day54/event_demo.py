import threading
import time

# 创建事件
event = threading.Event()


def drive(name):
    i = 0
    while True:
        i = i + 1
        print(name + "正在行驶中，行驶了" + str(i * 60) + "Km")
        time.sleep(1)
        event.wait()
        print(name + '通过了红灯')


# 红绿灯信号
def sign():
    print("绿灯初始化")
    #  将 flag 设为 True，通知所有处于阻塞状态的线程恢复运行状态。
    event.set()
    while True:
        time.sleep(3)
        if event.isSet():
            print("红灯亮起，所有行驶中的车辆不允许通过")
            event.clear()
        else:
            print("绿灯亮起，所有行驶中的车辆必须通过")
            event.set()


if __name__ == '__main__':
    #  设置公路线程组
    highwayThreads = []
    # 创建汽车新线程
    bmwCar = threading.Thread(target=drive, args=('BMWCar',))
    vmCar = threading.Thread(target=drive, args=('VMCar',))

    #  将汽车线程添加到公路线程组
    highwayThreads.append(bmwCar)
    highwayThreads.append(vmCar)

    # 汽车启动
    for thread in highwayThreads:
        thread.start()
    
    # 红绿灯发送事件通知
    sign()