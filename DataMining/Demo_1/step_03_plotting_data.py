from pylab import plot, show
from step_02_data_analyzer import data,target


def show_plotting_image():
    # show the data in visual
    plot(data[target=='setosa',0],data[target=='setosa',2],'bo')
    plot(data[target=='versicolor',0],data[target=='versicolor',2],'ro')
    plot(data[target=='virginica',0],data[target=='virginica',2],'go')
    show()

if __name__ == '__main__':
    show_plotting_image()
