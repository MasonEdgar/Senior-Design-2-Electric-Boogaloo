''' 
Author: Mason Edgar

University of Houston
Portable Medical Diagnosis Kit (PMDK)
Senior Capstone Fall 2017

Additonal Members: 
Nicholas Archibong 
Neamen Asfaha 
Ermias (Jeremy) Kebede

'''

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QLineEdit
import numpy as np
import pandas as pd
import Algorithm_1_Method as algo


ResponseVector = np.empty(shape=69, dtype=int, order='C')

np.set_printoptions(threshold=np.nan)

df = pd.read_excel('WeightedResponseVector.xlsx')
WeightVector = df.as_matrix()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(692, 578)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setHorizontalSpacing(2)
        self.gridLayout_2.setVerticalSpacing(1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 2, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 3, 0, 1, 1)
        self.ConfirmButton = QtWidgets.QPushButton(self.centralwidget)
        self.ConfirmButton.setStyleSheet("")
        self.ConfirmButton.setFlat(False)
        self.ConfirmButton.setObjectName("ConfirmButton")
        self.gridLayout_2.addWidget(self.ConfirmButton, 2, 1, 1, 1)
        self.ClearButton = QtWidgets.QPushButton(self.centralwidget)
        self.ClearButton.setObjectName("ClearButton")
        self.gridLayout_2.addWidget(self.ClearButton, 3, 1, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 670, 808))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.GeneralBody = QtWidgets.QWidget()
        self.GeneralBody.setObjectName("GeneralBody")
        self.ExtremeHunger = QtWidgets.QCheckBox(self.GeneralBody)
        self.ExtremeHunger.setGeometry(QtCore.QRect(20, 230, 201, 20))
        self.ExtremeHunger.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ExtremeHunger.setObjectName("ExtremeHunger")
        self.BodyAches = QtWidgets.QCheckBox(self.GeneralBody)
        self.BodyAches.setGeometry(QtCore.QRect(20, 150, 151, 20))
        self.BodyAches.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.BodyAches.setObjectName("BodyAches")
        self.ExtremeThirst = QtWidgets.QCheckBox(self.GeneralBody)
        self.ExtremeThirst.setGeometry(QtCore.QRect(20, 250, 231, 20))
        self.ExtremeThirst.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ExtremeThirst.setObjectName("ExtremeThirst")
        self.Vomiting = QtWidgets.QCheckBox(self.GeneralBody)
        self.Vomiting.setGeometry(QtCore.QRect(20, 90, 161, 20))
        self.Vomiting.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Vomiting.setObjectName("Vomiting")
        self.Fever = QtWidgets.QCheckBox(self.GeneralBody)
        self.Fever.setGeometry(QtCore.QRect(20, 30, 111, 20))
        self.Fever.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Fever.setObjectName("Fever")
        self.RaisedPinkRedBumps = QtWidgets.QCheckBox(self.GeneralBody)
        self.RaisedPinkRedBumps.setGeometry(QtCore.QRect(20, 330, 211, 20))
        self.RaisedPinkRedBumps.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.RaisedPinkRedBumps.setObjectName("RaisedPinkRedBumps")
        self.PeriodicPainFluctuatingIntensity = QtWidgets.QCheckBox(self.GeneralBody)
        self.PeriodicPainFluctuatingIntensity.setGeometry(QtCore.QRect(20, 390, 311, 20))
        self.PeriodicPainFluctuatingIntensity.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PeriodicPainFluctuatingIntensity.setObjectName("PeriodicPainFluctuatingIntensity")
        self.ThrobbingPulsatingPain = QtWidgets.QCheckBox(self.GeneralBody)
        self.ThrobbingPulsatingPain.setGeometry(QtCore.QRect(20, 350, 251, 20))
        self.ThrobbingPulsatingPain.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ThrobbingPulsatingPain.setObjectName("ThrobbingPulsatingPain")
        self.Irritation = QtWidgets.QCheckBox(self.GeneralBody)
        self.Irritation.setGeometry(QtCore.QRect(20, 130, 131, 20))
        self.Irritation.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Irritation.setObjectName("Irritation")
        self.AchingMuscles = QtWidgets.QCheckBox(self.GeneralBody)
        self.AchingMuscles.setGeometry(QtCore.QRect(20, 210, 211, 20))
        self.AchingMuscles.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.AchingMuscles.setObjectName("AchingMuscles")
        self.NumbnessTingling = QtWidgets.QCheckBox(self.GeneralBody)
        self.NumbnessTingling.setGeometry(QtCore.QRect(20, 310, 221, 20))
        self.NumbnessTingling.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.NumbnessTingling.setObjectName("NumbnessTingling")
        self.SmallFluidFilledBlisters = QtWidgets.QCheckBox(self.GeneralBody)
        self.SmallFluidFilledBlisters.setGeometry(QtCore.QRect(20, 370, 241, 20))
        self.SmallFluidFilledBlisters.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SmallFluidFilledBlisters.setObjectName("SmallFluidFilledBlisters")
        self.Fatigue = QtWidgets.QCheckBox(self.GeneralBody)
        self.Fatigue.setGeometry(QtCore.QRect(20, 70, 141, 20))
        self.Fatigue.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Fatigue.setObjectName("Fatigue")
        self.Weakness = QtWidgets.QCheckBox(self.GeneralBody)
        self.Weakness.setGeometry(QtCore.QRect(20, 110, 171, 20))
        self.Weakness.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Weakness.setObjectName("Weakness")
        self.PaleSkin = QtWidgets.QCheckBox(self.GeneralBody)
        self.PaleSkin.setGeometry(QtCore.QRect(20, 190, 161, 20))
        self.PaleSkin.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PaleSkin.setObjectName("PaleSkin")
        self.Chills = QtWidgets.QCheckBox(self.GeneralBody)
        self.Chills.setGeometry(QtCore.QRect(20, 50, 121, 20))
        self.Chills.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Chills.setObjectName("Chills")
        self.Rash = QtWidgets.QCheckBox(self.GeneralBody)
        self.Rash.setGeometry(QtCore.QRect(20, 10, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Rash.setFont(font)
        self.Rash.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Rash.setObjectName("Rash")
        self.NightSweats = QtWidgets.QCheckBox(self.GeneralBody)
        self.NightSweats.setGeometry(QtCore.QRect(20, 170, 191, 20))
        self.NightSweats.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.NightSweats.setObjectName("NightSweats")
        self.label_2 = QtWidgets.QLabel(self.GeneralBody)
        self.label_2.setGeometry(QtCore.QRect(300, 0, 291, 151))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("SD_Logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.LossOfEnergy = QtWidgets.QCheckBox(self.GeneralBody)
        self.LossOfEnergy.setGeometry(QtCore.QRect(20, 290, 181, 20))
        self.LossOfEnergy.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LossOfEnergy.setObjectName("LossOfEnergy")
        self.WeightLoss = QtWidgets.QCheckBox(self.GeneralBody)
        self.WeightLoss.setGeometry(QtCore.QRect(20, 270, 211, 20))
        self.WeightLoss.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.WeightLoss.setObjectName("WeightLoss")
        self.tabWidget.addTab(self.GeneralBody, "")
        self.Head = QtWidgets.QWidget()
        self.Head.setObjectName("Head")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Head)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Nausea = QtWidgets.QCheckBox(self.Head)
        self.Nausea.setObjectName("Nausea")
        self.gridLayout_3.addWidget(self.Nausea, 0, 0, 1, 1)
        self.SinusPressure = QtWidgets.QCheckBox(self.Head)
        self.SinusPressure.setObjectName("SinusPressure")
        self.gridLayout_3.addWidget(self.SinusPressure, 1, 0, 1, 1)
        self.Coughing = QtWidgets.QCheckBox(self.Head)
        self.Coughing.setObjectName("Coughing")
        self.gridLayout_3.addWidget(self.Coughing, 2, 0, 1, 1)
        self.Drooling = QtWidgets.QCheckBox(self.Head)
        self.Drooling.setObjectName("Drooling")
        self.gridLayout_3.addWidget(self.Drooling, 3, 0, 1, 1)
        self.Insomnia = QtWidgets.QCheckBox(self.Head)
        self.Insomnia.setObjectName("Insomnia")
        self.gridLayout_3.addWidget(self.Insomnia, 4, 0, 1, 1)
        self.UrgeToRubEyes = QtWidgets.QCheckBox(self.Head)
        self.UrgeToRubEyes.setObjectName("UrgeToRubEyes")
        self.gridLayout_3.addWidget(self.UrgeToRubEyes, 5, 0, 1, 1)
        self.BlurryVision = QtWidgets.QCheckBox(self.Head)
        self.BlurryVision.setObjectName("BlurryVision")
        self.gridLayout_3.addWidget(self.BlurryVision, 6, 0, 1, 1)
        self.SoundSensitivity = QtWidgets.QCheckBox(self.Head)
        self.SoundSensitivity.setObjectName("SoundSensitivity")
        self.gridLayout_3.addWidget(self.SoundSensitivity, 7, 0, 1, 1)
        self.Wheezing = QtWidgets.QCheckBox(self.Head)
        self.Wheezing.setObjectName("Wheezing")
        self.gridLayout_3.addWidget(self.Wheezing, 8, 0, 1, 1)
        self.ShortnessOfBreath = QtWidgets.QCheckBox(self.Head)
        self.ShortnessOfBreath.setObjectName("ShortnessOfBreath")
        self.gridLayout_3.addWidget(self.ShortnessOfBreath, 9, 0, 1, 1)
        self.BreathingPain = QtWidgets.QCheckBox(self.Head)
        self.BreathingPain.setObjectName("BreathingPain")
        self.gridLayout_3.addWidget(self.BreathingPain, 10, 0, 1, 1)
        self.VisionChanges = QtWidgets.QCheckBox(self.Head)
        self.VisionChanges.setObjectName("VisionChanges")
        self.gridLayout_3.addWidget(self.VisionChanges, 11, 0, 1, 1)
        self.CoughingBlood = QtWidgets.QCheckBox(self.Head)
        self.CoughingBlood.setObjectName("CoughingBlood")
        self.gridLayout_3.addWidget(self.CoughingBlood, 12, 0, 1, 1)
        self.DecreasedSenseOfTasteSmell = QtWidgets.QCheckBox(self.Head)
        self.DecreasedSenseOfTasteSmell.setObjectName("DecreasedSenseOfTasteSmell")
        self.gridLayout_3.addWidget(self.DecreasedSenseOfTasteSmell, 13, 0, 1, 1)
        self.DifficultyConcentrating = QtWidgets.QCheckBox(self.Head)
        self.DifficultyConcentrating.setObjectName("DifficultyConcentrating")
        self.gridLayout_3.addWidget(self.DifficultyConcentrating, 14, 0, 1, 1)
        self.NasalCongestion = QtWidgets.QCheckBox(self.Head)
        self.NasalCongestion.setObjectName("NasalCongestion")
        self.gridLayout_3.addWidget(self.NasalCongestion, 15, 0, 1, 1)
        self.IncreasedAsthmaticReactions = QtWidgets.QCheckBox(self.Head)
        self.IncreasedAsthmaticReactions.setObjectName("IncreasedAsthmaticReactions")
        self.gridLayout_3.addWidget(self.IncreasedAsthmaticReactions, 16, 0, 1, 1)
        self.FacialPain = QtWidgets.QCheckBox(self.Head)
        self.FacialPain.setObjectName("FacialPain")
        self.gridLayout_3.addWidget(self.FacialPain, 17, 0, 1, 1)
        self.LightSensitivity = QtWidgets.QCheckBox(self.Head)
        self.LightSensitivity.setObjectName("LightSensitivity")
        self.gridLayout_3.addWidget(self.LightSensitivity, 18, 0, 1, 1)
        self.PainOnOneSideOfHead = QtWidgets.QCheckBox(self.Head)
        self.PainOnOneSideOfHead.setObjectName("PainOnOneSideOfHead")
        self.gridLayout_3.addWidget(self.PainOnOneSideOfHead, 19, 0, 1, 1)
        self.Dizziness = QtWidgets.QCheckBox(self.Head)
        self.Dizziness.setObjectName("Dizziness")
        self.gridLayout_3.addWidget(self.Dizziness, 20, 0, 1, 1)
        self.IncreasedTears = QtWidgets.QCheckBox(self.Head)
        self.IncreasedTears.setObjectName("IncreasedTears")
        self.gridLayout_3.addWidget(self.IncreasedTears, 21, 0, 1, 1)
        self.ScratchyThroat = QtWidgets.QCheckBox(self.Head)
        self.ScratchyThroat.setObjectName("ScratchyThroat")
        self.gridLayout_3.addWidget(self.ScratchyThroat, 22, 0, 1, 1)
        self.BurningEyes = QtWidgets.QCheckBox(self.Head)
        self.BurningEyes.setObjectName("BurningEyes")
        self.gridLayout_3.addWidget(self.BurningEyes, 23, 0, 1, 1)
        self.SoreThroat = QtWidgets.QCheckBox(self.Head)
        self.SoreThroat.setObjectName("SoreThroat")
        self.gridLayout_3.addWidget(self.SoreThroat, 24, 0, 1, 1)
        self.BlockedNose = QtWidgets.QCheckBox(self.Head)
        self.BlockedNose.setObjectName("BlockedNose")
        self.gridLayout_3.addWidget(self.BlockedNose, 25, 0, 1, 1)
        self.ItchyEyes = QtWidgets.QCheckBox(self.Head)
        self.ItchyEyes.setObjectName("ItchyEyes")
        self.gridLayout_3.addWidget(self.ItchyEyes, 26, 0, 1, 1)
        self.NeckPain = QtWidgets.QCheckBox(self.Head)
        self.NeckPain.setObjectName("NeckPain")
        self.gridLayout_3.addWidget(self.NeckPain, 27, 0, 1, 1)
        self.RunnyNose = QtWidgets.QCheckBox(self.Head)
        self.RunnyNose.setObjectName("RunnyNose")
        self.gridLayout_3.addWidget(self.RunnyNose, 28, 0, 1, 1)
        self.VisualAura = QtWidgets.QCheckBox(self.Head)
        self.VisualAura.setObjectName("VisualAura")
        self.gridLayout_3.addWidget(self.VisualAura, 29, 0, 1, 1)
        self.Headaches = QtWidgets.QCheckBox(self.Head)
        self.Headaches.setObjectName("Headaches")
        self.gridLayout_3.addWidget(self.Headaches, 30, 0, 1, 1)
        self.SwollenLymphNodes = QtWidgets.QCheckBox(self.Head)
        self.SwollenLymphNodes.setObjectName("SwollenLymphNodes")
        self.gridLayout_3.addWidget(self.SwollenLymphNodes, 31, 0, 1, 1)
        self.PinkRedColorInWhitesEyes = QtWidgets.QCheckBox(self.Head)
        self.PinkRedColorInWhitesEyes.setObjectName("PinkRedColorInWhitesEyes")
        self.gridLayout_3.addWidget(self.PinkRedColorInWhitesEyes, 32, 0, 1, 1)
        self.SwollenBlueSkinUnderEyes = QtWidgets.QCheckBox(self.Head)
        self.SwollenBlueSkinUnderEyes.setObjectName("SwollenBlueSkinUnderEyes")
        self.gridLayout_3.addWidget(self.SwollenBlueSkinUnderEyes, 33, 0, 1, 1)
        self.SoreMouthMakesEatDrinkSleepHard = QtWidgets.QCheckBox(self.Head)
        self.SoreMouthMakesEatDrinkSleepHard.setObjectName("SoreMouthMakesEatDrinkSleepHard")
        self.gridLayout_3.addWidget(self.SoreMouthMakesEatDrinkSleepHard, 34, 0, 1, 1)
        self.tabWidget.addTab(self.Head, "")
        self.Torso = QtWidgets.QWidget()
        self.Torso.setObjectName("Torso")
        self.ChestPain = QtWidgets.QCheckBox(self.Torso)
        self.ChestPain.setGeometry(QtCore.QRect(10, 30, 151, 20))
        self.ChestPain.setObjectName("ChestPain")
        self.LossOfAppetite = QtWidgets.QCheckBox(self.Torso)
        self.LossOfAppetite.setGeometry(QtCore.QRect(10, 10, 191, 20))
        self.LossOfAppetite.setObjectName("LossOfAppetite")
        self.RapidHeartBeat = QtWidgets.QCheckBox(self.Torso)
        self.RapidHeartBeat.setGeometry(QtCore.QRect(10, 50, 221, 20))
        self.RapidHeartBeat.setObjectName("RapidHeartBeat")
        self.PainInSideBackBelowRibs = QtWidgets.QCheckBox(self.Torso)
        self.PainInSideBackBelowRibs.setGeometry(QtCore.QRect(10, 70, 381, 20))
        self.PainInSideBackBelowRibs.setObjectName("PainInSideBackBelowRibs")
        self.tabWidget.addTab(self.Torso, "")
        self.LowerBody = QtWidgets.QWidget()
        self.LowerBody.setObjectName("LowerBody")
        self.LegCramp = QtWidgets.QCheckBox(self.LowerBody)
        self.LegCramp.setGeometry(QtCore.QRect(20, 10, 171, 20))
        self.LegCramp.setObjectName("LegCramp")
        self.FrequentUrination = QtWidgets.QCheckBox(self.LowerBody)
        self.FrequentUrination.setGeometry(QtCore.QRect(20, 30, 171, 20))
        self.FrequentUrination.setObjectName("FrequentUrination")
        self.PainWhenUrinating = QtWidgets.QCheckBox(self.LowerBody)
        self.PainWhenUrinating.setGeometry(QtCore.QRect(20, 50, 201, 20))
        self.PainWhenUrinating.setObjectName("PainWhenUrinating")
        self.UrinatingSmallAmount = QtWidgets.QCheckBox(self.LowerBody)
        self.UrinatingSmallAmount.setGeometry(QtCore.QRect(20, 70, 221, 20))
        self.UrinatingSmallAmount.setObjectName("UrinatingSmallAmount")
        self.PinkRedBrownUrine = QtWidgets.QCheckBox(self.LowerBody)
        self.PinkRedBrownUrine.setGeometry(QtCore.QRect(20, 90, 211, 20))
        self.PinkRedBrownUrine.setObjectName("PinkRedBrownUrine")
        self.PersistentNeedToUrinate = QtWidgets.QCheckBox(self.LowerBody)
        self.PersistentNeedToUrinate.setGeometry(QtCore.QRect(20, 110, 261, 20))
        self.PersistentNeedToUrinate.setObjectName("PersistentNeedToUrinate")
        self.CloudyFoulSmellingUrine = QtWidgets.QCheckBox(self.LowerBody)
        self.CloudyFoulSmellingUrine.setGeometry(QtCore.QRect(20, 130, 241, 20))
        self.CloudyFoulSmellingUrine.setObjectName("CloudyFoulSmellingUrine")
        self.BurningSensationUrinating = QtWidgets.QCheckBox(self.LowerBody)
        self.BurningSensationUrinating.setGeometry(QtCore.QRect(20, 150, 311, 20))
        self.BurningSensationUrinating.setObjectName("BurningSensationUrinating")
        self.PainRadiatesLowerAbdomenGroin = QtWidgets.QCheckBox(self.LowerBody)
        self.PainRadiatesLowerAbdomenGroin.setGeometry(QtCore.QRect(20, 170, 391, 20))
        self.PainRadiatesLowerAbdomenGroin.setObjectName("PainRadiatesLowerAbdomenGroin")
        self.tabWidget.addTab(self.LowerBody, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        
        QLineEdit.setPlaceholderText(self.lineEdit, "Diagnosis #1")
        QLineEdit.setReadOnly (self.lineEdit, True)
        QLineEdit.setPlaceholderText(self.lineEdit_2, "Diagnosis #2")
        QLineEdit.setReadOnly (self.lineEdit_2, True)
        QLineEdit.setPlaceholderText(self.lineEdit_3, "Diagnosis #3")
        QLineEdit.setReadOnly (self.lineEdit_3, True)
        
        
        self.ConfirmButton.clicked.connect(self.ConfirmFunction) 
        self.ClearButton.clicked.connect(self.ClearFunction)


        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Diagnosis #3"))
        self.label.setText(_translate("MainWindow", "Differential Diagnosis"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Diagnosis #1"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Diagnosis #2"))
        self.ConfirmButton.setText(_translate("MainWindow", "Confirm"))
        self.ClearButton.setText(_translate("MainWindow", "Clear"))
        self.ExtremeHunger.setText(_translate("MainWindow", "Extreme Hunger"))
        self.BodyAches.setText(_translate("MainWindow", "Body Aches"))
        self.ExtremeThirst.setText(_translate("MainWindow", "Extreme Thirst"))
        self.Vomiting.setText(_translate("MainWindow", "Vomiting"))
        self.Fever.setText(_translate("MainWindow", "Fever"))
        self.RaisedPinkRedBumps.setText(_translate("MainWindow", "Raised Pink/Red Bumps"))
        self.PeriodicPainFluctuatingIntensity.setText(_translate("MainWindow", "Periodic Pain With Fluctuating Intensity"))
        self.ThrobbingPulsatingPain.setText(_translate("MainWindow", "Throbbing/Pulsating Pain"))
        self.Irritation.setText(_translate("MainWindow", "Irritation"))
        self.AchingMuscles.setText(_translate("MainWindow", "Aching Muscles"))
        self.NumbnessTingling.setText(_translate("MainWindow", "Numbness/Tingling"))
        self.SmallFluidFilledBlisters.setText(_translate("MainWindow", "Small Fluid-Filled Blisters"))
        self.Fatigue.setText(_translate("MainWindow", "Fatigue"))
        self.Weakness.setText(_translate("MainWindow", "Weakness"))
        self.PaleSkin.setText(_translate("MainWindow", "Pale Skin"))
        self.Chills.setText(_translate("MainWindow", "Chills"))
        self.Rash.setText(_translate("MainWindow", "Rash"))
        self.NightSweats.setText(_translate("MainWindow", "Night Sweats"))
        self.LossOfEnergy.setText(_translate("MainWindow", "Loss of Energy"))
        self.WeightLoss.setText(_translate("MainWindow", "Weight Loss"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.GeneralBody), _translate("MainWindow", "General Body"))
        self.Nausea.setText(_translate("MainWindow", "Nausea"))
        self.SinusPressure.setText(_translate("MainWindow", "Sinus Pressure"))
        self.Coughing.setText(_translate("MainWindow", "Coughing"))
        self.Drooling.setText(_translate("MainWindow", "Drooling"))
        self.Insomnia.setText(_translate("MainWindow", "Insomnia"))
        self.UrgeToRubEyes.setText(_translate("MainWindow", "Urge to Rub Eyes"))
        self.BlurryVision.setText(_translate("MainWindow", "Blurry Vision"))
        self.SoundSensitivity.setText(_translate("MainWindow", "Sound Sensitivity"))
        self.Wheezing.setText(_translate("MainWindow", "Wheezing"))
        self.ShortnessOfBreath.setText(_translate("MainWindow", "Shortness of Breath"))
        self.BreathingPain.setText(_translate("MainWindow", "Breathing Pain"))
        self.VisionChanges.setText(_translate("MainWindow", "Vision Changes"))
        self.CoughingBlood.setText(_translate("MainWindow", "Coughing blood"))
        self.DecreasedSenseOfTasteSmell.setText(_translate("MainWindow", "Decreased Sense of Taste or Smell"))
        self.DifficultyConcentrating.setText(_translate("MainWindow", "Difficulty Concentrating"))
        self.NasalCongestion.setText(_translate("MainWindow", "Nasal Congestion"))
        self.IncreasedAsthmaticReactions.setText(_translate("MainWindow", "Increased Asthmatic Reactions"))
        self.FacialPain.setText(_translate("MainWindow", "Facial Pain"))
        self.LightSensitivity.setText(_translate("MainWindow", "Light Sensitivity"))
        self.PainOnOneSideOfHead.setText(_translate("MainWindow", "Pain On One Side of The Head"))
        self.Dizziness.setText(_translate("MainWindow", "Dizziness"))
        self.IncreasedTears.setText(_translate("MainWindow", "Increased Tear Production"))
        self.ScratchyThroat.setText(_translate("MainWindow", "Scratchy Throat"))
        self.BurningEyes.setText(_translate("MainWindow", "Burning Eyes"))
        self.SoreThroat.setText(_translate("MainWindow", "Sore Throat"))
        self.BlockedNose.setText(_translate("MainWindow", "Blocked Nose"))
        self.ItchyEyes.setText(_translate("MainWindow", "Itchy Eyes"))
        self.NeckPain.setText(_translate("MainWindow", "Neck Pain"))
        self.RunnyNose.setText(_translate("MainWindow", "Runny Nose"))
        self.VisualAura.setText(_translate("MainWindow", "Visual Aura"))
        self.Headaches.setText(_translate("MainWindow", "Headaches"))
        self.SwollenLymphNodes.setText(_translate("MainWindow", "Swollen Lymph Nodes in Neck"))
        self.PinkRedColorInWhitesEyes.setText(_translate("MainWindow", "Pink/Red Color In the Whites of Eyes"))
        self.SwollenBlueSkinUnderEyes.setText(_translate("MainWindow", "Swollen, bluish colored skin below the eyes"))
        self.SoreMouthMakesEatDrinkSleepHard.setText(_translate("MainWindow", "Sore Mouth That Complicates Sleeping, Eating, Drinking"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Head), _translate("MainWindow", "Head"))
        self.ChestPain.setText(_translate("MainWindow", "Chest Pain"))
        self.LossOfAppetite.setText(_translate("MainWindow", "Loss of Appetite"))
        self.RapidHeartBeat.setText(_translate("MainWindow", "Rapid Heart Beat"))
        self.PainInSideBackBelowRibs.setText(_translate("MainWindow", "Severe Pain In The Side and Back, Below the Ribs"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Torso), _translate("MainWindow", "Torso"))
        self.LegCramp.setText(_translate("MainWindow", "Leg Cramps"))
        self.FrequentUrination.setText(_translate("MainWindow", "Frequent Urination"))
        self.PainWhenUrinating.setText(_translate("MainWindow", "Pain When Urinating"))
        self.UrinatingSmallAmount.setText(_translate("MainWindow", "Urinating Small Amounts"))
        self.PinkRedBrownUrine.setText(_translate("MainWindow", "Pink/Red/Brown Urine"))
        self.PersistentNeedToUrinate.setText(_translate("MainWindow", "Persistent Need to Urinate"))
        self.CloudyFoulSmellingUrine.setText(_translate("MainWindow", "Cloudy/Foul Smelling Urine"))
        self.BurningSensationUrinating.setText(_translate("MainWindow", "Burning Sensation When Urinating"))
        self.PainRadiatesLowerAbdomenGroin.setText(_translate("MainWindow", "Pain That Radiates To The Lower Abdomen/Groin"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.LowerBody), _translate("MainWindow", "Lower Body"))

    def ConfirmFunction(self):
        
       global ResponseVector
       index = 0
       
       #------------------------------------------#    
       if  self.AchingMuscles.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.AchingMuscles.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.BodyAches.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.BodyAches.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.Chills.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.Chills.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.Fatigue.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.Fatigue.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.ExtremeHunger.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.ExtremeHunger.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.ExtremeThirst.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.ExtremeThirst.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.Fever.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.Fever.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.Irritation.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.Irritation.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.LossOfEnergy.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.LossOfEnergy.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.NightSweats.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.NightSweats.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.NumbnessTingling.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.NumbnessTingling.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.PeriodicPainFluctuatingIntensity.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.PeriodicPainFluctuatingIntensity.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.PaleSkin.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.PaleSkin.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.RaisedPinkRedBumps.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.RaisedPinkRedBumps.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.Rash.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.Rash.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.SmallFluidFilledBlisters.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.SmallFluidFilledBlisters.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.ThrobbingPulsatingPain.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.ThrobbingPulsatingPain.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  True:
           ResponseVector[index] = 0
           index = index + 1
           # THIS IS THE ERROR TERM #
       
       #------------------------------------------#
       if  self.Vomiting.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.Vomiting.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.Weakness.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.Weakness.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.WeightLoss.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.WeightLoss.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.BlockedNose.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.BlockedNose.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.BlurryVision.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.BlurryVision.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.BurningEyes.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.BurningEyes.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.Coughing.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.Coughing.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.CoughingBlood.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.CoughingBlood.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.DecreasedSenseOfTasteSmell.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.DecreasedSenseOfTasteSmell.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.DifficultyConcentrating.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.DifficultyConcentrating.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.Dizziness.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.Dizziness.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.Drooling.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.Drooling.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.FacialPain.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.FacialPain.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.Headaches.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.Headaches.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.IncreasedAsthmaticReactions.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.IncreasedAsthmaticReactions.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.IncreasedTears.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.IncreasedTears.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.Insomnia.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.Insomnia.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.ItchyEyes.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.ItchyEyes.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.LightSensitivity.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.LightSensitivity.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.NasalCongestion.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.NasalCongestion.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.Nausea.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.Nausea.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.NeckPain.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.NeckPain.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.PainOnOneSideOfHead.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.PainOnOneSideOfHead.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.BreathingPain.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.BreathingPain.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.PinkRedColorInWhitesEyes.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.PinkRedColorInWhitesEyes.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.RunnyNose.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.RunnyNose.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.ScratchyThroat.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.ScratchyThroat.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.ShortnessOfBreath.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.ShortnessOfBreath.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.SinusPressure.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.SinusPressure.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.SoreMouthMakesEatDrinkSleepHard.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.SoreMouthMakesEatDrinkSleepHard.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.SoreThroat.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.SoreThroat.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.SoundSensitivity.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.SoundSensitivity.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.SwollenLymphNodes.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.SwollenLymphNodes.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.SwollenBlueSkinUnderEyes.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.SwollenBlueSkinUnderEyes.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.UrgeToRubEyes.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.UrgeToRubEyes.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.VisionChanges.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.VisionChanges.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.VisualAura.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.VisualAura.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.Wheezing.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.Wheezing.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.BurningSensationUrinating.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.BurningSensationUrinating.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.CloudyFoulSmellingUrine.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.CloudyFoulSmellingUrine.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.LegCramp.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.LegCramp.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.PainWhenUrinating.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.PainWhenUrinating.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.PainRadiatesLowerAbdomenGroin.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.PainRadiatesLowerAbdomenGroin.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.PersistentNeedToUrinate.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.PersistentNeedToUrinate.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.PinkRedBrownUrine.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.PinkRedBrownUrine.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.FrequentUrination.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.FrequentUrination.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.UrinatingSmallAmount.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.UrinatingSmallAmount.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.ChestPain.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.ChestPain.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.LossOfAppetite.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.LossOfAppetite.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.PainInSideBackBelowRibs.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.PainInSideBackBelowRibs.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       if  self.RapidHeartBeat.isChecked():
           ResponseVector[index] = 1
           index = index + 1
       elif not(self.RapidHeartBeat.isChecked()):
           ResponseVector[index] = 0
           index = index + 1
       #------------------------------------------#
       
      
        
       global WeightVector
       Diagnosis = []
       
       for x in range(len(WeightVector[0])):
           ResponseVector[x] = ResponseVector[x] * WeightVector[0][x]
        
       Diagnosis = algo.Method1(ResponseVector)
       
       QLineEdit.setText(self.lineEdit, Diagnosis[0])
       QLineEdit.setText(self.lineEdit_2, Diagnosis[1])
       QLineEdit.setText(self.lineEdit_3, Diagnosis[2])
       
  


     
    def ClearFunction(self):
       self.AchingMuscles.setChecked(False)
       self.BodyAches.setChecked(False)
       self.Chills.setChecked(False)
       self.Fatigue.setChecked(False)
       self.ExtremeHunger.setChecked(False)
       self.ExtremeThirst.setChecked(False)
       self.Fever.setChecked(False)
       self.Irritation.setChecked(False)
       self.LossOfEnergy.setChecked(False)
       self.NightSweats.setChecked(False)
       self.NumbnessTingling.setChecked(False)
       self.PeriodicPainFluctuatingIntensity.setChecked(False)
       self.PaleSkin.setChecked(False)
       self.RaisedPinkRedBumps.setChecked(False)
       self.Rash.setChecked(False)
       self.SmallFluidFilledBlisters.setChecked(False)
       self.ThrobbingPulsatingPain.setChecked(False)
       self.Vomiting.setChecked(False)
       self.Weakness.setChecked(False)
       self.WeightLoss.setChecked(False)
       self.BlockedNose.setChecked(False)
       self.BlurryVision.setChecked(False)
       self.BurningEyes.setChecked(False)
       self.Coughing.setChecked(False)
       self.CoughingBlood.setChecked(False)
       self.DecreasedSenseOfTasteSmell.setChecked(False)
       self.DifficultyConcentrating.setChecked(False)
       self.Dizziness.setChecked(False)
       self.Drooling.setChecked(False)
       self.FacialPain.setChecked(False)
       self.Headaches.setChecked(False)
       self.IncreasedAsthmaticReactions.setChecked(False)
       self.IncreasedTears.setChecked(False)
       self.Insomnia.setChecked(False)
       self.ItchyEyes.setChecked(False)
       self.LightSensitivity.setChecked(False)
       self.NasalCongestion.setChecked(False)
       self.Nausea.setChecked(False)
       self.NeckPain.setChecked(False)
       self.PainOnOneSideOfHead.setChecked(False)
       self.BreathingPain.setChecked(False)
       self.PinkRedColorInWhitesEyes.setChecked(False)
       self.RunnyNose.setChecked(False)
       self.ScratchyThroat.setChecked(False)
       self.ShortnessOfBreath.setChecked(False)
       self.SinusPressure.setChecked(False)
       self.SoreMouthMakesEatDrinkSleepHard.setChecked(False)
       self.SoreThroat.setChecked(False)
       self.SoundSensitivity.setChecked(False)
       self.SwollenLymphNodes.setChecked(False)
       self.SwollenBlueSkinUnderEyes.setChecked(False)
       self.UrgeToRubEyes.setChecked(False)
       self.VisionChanges.setChecked(False)
       self.VisualAura.setChecked(False)
       self.Wheezing.setChecked(False)
       self.BurningSensationUrinating.setChecked(False)
       self.CloudyFoulSmellingUrine.setChecked(False)
       self.LegCramp.setChecked(False)
       self.PainWhenUrinating.setChecked(False)
       self.PainRadiatesLowerAbdomenGroin.setChecked(False)
       self.PersistentNeedToUrinate.setChecked(False)
       self.PinkRedBrownUrine.setChecked(False)
       self.FrequentUrination.setChecked(False)
       self.UrinatingSmallAmount.setChecked(False)
       self.ChestPain.setChecked(False)
       self.LossOfAppetite.setChecked(False)
       self.PainInSideBackBelowRibs.setChecked(False)
       self.RapidHeartBeat.setChecked(False)
       
       QLineEdit.setText(self.lineEdit, "")
       QLineEdit.setText(self.lineEdit_2, "")
       QLineEdit.setText(self.lineEdit_3, "")

          

                

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    