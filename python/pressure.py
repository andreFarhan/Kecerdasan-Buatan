from matplotlib import pyplot as plt

class VariableFuzzy():

    def __init__(self):
        self.maximum = 0
        self.minimum = 0

    def naik(self, x):
        return (x - self.minimum )/(self.maximum - self.minimum)

    def turun(self, x):
        return (self.maximum - x)/(self.maximum - self.minimum)

class Speed(VariableFuzzy):

    def __init__(self):
        self.s1 = 40
        self.s2 = 60
        self.s3 = 80
        self.s4 = 100
        self.sn = 200
    
    def slow(self, x):
        # 0-s1 = 1
        if x < self.s1:
            return 1
        # s1-s2 = turun
        elif self.s1<=x<=self.s2:
            self.minimum = self.s1
            self.maximum = self.s2
            return self.turun(x)
        else:
            return 0

    def steady(self, x):
        # s1-s2 = naik
        if self.s1<=x<=self.s2:
            self.minimum = self.s1
            self.maximum = self.s2
            return self.naik(x)
        # s2-s3 = 1
        elif self.s2<=x<=self.s3:
            return 1
        # s3-s4 = turun
        elif self.s3<=x<=self.s4:
            self.minimum = self.s3
            self.maximum = self.s4
            return self.turun(x)
        else:
            return 0
    
    def fast(self, x):
        # s3-s4 = naik
        # s4-... = 1
        if x > self.s4:
            return 1
        elif self.s3<=x<=self.s4:
            self.minimum = self.s3
            self.maximum = self.s4
            return self.naik(x)
        else:
            return 0

    def graph(self, value=None):
        plt.figure(figsize=(15, 5))
        # slow
        # 0-s1 = 1 [1=>1]
        # s1-s2 = down[1=>0]
        # s2- ... [0=>0]
        x_slow = [0, self.s1, self.s2, self.sn]
        y_slow = [1, 1, 0, 0]
        plt.plot(x_slow, y_slow, label='slow')
        # steady
        # 0-s1  => 0[0-0]
        # s1-s2 =>up[0-1]
        # s2-s3 => 1 [1-1]
        # s3-s4 => down [1-0]
        # s4-sn = > 0 [0-0]
        x_steady = [0, self.s1, self.s2, self.s3, self.s4, self.sn]
        y_steady = [0, 0, 1, 1, 0, 0]
        plt.plot(x_steady, y_steady, label='steady')
        # fast
        # 0-s3 =>0[0-0]
        # s3-s4 => up[0-1]
        # s4-sn => 1[1-1]
        x_fast = [0, self.s3, self.s4, self.sn]
        y_fast = [0, 0, 1, 1]
        plt.plot(x_fast, y_fast, label='fast')

        if value:
            x_param = [0, value, value]
            y_slow = self.slow(value)
            y_steady = self.steady(value)
            y_fast = self.fast(value)
            y_param_slow = [y_slow, y_slow, 0]
            y_param_steady = [y_steady, y_steady, 0]
            y_param_fast = [y_fast, y_fast, 0]
            plt.plot(x_param, y_param_slow, label='slow_value')
            plt.plot(x_param, y_param_steady, label='steady_value')
            plt.plot(x_param, y_param_fast, label='fast_value')


        plt.legend(loc = 'upper left')
        plt.show()


