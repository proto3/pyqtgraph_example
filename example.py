#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, Qt
import pyqtgraph as pg
import sys, math

class MainWidget(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        plot = pg.PlotWidget()

        self.curve = pg.PlotCurveItem([], [], pen=pg.mkPen(color=(46, 134, 171), width=2))
        plot.addItem(self.curve)

        grid_alpha = 50
        grid_levels = [(100, 0), (20, 0), (1, 0)]
        x = plot.getAxis("bottom")
        y = plot.getAxis("left")
        x.setGrid(grid_alpha)
        y.setGrid(grid_alpha)
        x.setTickSpacing(levels=grid_levels)
        y.setTickSpacing(levels=grid_levels)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(plot)
        self.setLayout(layout)

    def draw(self, points):
        self.curve.setData(points[0], points[1])

if __name__ == '__main__':
    pg.setConfigOption('background', 'w')
    pg.setConfigOption('foreground', 'k')
    pg.setConfigOption('antialias', True)
    app = QtGui.QApplication([])

    main_widget = MainWidget()
    main_widget.show()

    points = [[],[]]
    for i in range(1000):
        points[0].append(i)
        points[1].append(math.sin(i/100))

    main_widget.draw(points)

    sys.exit(app.exec_())
