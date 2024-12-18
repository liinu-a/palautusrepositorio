from kps_tekoaly import KPSTekoaly
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly(KPSTekoaly):
    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)
