import sys
import random
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        screen = app.primaryScreen()

        self.setGeometry(50, 50, screen.size().width(), screen.size().height())
        self.setWindowTitle("Algorithm Suite")
        self.setWindowIcon(QIcon("Python\Projekte\AlgorithmSuite\Icons\MainIcon.png"))

        HomeAction = QAction(QIcon("Python\Projekte\AlgorithmSuite\Icons\HomeIcon.png"), "Home", self)
        HomeAction.triggered.connect(self.HomeWidget)

        SortAction = QAction(QIcon("Python\Projekte\AlgorithmSuite\Icons\SortIcon.png"), "Sorting Algorithms", self)
        SortAction.triggered.connect(self.SortingWidget)

        GraphAction = QAction(QIcon("Python\Projekte\AlgorithmSuite\Icons\GraphIcon.png"), "Graph Algorithms", self)
        GraphAction.triggered.connect(self.close)

        AIAction = QAction(QIcon("Python\Projekte\AlgorithmSuite\Icons\AI-Icon.png"), "Machine Learning Algorithms", self)
        AIAction.triggered.connect(self.close)

        toolBar = self.addToolBar("Toolbar")
        toolBar.setIconSize(QSize(64, 64))
        toolBar.setMovable(False)
        toolBar.addAction(HomeAction)

        toolBar.addSeparator()
        
        toolBar.addAction(SortAction)
        toolBar.addAction(GraphAction)
        toolBar.addAction(AIAction)

        toolBar.addSeparator()

        self.options = QComboBox(self)
        self.options.currentTextChanged.connect(self.changewidget)
        self.options.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)
        toolBar.addWidget(self.options)

        widget = Home()
        self.setCentralWidget(widget)

        self.currentcategory = "Home"

        self.showMaximized()

    def changewidget(self):
        sortmap = ["Selection Sort", "Bubble Sort", "Merge Sort"]
        if self.currentcategory == "Sorting":
            if self.options.currentText() == "Introduction":
                widget = SortingIntroduction()
                self.setCentralWidget(widget)
            else:
                for name in sortmap:
                    if self.options.currentText() == name:
                        widget = Sorting(name)
                        self.setCentralWidget(widget)
                        break

    def HomeWidget(self):
        self.options.clear()
        self.currentcategory = "Home"
        widget = Home()
        self.setCentralWidget(widget)

    def SortingWidget(self):
        self.options.clear()
        self.options.addItems(["Introduction", "Selection Sort", "Bubble Sort", "Merge Sort"])
        self.currentcategory = "Sorting"
        widget = SortingIntroduction()
        self.setCentralWidget(widget)

class SortingMerge(QWidget):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        self.v3 = QVBoxLayout()
        self.v3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.v3)

        self.title3 = QLabel("Information", self)
        self.title3.setStyleSheet("QWidget {font-weight: bold; font-size: 20px}")
        self.title3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.v3.addWidget(self.title3)

        self.h1 = QLabel("How does Merge Sort work?", self)
        self.h1.setStyleSheet("QWidget {font-weight: bold; font-size: 15px}")
        self.h1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.v3.addWidget(self.h1)

        self.t1 = QLabel("Merge Sort uses the principle of \"Divide and Conquer\".\nIt divides the list into two sub-lists that get divided again until only one element is left.\nAt the end, the algorithm merges the many sub-lists together by comparison.", self)
        self.t1.setStyleSheet("QWidget {font-size: 15px}")
        self.v3.addWidget(self.t1)

        self.h2 = QLabel("\nWhat's its complexity?", self)
        self.h2.setStyleSheet("QWidget {font-weight: bold; font-size: 15px}")
        self.h2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.v3.addWidget(self.h2)

        self.t2 = QLabel("Due to its recursive nature, the algorithm has a complexity of O(n log(n)).", self)
        self.t2.setStyleSheet("QWidget {font-size: 15px}")
        self.v3.addWidget(self.t2)

        self.v3.addStretch(0)

        self.handles = [mpatches.Patch(color="yellow", label="Sub-List")]

