import time


class TrafficLight:

    def __init__(self):
        self.color = ["Red", "Yellow", "Green"]

    def running(self):
        for colors in self.color:
            print("The color is " + colors)
            if colors == "red":
                time.sleep(7)
            elif colors == "yellow":
                time.sleep(2)
            else:
                time.sleep(3)


TrafficLight().running()
