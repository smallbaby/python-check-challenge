#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 来源 http://www.oschina.net/code/snippet_219811_14920

import sys
import os.path
from PyQt4 import QtGui, QtCore, QtWebKit


class PageShotter(QtGui.QWidget):
    def __init__(self, url, filename, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.url = url
        self.filename = filename
        self.webpage = None

    def shot(self):
        webview = QtWebKit.QWebView(self)
        webview.load(QtCore.QUrl(self.url))
        self.webpage = webview.page()
        self.connect(webview, QtCore.SIGNAL("loadFinished(bool)"), self.save_page)

    def save_page(self, finished):
        # print finished
        if finished:
            size = self.webpage.mainFrame().contentsSize()
            self.webpage.setViewportSize(QtCore.QSize(size.width() + 16, size.height()))
            img = QtGui.QImage(size, QtGui.QImage.Format_ARGB32)
            painter = QtGui.QPainter(img)
            self.webpage.mainFrame().render(painter)
            painter.end()
            filename = self.filename;
            if img.save(filename):
                filepath = os.path.join(os.path.dirname(__file__), filename)
            else:
                pass
        else:
            self.close()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    shotter = PageShotter("http://www.youku.com/", 'shot.png')
    shotter.shot()
    sys.exit(app.exec_())