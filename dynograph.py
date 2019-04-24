import matplotlib.pyplot as plt


class LineGraph:
    def __init__(self):
        self.xvalues = []    #speed
        self.yvalues = []    #power
        self.tvalues = []    #torque
        
    def addx(self, x):
        self.xvalues = x
        
    def addy(self, y):
        self.yvalues = y
        
    def addt(self, t):
        self.tvalues = t
    
    
    # where f is the figure/graph you want to display
    def display_graph(self):
        fig, ax1 = plt.subplots()
        ax1.plot(self.xvalues, self.yvalues, 'b-')
        ax1.set_xlabel('Speed (rpm)')
        ax1.set_ylabel('Power (hp)', color='b')
        
        ax2=ax1.twinx()
        ax2.plot(self.xvalues, self.tvalues, 'xr-')
        ax2.set_ylabel('Torque (ft-lbs/min)', color='r')
        
        fig.tight_layout()
        
        plt.show()
        

"""
if __name__ == "__main__":

    plt.plot([1,2,3,4], [5,10,15,20], 'b-')
    plt.ylabel('Speed (mph)')
    plt.xlabel('Time (ms)')
    plt.show()
"""