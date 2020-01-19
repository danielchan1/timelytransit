class timeTabler {
    constructor(start, end, increment, bus, stopName) {
        this.start = start;
        this.end = end;
        this.increment = increment;
        this.bus = bus;
        this.stopName = stopName;
        this.times = new Array();
        while (this.start <= this.end) {
            this.times.push(this.start);
            this.start += this.increment;
            
        }
    }

    addMoreTimes(s, e, inc) {
        while (s <= e) {
            this.times.push(this.s);
            s += e;
        }

        this.times.sort();
    }

    getBusName() {
        return this.bus;
    }

    getStopName() {
        return this.stopName;
    }

    findClosestTimes(time) {
        var closestTime = null;
        for (i = 0; i < this.times.length; i++) {
            if (closestTime == null || ((this.times[i] - time) < closestTime)) {
                closestTime = this.times[i];
            }
        }
        return closestTime;
    }

}

SHMF10 = new timeTabler(459, 1185, 60, 'Bus 10', 'Science Hill');
SCMMF10 = new timeTabler(465, 1125, 60, 'Bus 10', 'Santa Cruz Metro Center');
SCMMF10.addMoreTimes(735, 1155, 60);
CWMF10 = new timeTabler(437, 1157, 30, 'Bus 10', 'Cedar & Walnut');
HLMF10 = new timeTabler(443, 1163, 30, 'Bus 10', 'High & Laurel');
HLMF10.addMoreTimes(470, 1190, 30);

SCMMF15 = new timeTabler(435, 1185, 15, 'Bus 15', 'Santa Cruz Metro Center');
BMMF15 = new timeTabler(446, 831, 30, 'Bus 15', 'Bay & Mission');
BMMF15.addMoreTimes(846, 1026, 30);
BMMF15.addMoreTimes(861, 1191, 30);
SHMF15 = new timeTabler(473, 1203, 30, 'Bus 15', 'Science Hill');
BMMF15.addMoreTimes(463, 493, 30);
BMMF15.addMoreTimes(898, 1048, 30);

SCMMF16 = new timeTabler(397, 1327, 30, 'Bus 16', 'Santa Cruz Metro Center');
SCMMF16.addMoreTimes(472, 1222, 30);
BMMF16 = new timeTabler(463, 1333, 30, 'Bus 16', 'Bay & Mission');
BMMF16.addMoreTimes(478, 1228, 30);
SHMF16 = new timeTabler(475, 25, 15, 'Bus 16', 'Science Hill');
BMMF16.addMoreTimes(425, 1265, 15);
BMMF16.addMoreTimes(1325, 1415, 30);

SCMMF19 = new timeTabler(445, 1075, 30, 'Bus 19', 'Santa Cruz Metro Center');
SCMMF19.addMoreTimes(1105, 1405, 60);
BMMF19 = new timeTabler(512, 1082, 30, 'Bus 19', 'Bay & Mission');
BMMF19.addMoreTimes(1112, 1412, 60);
SHMF19 = new timeTabler(524, 1094, 30, 'Bus 19', 'Science Hill');
SHMF19.addMoreTimes(1124, 1424, 60);
BMMF19.addMoreTimes(534, 1104, 30);
BMMF19.addMoreTimes(1134, 1434, 60);

SHSS10 = new timeTabler(608, 1028, 60, 'Bus 10', 'Science Hill');
SCMSS10 = new timeTabler(590, 1010, 60, 'Bus 10', 'Santa Cruz Metro Center');
CWSS10 = new timeTabler(592, 1012, 60, 'Bus 10', 'Cedar & Walnut');
HLSS10 = new timeTabler(597, 1017, 60, 'Bus 10', 'High & Laurel');
HLSS10.addMoreTimes(615, 1035, 60);
SCMSS10.addMoreTimes(630, 1050, 60);

SCMSS16 = new timeTabler(490, 580, 30, 'Bus 16', 'Santa Cruz Metro Center');
SCMSS16.addMoreTimes(607, 757, 30);
SCMSS16.addMoreTimes(784, 1054, 30);
SCMSS16.addMoreTimes(110, 1100, 60);
SCMSS16.addMoreTimes(1087, 1387, 30);
BMSS16 = new timeTabler(495, 1395, 30, 'Bus 16', 'Bay & Mission');
SHSS16 = new timeTabler(505, 1405, 30, 'Bus 16', 'Science Hill');
BMSS16.addMoreTimes(515, 1415, 30);

SCMSS19 = new timeTabler(600, 1140, 60, 'Bus 19', 'Santa Cruz Metro Center');
BMSS19 = new timeTabler(607, 1147, 60, 'Bus 19', 'Bay & Mission');
SHSS19 = new timeTabler(619, 1159, 60, 'Bus 19', 'Science Hill');
BMSS19.addMoreTimes(629, 1169, 60);

MF = [
        SCMMF10, 
        SCMMF15, 
        SCMMF16, 
        SCMMF19, 
        SHMF10, 
        SHMF15, 
        SHMF16, 
        SHMF19, 
        BMMF15, 
        BMMF16, 
        BMMF19, 
        CWMF10
    ]

SS = [
        SCMSS10,
        SCMSS16,
        SCMSS19,
        SHSS10,
        SHSS16,
        SHSS19,
        BMSS16,
        BMSS19,
        CWSS10,
    ]