class SortingSelection(QWidget):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        self.v3 = QVBoxLayout()
        self.v3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.v3)

        self.title3 = QLabel("Information", self)
        self.title3.setStyleSheet("QWidget {font-weight: bold; font-size: 20px}")
        self.title3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.v3.addWidget(self.title3)

        self.h1 = QLabel("How does Selection Sort work?", self)
        self.h1.setStyleSheet("QWidget {font-weight: bold; font-size: 15px}")
        self.h1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.v3.addWidget(self.h1)

        self.t1 = QLabel("For every element k, it looks at every other element n in the list to decide whether or not the current element k is the smallest.\nIf there is a smaller element n found, it will be swapped with k.", self)
        self.t1.setStyleSheet("QWidget {font-size: 15px}")
        self.v3.addWidget(self.t1)

        self.h2 = QLabel("\nWhat's its complexity?", self)
        self.h2.setStyleSheet("QWidget {font-weight: bold; font-size: 15px}")
        self.h2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.v3.addWidget(self.h2)

        self.t2 = QLabel("Selection Sort utilizes two nested loops iterating over the whole list, resulting in a complexity of O(n²).", self)
        self.t2.setStyleSheet("QWidget {font-size: 15px}")
        self.v3.addWidget(self.t2)

        self.v3.addStretch(0)

        self.handles = [mpatches.Patch(color="red", label="Current element"), mpatches.Patch(color="yellow", label="Smaller element")]

class SortingBubble(QWidget):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        self.v3 = QVBoxLayout()
        self.v3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.v3)

        self.title3 = QLabel("Information", self)
        self.title3.setStyleSheet("QWidget {font-weight: bold; font-size: 20px}")
        self.title3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.v3.addWidget(self.title3)

        self.h1 = QLabel("How does Bubble Sort work?", self)
        self.h1.setStyleSheet("QWidget {font-weight: bold; font-size: 15px}")
        self.h1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.v3.addWidget(self.h1)

        self.t1 = QLabel("The algorithm compares two values and sorts them, then continues with the next pair and so on. It repeats this until the list is sorted.", self)
        self.t1.setStyleSheet("QWidget {font-size: 15px}")
        self.v3.addWidget(self.t1)

        self.h2 = QLabel("\nWhat's its complexity?", self)
        self.h2.setStyleSheet("QWidget {font-weight: bold; font-size: 15px}")
        self.h2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.v3.addWidget(self.h2)

        self.t2 = QLabel("Bubble Sort utilizes two nested loops iterating over the whole list, resulting in a complexity of O(n²).", self)
        self.t2.setStyleSheet("QWidget {font-size: 15px}")
        self.v3.addWidget(self.t2)

        self.v3.addStretch(0)

        self.handles = [mpatches.Patch(color="yellow", label="Compared elements")]

