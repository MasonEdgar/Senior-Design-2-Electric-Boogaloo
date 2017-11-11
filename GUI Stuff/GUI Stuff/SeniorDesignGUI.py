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
        MainWindow.resize(753, 619)
        MainWindow.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 210, 751, 221))
        self.tabWidget.setObjectName("tabWidget")
        self.GeneralBody = QtWidgets.QWidget()
        self.GeneralBody.setObjectName("GeneralBody")
        self.Rash = QtWidgets.QCheckBox(self.GeneralBody)
        self.Rash.setGeometry(QtCore.QRect(10, 10, 51, 17))
        self.Rash.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Rash.setObjectName("Rash")
        self.Fever = QtWidgets.QCheckBox(self.GeneralBody)
        self.Fever.setGeometry(QtCore.QRect(10, 30, 51, 17))
        self.Fever.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Fever.setObjectName("Fever")
        self.Chills = QtWidgets.QCheckBox(self.GeneralBody)
        self.Chills.setGeometry(QtCore.QRect(10, 50, 51, 17))
        self.Chills.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Chills.setObjectName("Chills")
        self.Fatigue = QtWidgets.QCheckBox(self.GeneralBody)
        self.Fatigue.setGeometry(QtCore.QRect(10, 70, 61, 17))
        self.Fatigue.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Fatigue.setObjectName("Fatigue")
        self.Vomiting = QtWidgets.QCheckBox(self.GeneralBody)
        self.Vomiting.setGeometry(QtCore.QRect(10, 90, 71, 17))
        self.Vomiting.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Vomiting.setObjectName("Vomiting")
        self.Weakness = QtWidgets.QCheckBox(self.GeneralBody)
        self.Weakness.setGeometry(QtCore.QRect(10, 110, 71, 17))
        self.Weakness.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Weakness.setObjectName("Weakness")
        self.PaleSkin = QtWidgets.QCheckBox(self.GeneralBody)
        self.PaleSkin.setGeometry(QtCore.QRect(10, 130, 71, 17))
        self.PaleSkin.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PaleSkin.setObjectName("PaleSkin")
        self.BodyAches = QtWidgets.QCheckBox(self.GeneralBody)
        self.BodyAches.setGeometry(QtCore.QRect(10, 150, 81, 17))
        self.BodyAches.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.BodyAches.setObjectName("BodyAches")
        self.Irritation = QtWidgets.QCheckBox(self.GeneralBody)
        self.Irritation.setGeometry(QtCore.QRect(10, 170, 71, 17))
        self.Irritation.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Irritation.setObjectName("Irritation")
        self.WeightLoss = QtWidgets.QCheckBox(self.GeneralBody)
        self.WeightLoss.setGeometry(QtCore.QRect(100, 10, 81, 17))
        self.WeightLoss.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.WeightLoss.setObjectName("WeightLoss")
        self.NightSweats = QtWidgets.QCheckBox(self.GeneralBody)
        self.NightSweats.setGeometry(QtCore.QRect(100, 30, 91, 17))
        self.NightSweats.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.NightSweats.setObjectName("NightSweats")
        self.NumbnessTingling = QtWidgets.QCheckBox(self.GeneralBody)
        self.NumbnessTingling.setGeometry(QtCore.QRect(100, 130, 111, 17))
        self.NumbnessTingling.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.NumbnessTingling.setObjectName("NumbnessTingling")
        self.LossOfEnergy = QtWidgets.QCheckBox(self.GeneralBody)
        self.LossOfEnergy.setGeometry(QtCore.QRect(100, 70, 101, 17))
        self.LossOfEnergy.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LossOfEnergy.setObjectName("LossOfEnergy")
        self.AchingMuscles = QtWidgets.QCheckBox(self.GeneralBody)
        self.AchingMuscles.setGeometry(QtCore.QRect(100, 50, 91, 17))
        self.AchingMuscles.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.AchingMuscles.setObjectName("AchingMuscles")
        self.SmallFluidFilledBlisters = QtWidgets.QCheckBox(self.GeneralBody)
        self.SmallFluidFilledBlisters.setGeometry(QtCore.QRect(220, 10, 141, 17))
        self.SmallFluidFilledBlisters.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SmallFluidFilledBlisters.setObjectName("SmallFluidFilledBlisters")
        self.ExtremeHunger = QtWidgets.QCheckBox(self.GeneralBody)
        self.ExtremeHunger.setGeometry(QtCore.QRect(100, 90, 101, 17))
        self.ExtremeHunger.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ExtremeHunger.setObjectName("ExtremeHunger")
        self.ExtremeThirst = QtWidgets.QCheckBox(self.GeneralBody)
        self.ExtremeThirst.setGeometry(QtCore.QRect(100, 110, 101, 17))
        self.ExtremeThirst.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ExtremeThirst.setObjectName("ExtremeThirst")
        self.RaisedPinkRedBumps = QtWidgets.QCheckBox(self.GeneralBody)
        self.RaisedPinkRedBumps.setGeometry(QtCore.QRect(100, 150, 141, 17))
        self.RaisedPinkRedBumps.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.RaisedPinkRedBumps.setObjectName("RaisedPinkRedBumps")
        self.ThrobbingPulsatingPain = QtWidgets.QCheckBox(self.GeneralBody)
        self.ThrobbingPulsatingPain.setGeometry(QtCore.QRect(100, 170, 141, 17))
        self.ThrobbingPulsatingPain.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ThrobbingPulsatingPain.setObjectName("ThrobbingPulsatingPain")
        self.PeriodicPainFluctuatingIntensity = QtWidgets.QCheckBox(self.GeneralBody)
        self.PeriodicPainFluctuatingIntensity.setGeometry(QtCore.QRect(220, 30, 211, 17))
        self.PeriodicPainFluctuatingIntensity.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PeriodicPainFluctuatingIntensity.setObjectName("PeriodicPainFluctuatingIntensity")
        self.tabWidget.addTab(self.GeneralBody, "")
        self.Head = QtWidgets.QWidget()
        self.Head.setObjectName("Head")
        self.Nausea = QtWidgets.QCheckBox(self.Head)
        self.Nausea.setGeometry(QtCore.QRect(10, 10, 61, 17))
        self.Nausea.setObjectName("Nausea")
        self.Coughing = QtWidgets.QCheckBox(self.Head)
        self.Coughing.setGeometry(QtCore.QRect(10, 30, 71, 17))
        self.Coughing.setObjectName("Coughing")
        self.Drooling = QtWidgets.QCheckBox(self.Head)
        self.Drooling.setGeometry(QtCore.QRect(10, 50, 71, 17))
        self.Drooling.setObjectName("Drooling")
        self.Insomnia = QtWidgets.QCheckBox(self.Head)
        self.Insomnia.setGeometry(QtCore.QRect(10, 70, 71, 17))
        self.Insomnia.setObjectName("Insomnia")
        self.Wheezing = QtWidgets.QCheckBox(self.Head)
        self.Wheezing.setGeometry(QtCore.QRect(90, 10, 71, 17))
        self.Wheezing.setObjectName("Wheezing")
        self.Dizziness = QtWidgets.QCheckBox(self.Head)
        self.Dizziness.setGeometry(QtCore.QRect(90, 30, 71, 17))
        self.Dizziness.setObjectName("Dizziness")
        self.Headaches = QtWidgets.QCheckBox(self.Head)
        self.Headaches.setGeometry(QtCore.QRect(90, 50, 71, 17))
        self.Headaches.setObjectName("Headaches")
        self.NeckPain = QtWidgets.QCheckBox(self.Head)
        self.NeckPain.setGeometry(QtCore.QRect(90, 70, 71, 17))
        self.NeckPain.setObjectName("NeckPain")
        self.ItchyEyes = QtWidgets.QCheckBox(self.Head)
        self.ItchyEyes.setGeometry(QtCore.QRect(170, 10, 81, 17))
        self.ItchyEyes.setObjectName("ItchyEyes")
        self.RunnyNose = QtWidgets.QCheckBox(self.Head)
        self.RunnyNose.setGeometry(QtCore.QRect(170, 30, 81, 17))
        self.RunnyNose.setObjectName("RunnyNose")
        self.FacialPain = QtWidgets.QCheckBox(self.Head)
        self.FacialPain.setGeometry(QtCore.QRect(170, 50, 71, 17))
        self.FacialPain.setObjectName("FacialPain")
        self.SoreThroat = QtWidgets.QCheckBox(self.Head)
        self.SoreThroat.setGeometry(QtCore.QRect(170, 70, 81, 17))
        self.SoreThroat.setObjectName("SoreThroat")
        self.VisualAura = QtWidgets.QCheckBox(self.Head)
        self.VisualAura.setGeometry(QtCore.QRect(260, 10, 81, 17))
        self.VisualAura.setObjectName("VisualAura")
        self.BlockedNose = QtWidgets.QCheckBox(self.Head)
        self.BlockedNose.setGeometry(QtCore.QRect(260, 30, 81, 17))
        self.BlockedNose.setObjectName("BlockedNose")
        self.BurningEyes = QtWidgets.QCheckBox(self.Head)
        self.BurningEyes.setGeometry(QtCore.QRect(260, 50, 91, 17))
        self.BurningEyes.setObjectName("BurningEyes")
        self.BlurryVision = QtWidgets.QCheckBox(self.Head)
        self.BlurryVision.setGeometry(QtCore.QRect(260, 70, 81, 17))
        self.BlurryVision.setObjectName("BlurryVision")
        self.SinusPressure = QtWidgets.QCheckBox(self.Head)
        self.SinusPressure.setGeometry(QtCore.QRect(350, 10, 91, 17))
        self.SinusPressure.setObjectName("SinusPressure")
        self.VisionChanges = QtWidgets.QCheckBox(self.Head)
        self.VisionChanges.setGeometry(QtCore.QRect(350, 30, 101, 17))
        self.VisionChanges.setObjectName("VisionChanges")
        self.NasalCongestion = QtWidgets.QCheckBox(self.Head)
        self.NasalCongestion.setGeometry(QtCore.QRect(350, 70, 101, 17))
        self.NasalCongestion.setObjectName("NasalCongestion")
        self.ScratchyThroat = QtWidgets.QCheckBox(self.Head)
        self.ScratchyThroat.setGeometry(QtCore.QRect(350, 50, 101, 17))
        self.ScratchyThroat.setObjectName("ScratchyThroat")
        self.CoughingBlood = QtWidgets.QCheckBox(self.Head)
        self.CoughingBlood.setGeometry(QtCore.QRect(460, 10, 111, 17))
        self.CoughingBlood.setObjectName("CoughingBlood")
        self.LightSensitivity = QtWidgets.QCheckBox(self.Head)
        self.LightSensitivity.setGeometry(QtCore.QRect(460, 30, 101, 17))
        self.LightSensitivity.setObjectName("LightSensitivity")
        self.SoundSensitivity = QtWidgets.QCheckBox(self.Head)
        self.SoundSensitivity.setGeometry(QtCore.QRect(460, 50, 101, 17))
        self.SoundSensitivity.setObjectName("SoundSensitivity")
        self.BreathingPain = QtWidgets.QCheckBox(self.Head)
        self.BreathingPain.setGeometry(QtCore.QRect(460, 70, 101, 17))
        self.BreathingPain.setObjectName("BreathingPain")
        self.ShortnessOfBreath = QtWidgets.QCheckBox(self.Head)
        self.ShortnessOfBreath.setGeometry(QtCore.QRect(570, 10, 121, 17))
        self.ShortnessOfBreath.setObjectName("ShortnessOfBreath")
        self.UrgeToRubEyes = QtWidgets.QCheckBox(self.Head)
        self.UrgeToRubEyes.setGeometry(QtCore.QRect(570, 30, 111, 17))
        self.UrgeToRubEyes.setObjectName("UrgeToRubEyes")
        self.DifficultyConcentrating = QtWidgets.QCheckBox(self.Head)
        self.DifficultyConcentrating.setGeometry(QtCore.QRect(570, 50, 141, 17))
        self.DifficultyConcentrating.setObjectName("DifficultyConcentrating")
        self.IncreasedTears = QtWidgets.QCheckBox(self.Head)
        self.IncreasedTears.setGeometry(QtCore.QRect(570, 70, 151, 17))
        self.IncreasedTears.setObjectName("IncreasedTears")
        self.SwollenLymphNodes = QtWidgets.QCheckBox(self.Head)
        self.SwollenLymphNodes.setGeometry(QtCore.QRect(10, 100, 161, 17))
        self.SwollenLymphNodes.setObjectName("SwollenLymphNodes")
        self.PainOnOneSideOfHead = QtWidgets.QCheckBox(self.Head)
        self.PainOnOneSideOfHead.setGeometry(QtCore.QRect(190, 100, 171, 17))
        self.PainOnOneSideOfHead.setObjectName("PainOnOneSideOfHead")
        self.IncreasedAsthmaticReactions = QtWidgets.QCheckBox(self.Head)
        self.IncreasedAsthmaticReactions.setGeometry(QtCore.QRect(370, 100, 171, 17))
        self.IncreasedAsthmaticReactions.setObjectName("IncreasedAsthmaticReactions")
        self.DecreasedSenseOfTasteSmell = QtWidgets.QCheckBox(self.Head)
        self.DecreasedSenseOfTasteSmell.setGeometry(QtCore.QRect(550, 100, 191, 17))
        self.DecreasedSenseOfTasteSmell.setObjectName("DecreasedSenseOfTasteSmell")
        self.PinkRedColorInWhitesEyes = QtWidgets.QCheckBox(self.Head)
        self.PinkRedColorInWhitesEyes.setGeometry(QtCore.QRect(10, 120, 201, 21))
        self.PinkRedColorInWhitesEyes.setObjectName("PinkRedColorInWhitesEyes")
        self.SwollenBlueSkinUnderEyes = QtWidgets.QCheckBox(self.Head)
        self.SwollenBlueSkinUnderEyes.setGeometry(QtCore.QRect(10, 140, 231, 20))
        self.SwollenBlueSkinUnderEyes.setObjectName("SwollenBlueSkinUnderEyes")
        self.SoreMouthMakesEatDrinkSleepHard = QtWidgets.QCheckBox(self.Head)
        self.SoreMouthMakesEatDrinkSleepHard.setGeometry(QtCore.QRect(10, 160, 291, 21))
        self.SoreMouthMakesEatDrinkSleepHard.setObjectName("SoreMouthMakesEatDrinkSleepHard")
        self.tabWidget.addTab(self.Head, "")
        self.Torso = QtWidgets.QWidget()
        self.Torso.setObjectName("Torso")
        self.ChestPain = QtWidgets.QCheckBox(self.Torso)
        self.ChestPain.setGeometry(QtCore.QRect(10, 10, 70, 17))
        self.ChestPain.setObjectName("ChestPain")
        self.LossOfAppetite = QtWidgets.QCheckBox(self.Torso)
        self.LossOfAppetite.setGeometry(QtCore.QRect(10, 30, 141, 17))
        self.LossOfAppetite.setObjectName("LossOfAppetite")
        self.RapidHeartBeat = QtWidgets.QCheckBox(self.Torso)
        self.RapidHeartBeat.setGeometry(QtCore.QRect(10, 50, 121, 17))
        self.RapidHeartBeat.setObjectName("RapidHeartBeat")
        self.PainInSideBackBelowRibs = QtWidgets.QCheckBox(self.Torso)
        self.PainInSideBackBelowRibs.setGeometry(QtCore.QRect(10, 70, 261, 17))
        self.PainInSideBackBelowRibs.setObjectName("PainInSideBackBelowRibs")
        self.tabWidget.addTab(self.Torso, "")
        self.LowerBody = QtWidgets.QWidget()
        self.LowerBody.setObjectName("LowerBody")
        self.LegCramp = QtWidgets.QCheckBox(self.LowerBody)
        self.LegCramp.setGeometry(QtCore.QRect(10, 10, 70, 17))
        self.LegCramp.setObjectName("LegCramp")
        self.FrequentUrination = QtWidgets.QCheckBox(self.LowerBody)
        self.FrequentUrination.setGeometry(QtCore.QRect(10, 30, 121, 17))
        self.FrequentUrination.setObjectName("FrequentUrination")
        self.PainWhenUrinating = QtWidgets.QCheckBox(self.LowerBody)
        self.PainWhenUrinating.setGeometry(QtCore.QRect(10, 50, 151, 17))
        self.PainWhenUrinating.setObjectName("PainWhenUrinating")
        self.UrinatingSmallAmount = QtWidgets.QCheckBox(self.LowerBody)
        self.UrinatingSmallAmount.setGeometry(QtCore.QRect(10, 70, 141, 17))
        self.UrinatingSmallAmount.setObjectName("UrinatingSmallAmount")
        self.PinkRedBrownUrine = QtWidgets.QCheckBox(self.LowerBody)
        self.PinkRedBrownUrine.setGeometry(QtCore.QRect(10, 90, 131, 17))
        self.PinkRedBrownUrine.setObjectName("PinkRedBrownUrine")
        self.PersistentNeedToUrinate = QtWidgets.QCheckBox(self.LowerBody)
        self.PersistentNeedToUrinate.setGeometry(QtCore.QRect(10, 110, 151, 17))
        self.PersistentNeedToUrinate.setObjectName("PersistentNeedToUrinate")
        self.CloudyFoulSmellingUrine = QtWidgets.QCheckBox(self.LowerBody)
        self.CloudyFoulSmellingUrine.setGeometry(QtCore.QRect(10, 130, 151, 17))
        self.CloudyFoulSmellingUrine.setObjectName("CloudyFoulSmellingUrine")
        self.BurningSensationUrinating = QtWidgets.QCheckBox(self.LowerBody)
        self.BurningSensationUrinating.setGeometry(QtCore.QRect(10, 150, 191, 17))
        self.BurningSensationUrinating.setObjectName("BurningSensationUrinating")
        self.PainRadiatesLowerAbdomenGroin = QtWidgets.QCheckBox(self.LowerBody)
        self.PainRadiatesLowerAbdomenGroin.setGeometry(QtCore.QRect(10, 170, 261, 17))
        self.PainRadiatesLowerAbdomenGroin.setObjectName("PainRadiatesLowerAbdomenGroin")
        self.tabWidget.addTab(self.LowerBody, "")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(280, 490, 211, 20))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(280, 520, 211, 20))
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(280, 550, 211, 20))
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 450, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.ConfirmButton = QtWidgets.QPushButton(self.centralwidget)
        self.ConfirmButton.setGeometry(QtCore.QRect(660, 430, 91, 31))
        self.ConfirmButton.setStyleSheet("background-color:rgb(85, 255, 255)")
        self.ConfirmButton.setFlat(False)
        self.ConfirmButton.setObjectName("ConfirmButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 30, 321, 151))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("SD_Logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 753, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        QLineEdit.setPlaceholderText(self.lineEdit, "Diagnosis #1")
        QLineEdit.setReadOnly (self.lineEdit, True)
        QLineEdit.setPlaceholderText(self.lineEdit_2, "Diagnosis #2")
        QLineEdit.setReadOnly (self.lineEdit_2, True)
        QLineEdit.setPlaceholderText(self.lineEdit_3, "Diagnosis #3")
        QLineEdit.setReadOnly (self.lineEdit_3, True)
        
        
        self.ConfirmButton.clicked.connect(self.ConfirmFunction) 


        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Rash.setText(_translate("MainWindow", "Rash"))
        self.Fever.setText(_translate("MainWindow", "Fever"))
        self.Chills.setText(_translate("MainWindow", "Chills"))
        self.Fatigue.setText(_translate("MainWindow", "Fatigue"))
        self.Vomiting.setText(_translate("MainWindow", "Vomiting"))
        self.Weakness.setText(_translate("MainWindow", "Weakness"))
        self.PaleSkin.setText(_translate("MainWindow", "Pale Skin"))
        self.BodyAches.setText(_translate("MainWindow", "Body Aches"))
        self.Irritation.setText(_translate("MainWindow", "Irritation"))
        self.WeightLoss.setText(_translate("MainWindow", "Weight Loss"))
        self.NightSweats.setText(_translate("MainWindow", "Night Sweats"))
        self.NumbnessTingling.setText(_translate("MainWindow", "Numbness/Tingling"))
        self.LossOfEnergy.setText(_translate("MainWindow", "Loss of Energy"))
        self.AchingMuscles.setText(_translate("MainWindow", "Aching Muscles"))
        self.SmallFluidFilledBlisters.setText(_translate("MainWindow", "Small Fluid-Filled Blisters"))
        self.ExtremeHunger.setText(_translate("MainWindow", "Extreme Hunger"))
        self.ExtremeThirst.setText(_translate("MainWindow", "Extreme Thirst"))
        self.RaisedPinkRedBumps.setText(_translate("MainWindow", "Raised Pink/Red Bumps"))
        self.ThrobbingPulsatingPain.setText(_translate("MainWindow", "Throbbing/Pulsating Pain"))
        self.PeriodicPainFluctuatingIntensity.setText(_translate("MainWindow", "Periodic Pain With Fluctuating Intensity"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.GeneralBody), _translate("MainWindow", "General Body"))
        self.Nausea.setText(_translate("MainWindow", "Nausea"))
        self.Coughing.setText(_translate("MainWindow", "Coughing"))
        self.Drooling.setText(_translate("MainWindow", "Drooling"))
        self.Insomnia.setText(_translate("MainWindow", "Insomnia"))
        self.Wheezing.setText(_translate("MainWindow", "Wheezing"))
        self.Dizziness.setText(_translate("MainWindow", "Dizziness"))
        self.Headaches.setText(_translate("MainWindow", "Headaches"))
        self.NeckPain.setText(_translate("MainWindow", "Neck Pain"))
        self.ItchyEyes.setText(_translate("MainWindow", "Itchy Eyes"))
        self.RunnyNose.setText(_translate("MainWindow", "Runny Nose"))
        self.FacialPain.setText(_translate("MainWindow", "Facial Pain"))
        self.SoreThroat.setText(_translate("MainWindow", "Sore Throat"))
        self.VisualAura.setText(_translate("MainWindow", "Visual Aura"))
        self.BlockedNose.setText(_translate("MainWindow", "Blocked Nose"))
        self.BurningEyes.setText(_translate("MainWindow", "Burning Eyes"))
        self.BlurryVision.setText(_translate("MainWindow", "Blurry Vision"))
        self.SinusPressure.setText(_translate("MainWindow", "Sinus Pressure"))
        self.VisionChanges.setText(_translate("MainWindow", "Vision Changes"))
        self.NasalCongestion.setText(_translate("MainWindow", "Nasal Congestion"))
        self.ScratchyThroat.setText(_translate("MainWindow", "Scratchy Throat"))
        self.CoughingBlood.setText(_translate("MainWindow", "Coughing blood"))
        self.LightSensitivity.setText(_translate("MainWindow", "Light Sensitivity"))
        self.SoundSensitivity.setText(_translate("MainWindow", "Sound Sensitivity"))
        self.BreathingPain.setText(_translate("MainWindow", "Breathing Pain"))
        self.ShortnessOfBreath.setText(_translate("MainWindow", "Shortness of Breath"))
        self.UrgeToRubEyes.setText(_translate("MainWindow", "Urge to Rub Eyes"))
        self.DifficultyConcentrating.setText(_translate("MainWindow", "Difficulty Concentrating"))
        self.IncreasedTears.setText(_translate("MainWindow", "Increased Tear Production"))
        self.SwollenLymphNodes.setText(_translate("MainWindow", "Swollen Lymph Nodes in Neck"))
        self.PainOnOneSideOfHead.setText(_translate("MainWindow", "Pain On One Side of The Head"))
        self.IncreasedAsthmaticReactions.setText(_translate("MainWindow", "Increased Asthmatic Reactions"))
        self.DecreasedSenseOfTasteSmell.setText(_translate("MainWindow", "Decreased Sense of Taste or Smell"))
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
        self.label.setText(_translate("MainWindow", "Differential Diagnosis"))
        self.ConfirmButton.setText(_translate("MainWindow", "Confirm"))


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

        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

