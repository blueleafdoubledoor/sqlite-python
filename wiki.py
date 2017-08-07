# -*- coding: utf-8 -*-
import os
import SimpleHTTPServer

def test():
    post_file_list = os.listdir("{0}/Post/".format(os.path.dirname(os.path.abspath(__file__))))
    for name in post_file_list:
        file_name, ext = os.path.splitext(os.path.basename(name))
        if ext == ".html":
            print("=============")
            print(name)
            print(file_name)
            print(ext)
            print("=============")

if __name__ == "__main__":
    test()

