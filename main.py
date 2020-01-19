# [START gae_python37_app]
from flask import Flask, render_template
from datetime import datetime, date, time

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')

  
def main():
    class Timetabler:
        def __init__(self, startTime, endTime, increment, bus):
            self.H,self.M = startTime #unpack start time tuple
            self.fH,self.fM = endTime #unpack end time tuple
            self.times = list()
            self.increment = increment
            self.bus = bus
        def getTimes(self):
            while (self.H <= self.fH):
                if (self.H==self.fH and self.M >self.fM): break
                self.times.append((self.H,self.M))
                self.M+=self.increment
                if self.M >= 60:self.H+=1;self.M-=60
            return self.bus, self.times
    #Schedules

    SCMMF, SciHillMF, CedWaMF, HighLaurMF, BayMisMF = [],[],[],[],[]
    MF = [SciHillMF,SCMMF,CedWaMF,HighLaurMF, BayMisMF]

    #10
    SCMMF.append(Timetabler((7,45),(18,45),60,10).getTimes())
    SCMMF.append(Timetabler((12,15),(19,15),60,10).getTimes())
    CedWaMF.append(Timetabler((7,17),(19,17),30,10).getTimes())
    HighLaurMF.append(Timetabler((7,23),(19,23),30,10).getTimes())
    SciHillMF.append(Timetabler((7,39),(19,39),30,10).getTimes())
    HighLaurMF.append(Timetabler((7,50),(19,50),30,10).getTimes())

    #15
    SCMMF.append(Timetabler((7,15),(19,45),15,15).getTimes())
    BayMisMF.append(Timetabler((7,21),(13,51),30,15).getTimes())
    BayMisMF.append(Timetabler((14,6),(17,6),30,15).getTimes())
    BayMisMF.append(Timetabler((14,21),(19,51),30,15).getTimes())
    SciHillMF.append(Timetabler((7,33),(20,3),30,15).getTimes())
    SciHillMF.append(Timetabler((14,18),(17,18),30,15).getTimes())
    BayMisMF.append(Timetabler((7,43),(8,13),30,15).getTimes())
    BayMisMF.append(Timetabler((14,58),(17,28),30,15).getTimes())

    #16
    SCMMF.append(Timetabler((6,37),(22,7),30,16).getTimes())
    SCMMF.append(Timetabler((6,52),(20,22),30,16).getTimes())
    BayMisMF.append(Timetabler((6,43),(22,13),30,16).getTimes())
    BayMisMF.append(Timetabler((6,58),(20,28),30,16).getTimes())
    SciHillMF.append(Timetabler((6,55),(24,25),15,16).getTimes())
    BayMisMF.append(Timetabler((7,5),(21,5),15,16).getTimes())
    BayMisMF.append(Timetabler((22,5),(23,35),30,16).getTimes())

    #19
    SCMMF.append(Timetabler((7,25),(17,55),30,19).getTimes())
    SCMMF.append(Timetabler((18,25),(23,25),60,19).getTimes())
    BayMisMF.append(Timetabler((8,32),(18,2),30,19).getTimes())
    BayMisMF.append(Timetabler((18,32),(23,32),60,19).getTimes())
    SciHillMF.append(Timetabler((8,44),(18,14),30,19).getTimes())
    SciHillMF.append(Timetabler((18,44),(23,44),60,19).getTimes())
    BayMisMF.append(Timetabler((8,54),(18,24),30,19).getTimes())
    BayMisMF.append(Timetabler((18,54),(23,54),60,19).getTimes())

    SciHillSS,SCMSS,CedWaSS,HighLaurSS,BayMisSS = [],[],[],[],[]
    SS = [SciHillSS,SCMSS,CedWaSS,HighLaurSS,BayMisSS]

    #10
    SciHillSS.append(Timetabler((10, 8), (17, 8), 60, 10).getTimes())
    SCMSS.append(Timetabler((9, 50), (16, 50), 60, 10).getTimes())
    CedWaSS.append(Timetabler((9, 52), (16, 52), 60, 10).getTimes())
    HighLaurSS.append(Timetabler((9, 57), (16, 57), 60, 10).getTimes())
    HighLaurSS.append(Timetabler((10, 15), (17, 15), 60, 10).getTimes())
    SCMSS.append(Timetabler((10, 30), (17, 30), 60, 10).getTimes())

    #16
    SCMSS.append(Timetabler((8, 10), (9, 40), 30, 16).getTimes())
    SCMSS.append(Timetabler((10, 7), (12, 37), 30, 16).getTimes())
    SCMSS.append(Timetabler((13, 4), (17, 34), 30, 16).getTimes())
    SCMSS.append(Timetabler((15, 20), (18, 20), 60, 16).getTimes())
    SCMSS.append(Timetabler((18, 7), (23, 7), 30, 16).getTimes())
    BayMisSS.append(Timetabler((8, 15), (23, 15), 30, 16).getTimes())
    SciHillSS.append(Timetabler((8, 25), (23, 25), 30, 16).getTimes())
    BayMisSS.append(Timetabler((8,35), (23,35), 30, 16).getTimes())

    #19
    SCMSS.append(Timetabler((10, 0), (19, 0), 60, 19).getTimes())
    BayMisSS.append(Timetabler((10, 7), (19, 7), 60, 19).getTimes())
    SciHillSS.append(Timetabler((10, 19), (19, 19), 60, 19).getTimes())
    BayMisSS.append(Timetabler((10, 29), (19, 29), 60, 19).getTimes())
    
    def timetable_generator(MF):
        for a in MF:
            for b in a:
                for c in b:
                    if b.index(c) == 0: print("Bus ", c, end = "\t")
                    else:
                        for d in c:
                            x, y = d
                            if len(str(y)) == 1: y = "0" + str(y)
                            print("{}:{}".format(x, y), end = " ")
                    print("")
    
    """print("Monday-Friday")
    timetable_generator(MF)
    print("\nSaturday-Sunday")
    timetable_generator(SS)"""
    return render_template('index.html')


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
