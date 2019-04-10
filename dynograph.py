import matplotlib.pyplot as plt


class LineGraph:
    def __init__(self):
        self.xvalues = []
        self.yvalues = []
        
    def addx(self, x):
        self.xvalues = x
        
    def addy(self, y):
        self.yvalues = y
        
    def display_graph(self):
        plt.plot(self.xvalues, self.yvalues, 'b-')
        plt.ylabel('Speed (mph)')
        plt.xlabel('Time (s)')
        plt.show()


"""
if __name__ == "__main__":

    plt.plot([1,2,3,4], [5,10,15,20], 'b-')
    plt.ylabel('Speed (mph)')
    plt.xlabel('Time (ms)')
    plt.show()
"""