class Pressure(VariableFuzzy):

    def __init__(self):
        self.p1 = 5
        self.p2 = 10
        self.p3 = 15
        self.p4 = 20
        self.p5 = 23
        self.p6 = 28
        self.p7 = 35
        self.p8 = 40
        self.p9 = 70
        self.pn = 80

        self.color = {
            'very_low': 'C0',
            'low': 'C1',
            'medium': 'C2',
            'high': 'C3',
            'very_high': 'C4',
        }
        self.default = 'C5'
    
    def very_low(self, x):
        # 0-p1 = 1
        # p1-p2 = down
        if x < self.p1:
            return 1
        elif self.p1<=x<=self.p2:
            self.minimum = self.p1
            self.maximum = self.p2
            return self.turun(x)
        else:
            return 0

    def low(self, x):
        # p1-p2=up
        # p2-p4=down
        if self.p1<=x<=self.p2:
            self.minimum = self.p1
            self.maximum = self.p2
            return self.naik(x)
        elif self.p2<=x<=self.p4:
            self.minimum = self.p2
            self.maximum = self.p4
            return self.turun(x)
        else:
            return 0

    def medium(self, x):
        # p3-p5 = up
        # p5-p6 =1
        # p6-p7 = down
        if self.p3<=x<=self.p5:
            self.minimum = self.p3
            self.maximum = self.p5
            return self.naik(x)
        elif self.p5<=x<=self.p6:
            return 1
        elif self.p6<=x<=self.p7:
            self.minimum = self.p6
            self.maximum = self.p7
            return self.turun(x)
        else:
            return 0

    def high(self, x):
        # p6-p8 = up
        # p8-p9 = down
        if self.p6<=x<=self.p8:
            self.minimum = self.p6
            self.maximum = self.p8
            return self.naik(x)
        elif self.p8<=x<=self.p9:
            self.minimum = self.p8
            self.maximum = self.p9
            return self.turun(x)
        else:
            return 0


    def very_high(self, x):
        # p8-p9 = up
        # p9-...=1
        if x > self.p9:
            return 1
        elif self.p8<=x<=self.p9:
            self.minimum = self.p8
            self.maximum = self.p9
            return self.naik(x)
        else:
            return 0

    def graph(self, value=None):
        plt.figure(figsize=(15, 5))
        # very low
        # 0-p1 = 1
        # p1-p2 = down
        # p2-pn = 0
        x_v_low = [0, self.p1, self.p2, self.pn]
        y_v_low = [1, 1, 0, 0]
        plt.plot(x_v_low, y_v_low, label='very low', color=self.color.get('very_low', self.default))
        # low
        # 0-p1 = 0
        # p1-p2 = up
        # p2-p4 = down
        # p4-pn = 0
        x_low = [0, self.p1, self.p2, self.p4, self.pn]
        y_low = [0, 0, 1, 0, 0]
        plt.plot(x_low, y_low, label='low', color=self.color.get('low', self.default))
        # medium
        # 0-p3 = 0
        # p3-p5 = up
        # p5-p6 =1
        # p6-p7 = down
        # p7-pn = 0
        x_medium = [0, self.p3, self.p5, self.p6, self.p7, self.pn]
        y_medium = [0, 0, 1, 1, 0, 0]
        plt.plot(x_medium, y_medium, label='medium', color=self.color.get('medium', self.default))
        # high
        # 0-p6 = 0
        # p6-p8 = up
        # p8-p9 = down
        # p9-pn = 0
        x_low = [0, self.p6, self.p8, self.p9, self.pn]
        y_low = [0, 0, 1, 0, 0]
        plt.plot(x_low, y_low, label='high', color=self.color.get('high', self.default))
        # very high
        # 0-p8 = 0
        # p8-p9 = up
        # p9-pn = 1
        x_fast = [0, self.p8, self.p9, self.pn]
        y_fast = [0, 0, 1, 1]
        plt.plot(x_fast, y_fast, label='very high', color=self.color.get('very_high', self.default))
        if value:
            x_param = [0, value, value]
            y_v_low = self.very_low(value)
            y_low = self.low(value)
            y_medium = self.medium(value)
            y_high = self.high(value)
            y_v_high = self.very_high(value)

            y_param_v_low = [y_v_low, y_v_low, 0]
            y_param_low = [y_low, y_low, 0]
            y_param_medium = [y_medium, y_medium, 0]
            y_param_high = [y_high, y_high, 0]
            y_param_v_high = [y_v_high, y_v_high, 0]


            plt.plot(x_param, y_param_v_low, label='very low value', color=self.color.get('very_low', self.default))
            plt.plot(x_param, y_param_low, label='low value', color=self.color.get('low', self.default))
            plt.plot(x_param, y_param_medium, label='medium value', color=self.color.get('medium', self.default))
            plt.plot(x_param, y_param_high, label='high value', color=self.color.get('high', self.default))
            plt.plot(x_param, y_param_v_high, label='very high value', color=self.color.get('very_high', self.default))
            plt.legend(loc = 'upper right')