class Sorting(QWidget):
    def __init__(self, algorithm):
        super().__init__()
        self.initMe(algorithm)

    def initMe(self, algorithm):
        self.speed = 1
        self.queue = []
        self.prev = [-1, -1, -1, -1]
        self.algorithm = algorithm
        self.time = 0

        self.v = QVBoxLayout()
        self.setLayout(self.v)

        self.h = QHBoxLayout()
        self.v.addLayout(self.h)

        self.v2 = QVBoxLayout()
        self.h.addLayout(self.v2)

        self.h.addStretch(0)

        if self.algorithm == "Selection Sort":
            self.title = QLabel("Selection Sort", self)
            widget = SortingSelection()
        elif self.algorithm == "Bubble Sort":
            self.title = QLabel("Bubble Sort", self)
            widget = SortingBubble()
        elif self.algorithm == "Merge Sort":
            self.title = QLabel("Merge Sort", self)
            widget = SortingMerge()

        self.title.setStyleSheet("QWidget {font-weight: bold; font-size: 20px}")
        self.v2.addWidget(self.title)

        self.h.addWidget(widget)
        self.h.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.h.addStretch(0)

        title2 = QLabel("Settings", self)
        title2.setStyleSheet("QWidget {font-size: 15px; font-weight: bold}")
        self.v2.addWidget(title2)

        label = QLabel("Amount of items:", self)
        label.setStyleSheet("QWidget {font-size: 15px}")
        self.v2.addWidget(label)

        self.amount = QSpinBox(self)
        self.amount.setFixedWidth(50)
        self.v2.addWidget(self.amount)

        label2 = QLabel("Speed of simulation:", self)
        label2.setStyleSheet("QWidget {font-size: 15px}")
        self.v2.addWidget(label2)

        self.speedbtn = QComboBox(self)
        self.speedbtn.addItems(["1x", "2x", "3x", "4x"])
        self.speedbtn.setFixedWidth(40)
        self.v2.addWidget(self.speedbtn)

        self.genbtn = QPushButton("Generate list", self)
        self.genbtn.setFixedWidth(150)
        self.genbtn.clicked.connect(self.genlist)
        self.v2.addWidget(self.genbtn)

        self.sortbtn = QPushButton("Run algorithm", self)
        self.sortbtn.setFixedWidth(150)
        self.sortbtn.clicked.connect(self.sort)
        self.sortbtn.setEnabled(False)
        self.v2.addWidget(self.sortbtn)

        self.errorlabel = QLabel("", self)
        self.errorlabel.setFixedWidth(200)
        self.errorlabel.setStyleSheet("QWidget {font-weight: bold; color: red}")
        self.v2.addWidget(self.errorlabel)

        self.timelabel = QLabel(f"Timer: {0}s", self)
        self.timelabel.setStyleSheet("QWidget {font-weight: bold; color: blue; font-size: 20px}")
        self.v2.addWidget(self.timelabel)

        self.timer = QTimer()
        self.timer.timeout.connect(self.showtime)

        self.v2.addStretch(0)

        fig, self.ax = plt.subplots()
        self.figure = fig
        self.canvas = FigureCanvas(self.figure)      
        self.v.addWidget(self.canvas)

        self.figure.legend(handles=widget.handles)
        self.ax.set_title(self.algorithm)

        self.canvas.draw()

    def showtime(self):
        self.time += 1
        self.timelabel.setText(f"Timer: {self.time}s")

    def genlist(self):
        self.y = []
        self.timelabel.setText(f"Timer: {self.time}s")

        if self.amount.value() < 5:
            self.errorlabel.setText("ERROR: Please choose amount > 4")
        else:
            self.y = random.sample(range(1, 100), self.amount.value())
            self.colors = ["black" for _ in range(len(self.y))]

            self.ax.clear()
            self.createplot(list(range(len(self.y))), self.y)
            self.canvas.draw()

            if self.sortbtn.isEnabled() == False:
                self.sortbtn.setEnabled(True)
            self.errorlabel.setText("")

    def showcase(self):
        if self.queue[0][0] == "swap":
            swap(self.y, self.queue)
        elif self.queue[0][0] == "look":
            look(self.queue, self.colors, self.prev)
        elif self.queue[0][0] == "pick":
            pick(self.queue, self.colors, self.prev)
        elif self.queue[0][0] == "cmp":
            cmp(self.queue, self.colors, self.prev)
        elif self.queue[0][0] == "app":
            self.colors = append(self.y, self.queue, self.colors)
        del self.queue[0]
        if len(self.queue) != 0:
            QTimer.singleShot(self.speed, self.TimerHelper)
        else:
            self.colors = ["green" for _ in range(len(self.y))]
            self.timer.stop()
            self.time = 0
            self.sortbtn.setEnabled(True)
            self.genbtn.setEnabled(True)
            self.prev = [-1, -1, -1, -1]
        self.ax.clear()
        self.createplot(list(range(len(self.y))), self.y)
        self.canvas.draw()

    def sort(self):
        list = self.y.copy()
        self.genbtn.setEnabled(False)
        self.sortbtn.setEnabled(False)

        self.speed = int(self.speedbtn.currentText()[0])
        if self.speed == 1:
            self.speed = 250
        elif self.speed == 2:
            self.speed = 150
        elif self.speed == 3:
            self.speed = 50
        else:
            self.speed = 1

        if self.algorithm == "Selection Sort":
            selectionsort(self.queue, list)
        elif self.algorithm == "Bubble Sort":
            bubblesort(self.queue, list)
        elif self.algorithm == "Merge Sort":
            mergesort(self.queue, list)

        self.timer.start(1000)
        self.TimerHelper()

    def TimerHelper(self):
        QTimer.singleShot(self.speed, self.showcase)

    def createplot(self, x, l):
        self.ax.bar(x, l, width=0.8, color=self.colors)
        self.ax.set_ylabel("Value")
        self.ax.set_xlabel("Index")
        self.ax.set_title(f"{self.algorithm}")

