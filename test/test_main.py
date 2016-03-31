from pyapi.main import make_tmp_path, main
import logging
import sys

log = logging.getLogger(__name__)
D = log.debug


def dev_make_tmp_path():
    """ tmp path making"""
    D(make_tmp_path(["os", "os.path", "sys"]))


def dev_help():
    main("-h")


def dev_html1():
    main("-d", "-b", "-p", "/tmp/out.html",
         "stuff.module1")

def dev_html2():
    main("-d", "-b", "-p", "/tmp/out.html",
         "stuff.module1", "stuff.package.module2")

def dev_html3():
    main("-d", "-b", "-p", "/tmp/out.html",
         "numbers")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    dev_html3()