# output
class Value(VariableFuzzy):
    minimum = 1000
    maximum = 5000
    speed = 0
    pressure = 0

    def __init__(self):
        self.p1 = 1000
        self.p2 = 5000
        self.pn = 6000
        self.speed = 0
        self.pressure = 0
        self.turun = 0
        self.naik = 0
        self.real_value = 0

    def _berturun(self, a):
        self.turun = self.p2 - a*(self.p2 - self.p1)
        return self.turun


    def _bernaik(self, a):
        self.naik =  a*(self.p2 - self.p1) + self.p1
        return self.naik
    
    @property
    def fuzzy_berturun(self):
        x = self.real_value
        if x >= self.p2:
            return 0
        elif x<= self.p1:
            return 1
        else:
            self.minimum = self.p1
            self.maximum = self.p2
            return self.down(x)
    
    @property
    def fuzzy_bernaik(self):
        x = self.real_value
        if x >= self.p2:
            return 1
        elif x<= self.p1:
            return 0
        else:
            self.minimum = self.p1
            self.maximum = self.p2
            return self.up(x)
    

    def _inferensi(self, spd=Speed(), prs=Pressure()):
        result = []
        # [R1] JIKA Speed TURUN, dan Pressure BANYAK, MAKA
        # Value BERKURANG.
        a1 = min(spd.turun(self.speed), prs.banyak(self.pressure))
        z1 = self._berturun(a1)
        result.append((a1, z1))
        # [R2] JIKA Speed TURUN, dan Pressure SEDIKIT, MAKA
        # Value BERKURANG.
        a2 = min(spd.turun(self.speed), prs.sedikit(self.pressure))
        z2 = self._berturun(a2)
        result.append((a2, z2))
        # [R3] JIKA Speed NAIK, dan Pressure BANYAK, MAKA
        # Value BERTAMBAH.
        a3 = min(spd.naik(self.speed), prs.banyak(self.pressure))
        z3 = self._bernaik(a3)
        result.append((a3, z3))
        # [R4] JIKA Speed NAIK, dan Pressure SEDIKIT, MAKA
        # Value BERTAMBAH.
        a4 = min(spd.naik(self.speed), prs.sedikit(self.pressure))
        z4 = self._bernaik(a4)
        result.append((a4, z4))
        return result
    
    def defuzifikasi(self, data_inferensi=[]):
        # (α1∗z1+α2∗z2+α3∗z3+α4∗z4) / (α1+α2+α3+α4)
        data_inferensi = data_inferensi if data_inferensi else self._inferensi()
        res_a_z = 0
        res_a = 0
        for data in data_inferensi:
            # data[0] = a 
            # data[1] = z
            res_a_z += data[0] * data[1]
            res_a += data[0]
        self.real_value = res_a_z/res_a
        return self.real_value
    
    def graph(self):
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
        spd = Speed()
        prs = Pressure()

        spd.graph(ax1, self.speed)
        prs.graph(ax2, self.pressure)
        # berturun
        x = [0, self.p1, self.p2, self.pn]
        y_krg = [1, 1, 0, 0]
        ax3.plot(x, y_krg, label='berturun', color='C0')
        # bernaik
        y_tmb = [0, 0, 1, 1]
        ax3.plot(x, y_tmb, label='bernaik', color='C1')
        ax3.set_title('Value [Output]')
        ax3.legend(loc='upper left')
        if self.real_value:
            value = self.real_value
            # turun
            x_param = [0, value, value]
            turun_value = self.fuzzy_berturun
            y_param_turun = [turun_value, turun_value, 0]
            ax3.plot(x_param, y_param_turun, color='C0')
            # naik
            naik_value = self.fuzzy_bernaik
            y_param_naik = [naik_value, naik_value, 0]
            ax3.plot(x_param, y_param_naik, color='C1')

        plt.show()


speed = input('Speed:')
pressure = input('Pressure:')
produksi = Value()



produksi.speed = float(speed) # 2500
produksi.pressure = float(pressure) # 160
hasil_produksi = produksi.defuzifikasi()

print(f'Hasil produksi {hasil_produksi}')

produksi.graph()