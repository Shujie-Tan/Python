import traceback
import sys
import logging

gList = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

logging.basicConfig(
    level=logging.DEBUG,
    filename="log.txt",
    filemode='w',
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
)


def f():
    gList[5]
    logging.info('calling method g() in f()')
    return g()


def g():
    logging.info('calling method h() in g()')
    return h()


def h():
    logging.info('Delete element in gList in h()')
    del gList[2]
    logging.info('Append element i to gList in i()')
    gList.append(i())
    print(gList[7])


def i():
    logging.info('Append element i to gList in i()')
    gList.append('i')
    print(gList[7])


if __name__ == "__main__":
    logging.debug('Information during calling f():')
    console = logging.StreamHandler()
    console.setLevel(logging.ERROR)  # 可以在控制台输出错误信息
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)
    try:
        f()
    except IndexError as ex:
        print("Sorry, Exception occured, out of range")
        traceback.print_exc()
        ty, tv, tb = sys.exc_info()
        logging.error("[ERROR]:Sorry, Exception occured, out of range")
        logging.critical("object info:%s" % ex)
        logging.critical("Error Type:{0}, Error information:{1}".format(
            ty, tv, tb))
        logging.critical("".join(traceback.format_tb(tb)))
        sys.exit(1)
