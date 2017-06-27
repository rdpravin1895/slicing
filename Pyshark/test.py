# -*- coding: utf-8 -*-
import pyshark

cap = pyshark.LiveCapture(interface='Wi-Fi′)
cap.sniff()
