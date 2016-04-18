from matplotlib.pylab import table, show


def showMatr(matrix):
    table(cellText=matrix,
          loc='center',
          cellLoc='center',
          bbox=[0.2, 0.2, 0.5, 0.5])
    show()