def swap(y, queue):
    y[queue[0][1]], y[queue[0][2]] = y[queue[0][2]], y[queue[0][1]]

def look(queue, colors, prev):
    colors[prev[0]] = "black"
    colors[queue[0][1]] = "red"
    prev[0] = queue[0][1]

def pick(queue, colors, prev):
    colors[prev[1]] = "black"
    colors[queue[0][1]] = "yellow"
    prev[1] = queue[0][1]

def cmp(queue, colors, prev):
    colors[prev[2]] = "black"
    colors[prev[3]] = "black"
    colors[queue[0][1]] = "yellow"
    colors[queue[0][2]] = "yellow"
    prev[2] = queue[0][1]
    prev[3] = queue[0][2]

def append(y, queue, colors):
    x = y.index(queue[0][1][0])
    colors = ["black" for _ in range(len(y))]
    for i in range(len(queue[0][1])):
        del y[y.index(queue[0][2][i])]
        y.insert(x+i, queue[0][2][i])
        del colors[y.index(queue[0][2][i])]
        colors.insert(x+i, "yellow")
    return colors

def merge(l1, l2):
    i, j, k = 0, 0, 0
    result = []
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1
        k += 1
    result += l1[i:]
    result += l2[j:]
    print(l1, l2)
    return result

def mergesort(queue, l):
    if len(l) < 2:
        return l
    l1 = mergesort(queue, l[:len(l)//2])
    l2 = mergesort(queue, l[len(l)//2:])
    result = merge(l1, l2)
    queue.append(("app", l, result))
    return result

def bubblesort(queue, list):
    for _ in range(len(list)):
        swaps = False
        for j in range(len(list) - 1):
            queue.append(("cmp", j, j+1))
            if list[j] > list[j+1]:
                swaps = True
                queue.append(("swap", j, j+1))
                number = list[j]
                list[j] = list[j+1]
                list[j+1] = number
        if swaps == False:
            break

def selectionsort(queue, list):
    for i in range(len(list)):
        queue.append(("look", i))
        smallestindex = i                    
        for j in range(i, len(list)):
            if list[j] < list[smallestindex]:
                smallestindex = j
                queue.append(("pick", j))
        if smallestindex != i:
            number = list[i]
            list[i] = list[smallestindex]
            list[smallestindex] = number
            queue.append(("swap", i, smallestindex))

class SortingIntroduction(QWidget):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        v = QVBoxLayout()
        v.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(v)

        title = QLabel("Sorting Algorithms", self)
        title.setStyleSheet("QWidget {font-weight: bold; font-size: 25px}")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        v.addWidget(title)

        h1 = QLabel("\nWhat are sorting algorithms?", self)
        h1.setStyleSheet("QWidget {font-weight: bold; font-size: 20px}")
        v.addWidget(h1)

        t1 = QLabel("Sorting algorithms are algorithms used to put multiple items into their correct order, be it numerical or alphabetical.", self)
        t1.setStyleSheet("QWidget {font-size: 15px}")
        v.addWidget(t1)

        h2 = QLabel("\nWhat sorting algorithms are there?", self)
        h2.setStyleSheet("QWidget {font-weight: bold; font-size: 20px}")
        v.addWidget(h2)

        t2 = QLabel("There are a ton of sorting algorithms out there, also some nonsensical ones. The current algorithms we support are:", self)
        t2.setStyleSheet("QWidget {font-size: 15px}")
        v.addWidget(t2)

        v2 = QVBoxLayout()
        v2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        v.addLayout(v2)

        h3 = QLabel("\n• Selection Sort\n• Bubble Sort\n• Merge Sort", self)
        h3.setStyleSheet("QWidget {font-weight: bold; font-size: 20px}")
        v2.addWidget(h3)

        v.addStretch(0)

class Home(QWidget):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        v = QVBoxLayout()
        v.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(v)

        title = QLabel("Home", self)
        title.setStyleSheet("QWidget {font-weight: bold; font-size: 25px}")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        v.addWidget(title)

        h1 = QLabel("\nWhat is this program?", self)
        h1.setStyleSheet("QWidget {font-weight: bold; font-size: 20px}")
        v.addWidget(h1)

        t1 = QLabel("This program provides a showcase and explanation of the most famous and important algorithms in computer science.", self)
        t1.setStyleSheet("QWidget {font-size: 15px}")
        v.addWidget(t1)

        h2 = QLabel("\nWhat's the reason behind this?", self)
        h2.setStyleSheet("QWidget {font-weight: bold; font-size: 20px}")
        v.addWidget(h2)

        t2 = QLabel("Our goal is to make computer science education more accessible, visual and fun by providing a conclusive application\nto not only understand the underlying technology better, but to also see it in action.", self)
        t2.setStyleSheet("QWidget {font-size: 15px}")
        v.addWidget(t2)

        h3 = QLabel("\nHow is the application structured?", self)
        h3.setStyleSheet("QWidget {font-weight: bold; font-size: 20px}")
        v.addWidget(h3)

        t3 = QLabel("Using the toolbar, you can open different tabs representing categories of algorithms.\nYou will then have the opportunity to read about a variety of algorithms, aswell as to try them out yourself!", self)
        t3.setStyleSheet("QWidget {font-size: 15px}")
        v.addWidget(t3)

        h4 = QLabel("\nWhat categories are there?\n", self)
        h4.setStyleSheet("QWidget {font-weight: bold; font-size: 20px}")
        v.addWidget(h4)

        grid = QGridLayout()
        grid.setAlignment(Qt.AlignmentFlag.AlignCenter)
        v.addLayout(grid)

        icon1 = QLabel(self)
        icon1.setPixmap(QPixmap("Python\Projekte\AlgorithmSuite\Icons\SortIcon.png").scaled(75, 75))
        icon1.setFixedSize(75, 75)
        grid.addWidget(icon1, 0, 0)

        c1 = QLabel("Sorting algorithms", self)
        c1.setStyleSheet("QWidget {font-weight: bold; font-size: 20px}")
        grid.addWidget(c1, 0, 1)

        icon2 = QLabel(self)
        icon2.setPixmap(QPixmap("Python\Projekte\AlgorithmSuite\Icons\GraphIcon.png").scaled(75, 75))
        icon2.setFixedSize(75, 75)
        grid.addWidget(icon2, 1, 0)

        c2 = QLabel("Graph algorithms", self)
        c2.setStyleSheet("QWidget {font-weight: bold; font-size: 20px}")
        grid.addWidget(c2, 1, 1)

        icon3 = QLabel(self)
        icon3.setPixmap(QPixmap("Python\Projekte\AlgorithmSuite\Icons\AI-Icon.png").scaled(75, 75))
        icon3.setFixedSize(75, 75)
        grid.addWidget(icon3, 2, 0)

        c3 = QLabel("Machine learning algorithms", self)
        c3.setStyleSheet("QWidget {font-weight: bold; font-size: 20px}")
        grid.addWidget(c3, 2, 1)

        v.addStretch(0)

app = QApplication(sys.argv)
w = Main()

sys.exit(app.exec())