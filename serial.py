import sys
import glob


def serial_ports():
    """ Выводит список COM портов в Linux, Windows, MacOS

        :raise EnvironmentError('Версия ОС не определена!')

        :возвращает:
            Список COM портов и выводит их в терминал
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Версия ОС не определена!')

    result = []
    for port in ports:
        try:
            result.append(port)
        except (OSError):
            pass
    result.reverse()
    return result


if __name__ == '__main__':
    i = 1
    print("Список COM портов в системе:")

    for serPort in serial_ports():
        print("COM порт %s: %s" % (i, serPort))
        i += 1