# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QStatusBar, QTabWidget,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(990, 800)
        self.actionNew_Dial = QAction(MainWindow)
        self.actionNew_Dial.setObjectName(u"actionNew_Dial")
        self.actionOpen_Folder = QAction(MainWindow)
        self.actionOpen_Folder.setObjectName(u"actionOpen_Folder")
        self.actionSave_iwf_json = QAction(MainWindow)
        self.actionSave_iwf_json.setObjectName(u"actionSave_iwf_json")
        self.actionSave_font_json = QAction(MainWindow)
        self.actionSave_font_json.setObjectName(u"actionSave_font_json")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionValidate_iwf_json = QAction(MainWindow)
        self.actionValidate_iwf_json.setObjectName(u"actionValidate_iwf_json")
        self.actionValidate_font_json = QAction(MainWindow)
        self.actionValidate_font_json.setObjectName(u"actionValidate_font_json")
        self.actionValidate_structure = QAction(MainWindow)
        self.actionValidate_structure.setObjectName(u"actionValidate_structure")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionExport_Preview = QAction(MainWindow)
        self.actionExport_Preview.setObjectName(u"actionExport_Preview")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_8 = QVBoxLayout(self.tab)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButtonAddFile = QPushButton(self.groupBox_3)
        self.pushButtonAddFile.setObjectName(u"pushButtonAddFile")

        self.horizontalLayout_2.addWidget(self.pushButtonAddFile)

        self.pushButtonRemoveFile = QPushButton(self.groupBox_3)
        self.pushButtonRemoveFile.setObjectName(u"pushButtonRemoveFile")

        self.horizontalLayout_2.addWidget(self.pushButtonRemoveFile)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.listWidget = QListWidget(self.groupBox_3)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_5.addWidget(self.listWidget)

        self.frame = QFrame(self.groupBox_3)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 200))
        self.frame.setMaximumSize(QSize(16777215, 200))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_2)


        self.verticalLayout_5.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.groupBox_3)

        self.widget = QWidget(self.tab)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_7 = QVBoxLayout(self.widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox_4 = QGroupBox(self.widget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_3)

        self.groupBox_5 = QGroupBox(self.groupBox_4)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.graphicsView_2 = QGraphicsView(self.groupBox_5)
        self.graphicsView_2.setObjectName(u"graphicsView_2")
        self.graphicsView_2.setMaximumSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.graphicsView_2)

        self.pushButtonLoadResHour = QPushButton(self.groupBox_5)
        self.pushButtonLoadResHour.setObjectName(u"pushButtonLoadResHour")
        self.pushButtonLoadResHour.setMinimumSize(QSize(0, 32))
        self.pushButtonLoadResHour.setMaximumSize(QSize(16777215, 32))

        self.horizontalLayout_3.addWidget(self.pushButtonLoadResHour)

        self.pushButtonClearResHour = QPushButton(self.groupBox_5)
        self.pushButtonClearResHour.setObjectName(u"pushButtonClearResHour")
        self.pushButtonClearResHour.setMinimumSize(QSize(0, 32))
        self.pushButtonClearResHour.setMaximumSize(QSize(16777215, 32))

        self.horizontalLayout_3.addWidget(self.pushButtonClearResHour)


        self.verticalLayout_10.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.groupBox_5)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.spinBoxHourCenterX = QSpinBox(self.groupBox_5)
        self.spinBoxHourCenterX.setObjectName(u"spinBoxHourCenterX")
        self.spinBoxHourCenterX.setMaximum(999)

        self.horizontalLayout_4.addWidget(self.spinBoxHourCenterX)

        self.label_5 = QLabel(self.groupBox_5)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.spinBoxHourCenterY = QSpinBox(self.groupBox_5)
        self.spinBoxHourCenterY.setObjectName(u"spinBoxHourCenterY")
        self.spinBoxHourCenterY.setMaximum(999)

        self.horizontalLayout_4.addWidget(self.spinBoxHourCenterY)


        self.verticalLayout_10.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.groupBox_5)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.spinBoxHourAnchorX = QSpinBox(self.groupBox_5)
        self.spinBoxHourAnchorX.setObjectName(u"spinBoxHourAnchorX")
        self.spinBoxHourAnchorX.setMaximum(999)

        self.horizontalLayout_5.addWidget(self.spinBoxHourAnchorX)

        self.label_7 = QLabel(self.groupBox_5)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.spinBoxHourAnchorY = QSpinBox(self.groupBox_5)
        self.spinBoxHourAnchorY.setObjectName(u"spinBoxHourAnchorY")
        self.spinBoxHourAnchorY.setMaximum(999)

        self.horizontalLayout_5.addWidget(self.spinBoxHourAnchorY)


        self.verticalLayout_10.addLayout(self.horizontalLayout_5)


        self.verticalLayout_9.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.groupBox_4)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.graphicsView_4 = QGraphicsView(self.groupBox_6)
        self.graphicsView_4.setObjectName(u"graphicsView_4")
        self.graphicsView_4.setMaximumSize(QSize(32, 32))

        self.horizontalLayout_9.addWidget(self.graphicsView_4)

        self.pushButtonLoadResMin = QPushButton(self.groupBox_6)
        self.pushButtonLoadResMin.setObjectName(u"pushButtonLoadResMin")
        self.pushButtonLoadResMin.setMinimumSize(QSize(0, 32))
        self.pushButtonLoadResMin.setMaximumSize(QSize(16777215, 32))

        self.horizontalLayout_9.addWidget(self.pushButtonLoadResMin)

        self.pushButtonClearResMin = QPushButton(self.groupBox_6)
        self.pushButtonClearResMin.setObjectName(u"pushButtonClearResMin")
        self.pushButtonClearResMin.setMinimumSize(QSize(0, 32))
        self.pushButtonClearResMin.setMaximumSize(QSize(16777215, 32))

        self.horizontalLayout_9.addWidget(self.pushButtonClearResMin)


        self.verticalLayout_11.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_12 = QLabel(self.groupBox_6)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_10.addWidget(self.label_12)

        self.spinBoxMinCenterX = QSpinBox(self.groupBox_6)
        self.spinBoxMinCenterX.setObjectName(u"spinBoxMinCenterX")
        self.spinBoxMinCenterX.setMaximum(999)

        self.horizontalLayout_10.addWidget(self.spinBoxMinCenterX)

        self.label_13 = QLabel(self.groupBox_6)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_10.addWidget(self.label_13)

        self.spinBoxMinCenterY = QSpinBox(self.groupBox_6)
        self.spinBoxMinCenterY.setObjectName(u"spinBoxMinCenterY")
        self.spinBoxMinCenterY.setMaximum(999)

        self.horizontalLayout_10.addWidget(self.spinBoxMinCenterY)


        self.verticalLayout_11.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_14 = QLabel(self.groupBox_6)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_11.addWidget(self.label_14)

        self.spinBoxMinAnchorX = QSpinBox(self.groupBox_6)
        self.spinBoxMinAnchorX.setObjectName(u"spinBoxMinAnchorX")
        self.spinBoxMinAnchorX.setMaximum(999)

        self.horizontalLayout_11.addWidget(self.spinBoxMinAnchorX)

        self.label_15 = QLabel(self.groupBox_6)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_11.addWidget(self.label_15)

        self.spinBoxMinAnchorY = QSpinBox(self.groupBox_6)
        self.spinBoxMinAnchorY.setObjectName(u"spinBoxMinAnchorY")
        self.spinBoxMinAnchorY.setMaximum(999)

        self.horizontalLayout_11.addWidget(self.spinBoxMinAnchorY)


        self.verticalLayout_11.addLayout(self.horizontalLayout_11)


        self.verticalLayout_9.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.groupBox_4)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.graphicsView_5 = QGraphicsView(self.groupBox_7)
        self.graphicsView_5.setObjectName(u"graphicsView_5")
        self.graphicsView_5.setMaximumSize(QSize(32, 32))

        self.horizontalLayout_12.addWidget(self.graphicsView_5)

        self.pushButtonLoadResSec = QPushButton(self.groupBox_7)
        self.pushButtonLoadResSec.setObjectName(u"pushButtonLoadResSec")
        self.pushButtonLoadResSec.setMinimumSize(QSize(0, 32))
        self.pushButtonLoadResSec.setMaximumSize(QSize(16777215, 32))

        self.horizontalLayout_12.addWidget(self.pushButtonLoadResSec)

        self.pushButtonClearResSec = QPushButton(self.groupBox_7)
        self.pushButtonClearResSec.setObjectName(u"pushButtonClearResSec")
        self.pushButtonClearResSec.setMinimumSize(QSize(0, 32))
        self.pushButtonClearResSec.setMaximumSize(QSize(16777215, 32))

        self.horizontalLayout_12.addWidget(self.pushButtonClearResSec)


        self.verticalLayout_12.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_16 = QLabel(self.groupBox_7)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_13.addWidget(self.label_16)

        self.spinBoxSecCenterX = QSpinBox(self.groupBox_7)
        self.spinBoxSecCenterX.setObjectName(u"spinBoxSecCenterX")
        self.spinBoxSecCenterX.setMaximum(999)

        self.horizontalLayout_13.addWidget(self.spinBoxSecCenterX)

        self.label_17 = QLabel(self.groupBox_7)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_13.addWidget(self.label_17)

        self.spinBoxSecCenterY = QSpinBox(self.groupBox_7)
        self.spinBoxSecCenterY.setObjectName(u"spinBoxSecCenterY")
        self.spinBoxSecCenterY.setMaximum(999)

        self.horizontalLayout_13.addWidget(self.spinBoxSecCenterY)


        self.verticalLayout_12.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_18 = QLabel(self.groupBox_7)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_14.addWidget(self.label_18)

        self.spinBoxSecAnchorX = QSpinBox(self.groupBox_7)
        self.spinBoxSecAnchorX.setObjectName(u"spinBoxSecAnchorX")
        self.spinBoxSecAnchorX.setMaximum(999)

        self.horizontalLayout_14.addWidget(self.spinBoxSecAnchorX)

        self.label_19 = QLabel(self.groupBox_7)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_14.addWidget(self.label_19)

        self.spinBoxSecAnchorY = QSpinBox(self.groupBox_7)
        self.spinBoxSecAnchorY.setObjectName(u"spinBoxSecAnchorY")
        self.spinBoxSecAnchorY.setMaximum(999)

        self.horizontalLayout_14.addWidget(self.spinBoxSecAnchorY)


        self.verticalLayout_12.addLayout(self.horizontalLayout_14)


        self.verticalLayout_9.addWidget(self.groupBox_7)

        self.groupBox_8 = QGroupBox(self.groupBox_4)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.pushButtonResetRotations = QPushButton(self.groupBox_8)
        self.pushButtonResetRotations.setObjectName(u"pushButtonResetRotations")

        self.verticalLayout_13.addWidget(self.pushButtonResetRotations)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_20 = QLabel(self.groupBox_8)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_15.addWidget(self.label_20)

        self.horizontalSliderHourRotation = QSlider(self.groupBox_8)
        self.horizontalSliderHourRotation.setObjectName(u"horizontalSliderHourRotation")
        self.horizontalSliderHourRotation.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_15.addWidget(self.horizontalSliderHourRotation)


        self.verticalLayout_13.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_21 = QLabel(self.groupBox_8)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_16.addWidget(self.label_21)

        self.horizontalSliderMinRotation = QSlider(self.groupBox_8)
        self.horizontalSliderMinRotation.setObjectName(u"horizontalSliderMinRotation")
        self.horizontalSliderMinRotation.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_16.addWidget(self.horizontalSliderMinRotation)


        self.verticalLayout_13.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_22 = QLabel(self.groupBox_8)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_17.addWidget(self.label_22)

        self.horizontalSliderSecRotation = QSlider(self.groupBox_8)
        self.horizontalSliderSecRotation.setObjectName(u"horizontalSliderSecRotation")
        self.horizontalSliderSecRotation.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_17.addWidget(self.horizontalSliderSecRotation)


        self.verticalLayout_13.addLayout(self.horizontalLayout_17)


        self.verticalLayout_9.addWidget(self.groupBox_8)


        self.verticalLayout_7.addWidget(self.groupBox_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.widget)


        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.tab, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.verticalLayout_14 = QVBoxLayout(self.tab_8)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_23 = QLabel(self.tab_8)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_23)

        self.tabWidget.addTab(self.tab_8, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_15 = QVBoxLayout(self.tab_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.pushButtonExpandAll = QPushButton(self.tab_2)
        self.pushButtonExpandAll.setObjectName(u"pushButtonExpandAll")

        self.horizontalLayout_18.addWidget(self.pushButtonExpandAll)

        self.pushButtonCollapseAll = QPushButton(self.tab_2)
        self.pushButtonCollapseAll.setObjectName(u"pushButtonCollapseAll")

        self.horizontalLayout_18.addWidget(self.pushButtonCollapseAll)

        self.pushButtonRawIwfJson = QPushButton(self.tab_2)
        self.pushButtonRawIwfJson.setObjectName(u"pushButtonRawIwfJson")

        self.horizontalLayout_18.addWidget(self.pushButtonRawIwfJson)


        self.verticalLayout_15.addLayout(self.horizontalLayout_18)

        self.treeWidget = QTreeWidget(self.tab_2)
        self.treeWidget.setObjectName(u"treeWidget")

        self.verticalLayout_15.addWidget(self.treeWidget)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_16 = QVBoxLayout(self.tab_3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_8 = QLabel(self.tab_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_8)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_17 = QVBoxLayout(self.tab_5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_9 = QLabel(self.tab_5)
        self.label_9.setObjectName(u"label_9")
        font = QFont()
        font.setPointSize(18)
        self.label_9.setFont(font)

        self.verticalLayout_17.addWidget(self.label_9)

        self.groupBox_9 = QGroupBox(self.tab_5)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.verticalLayout_18 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_10 = QLabel(self.groupBox_9)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_18.addWidget(self.label_10)

        self.label_11 = QLabel(self.groupBox_9)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_11)

        self.pushButtonExportIwf = QPushButton(self.groupBox_9)
        self.pushButtonExportIwf.setObjectName(u"pushButtonExportIwf")

        self.verticalLayout_18.addWidget(self.pushButtonExportIwf)


        self.verticalLayout_17.addWidget(self.groupBox_9)

        self.groupBox_10 = QGroupBox(self.tab_5)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.verticalLayout_19 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_24 = QLabel(self.groupBox_10)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_19.addWidget(self.label_24)

        self.pushButtonExportIwfLz = QPushButton(self.groupBox_10)
        self.pushButtonExportIwfLz.setObjectName(u"pushButtonExportIwfLz")

        self.verticalLayout_19.addWidget(self.pushButtonExportIwfLz)


        self.verticalLayout_17.addWidget(self.groupBox_10)

        self.groupBox_11 = QGroupBox(self.tab_5)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.verticalLayout_20 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_25 = QLabel(self.groupBox_11)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_20.addWidget(self.label_25)

        self.pushButtonExportEntireDial = QPushButton(self.groupBox_11)
        self.pushButtonExportEntireDial.setObjectName(u"pushButtonExportEntireDial")

        self.verticalLayout_20.addWidget(self.pushButtonExportEntireDial)


        self.verticalLayout_17.addWidget(self.groupBox_11)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_3)

        self.tabWidget.addTab(self.tab_5, "")

        self.verticalLayout_4.addWidget(self.tabWidget)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(260, 325))
        self.groupBox.setMaximumSize(QSize(260, 325))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.graphicsView = QGraphicsView(self.groupBox)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setMinimumSize(QSize(240, 284))
        self.graphicsView.setMaximumSize(QSize(240, 284))

        self.verticalLayout_2.addWidget(self.graphicsView)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(260, 115))
        self.groupBox_2.setMaximumSize(QSize(260, 115))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.pushButtonUploadBkg = QPushButton(self.groupBox_2)
        self.pushButtonUploadBkg.setObjectName(u"pushButtonUploadBkg")

        self.verticalLayout_3.addWidget(self.pushButtonUploadBkg)

        self.pushButtonClearBkg = QPushButton(self.groupBox_2)
        self.pushButtonClearBkg.setObjectName(u"pushButtonClearBkg")

        self.verticalLayout_3.addWidget(self.pushButtonClearBkg)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 990, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNew_Dial)
        self.menuFile.addAction(self.actionOpen_Folder)
        self.menuFile.addAction(self.actionSave_iwf_json)
        self.menuFile.addAction(self.actionSave_font_json)
        self.menuFile.addAction(self.actionExport_Preview)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuTools.addAction(self.actionValidate_iwf_json)
        self.menuTools.addAction(self.actionValidate_font_json)
        self.menuTools.addAction(self.actionValidate_structure)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Dial Creator", None))
        self.actionNew_Dial.setText(QCoreApplication.translate("MainWindow", u"New Dial", None))
        self.actionOpen_Folder.setText(QCoreApplication.translate("MainWindow", u"Open Folder", None))
        self.actionSave_iwf_json.setText(QCoreApplication.translate("MainWindow", u"Save iwf.json", None))
        self.actionSave_font_json.setText(QCoreApplication.translate("MainWindow", u"Save font.json", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionValidate_iwf_json.setText(QCoreApplication.translate("MainWindow", u"Validate iwf.json", None))
        self.actionValidate_font_json.setText(QCoreApplication.translate("MainWindow", u"Validate font.json", None))
        self.actionValidate_structure.setText(QCoreApplication.translate("MainWindow", u"Validate structure", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionExport_Preview.setText(QCoreApplication.translate("MainWindow", u"Export Preview", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Resource Viewer", None))
        self.pushButtonAddFile.setText(QCoreApplication.translate("MainWindow", u"Add File", None))
        self.pushButtonRemoveFile.setText(QCoreApplication.translate("MainWindow", u"Remove File", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Select resource to preview", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Watch Widget", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Notice: Centers are auto-centered to prevent complex editing.", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Hour", None))
        self.pushButtonLoadResHour.setText(QCoreApplication.translate("MainWindow", u"Load from resources", None))
        self.pushButtonClearResHour.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"CenterX:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"CenterY:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"AnchorX:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"AnchorY:", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Minute", None))
        self.pushButtonLoadResMin.setText(QCoreApplication.translate("MainWindow", u"Load from resources", None))
        self.pushButtonClearResMin.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"CenterX:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"CenterY:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"AnchorX:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"AnchorY:", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Second", None))
        self.pushButtonLoadResSec.setText(QCoreApplication.translate("MainWindow", u"Load from resources", None))
        self.pushButtonClearResSec.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"CenterX:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"CenterY:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"AnchorX:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"AnchorY:", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Custom Rotation", None))
        self.pushButtonResetRotations.setText(QCoreApplication.translate("MainWindow", u"Reset to 12:00:00", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Hour (Angle: 0)", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Minute (Angle: 0)", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Second (Angle: 0)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Hands and Rotation", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Coming Soon", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"Widget Editor", None))
        self.pushButtonExpandAll.setText(QCoreApplication.translate("MainWindow", u"Expand All", None))
        self.pushButtonCollapseAll.setText(QCoreApplication.translate("MainWindow", u"Collapse All", None))
        self.pushButtonRawIwfJson.setText(QCoreApplication.translate("MainWindow", u"Raw iwf.json", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Value", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Property", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"iwf.json Editor", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Coming Soon", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"font.json Editor", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Export Options", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u".iwf (IDO Watch Face)", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Export the watch face into a binary format. Used in the VeryFit watch face market.", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-style:italic;\">Notice: To sideload modified dials, you'll need to replace the files on iOS or download VeryFit-3-3-1-Local-Dial.apk on Android.</span></p></body></html>", None))
        self.pushButtonExportIwf.setText(QCoreApplication.translate("MainWindow", u"Export .iwf", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u".iwf.lz (IDO Watch Face with LZ compression)", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Export the watch face into a binary format with LZ compression. Used for devices with smaller memory.", None))
        self.pushButtonExportIwfLz.setText(QCoreApplication.translate("MainWindow", u"Export .iwf.lz", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Entire Dial", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Export the watch face onto a folder. Exports all files and resources.", None))
        self.pushButtonExportEntireDial.setText(QCoreApplication.translate("MainWindow", u"Export Entire Dial", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Export", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Preview", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Background", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"No background uploaded", None))
        self.pushButtonUploadBkg.setText(QCoreApplication.translate("MainWindow", u"Upload Background", None))
        self.pushButtonClearBkg.setText(QCoreApplication.translate("MainWindow", u"Clear Background", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

