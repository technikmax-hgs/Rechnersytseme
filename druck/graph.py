#!/usr/bin/python3

import rrdtool
filename1 = "/home/gruppe2/temperatur1.rrd"
filename2 = "/home/gruppe2/temperatur2.rrd" 

ret = rrdtool.graph('-' ,
             '--imgformat', 'PNG' ,
             '--width',' 640' ,
             '--height', '300',
             '--start','-1hour' ,
             '--end',' now' ,
             '--vertical-label', "Grad Celsius" ,
             '--alt-autoscale',
             '--title',' Temperatur',
             'DEF:temp1='+filename1+':temp1:AVERAGE',
	     'DEF:temp2='+filename2+':temp2:AVERAGE',		
             'LINE1:temp1#000000:Temperatur DS18B20' ,
	     'LINE1:temp2#00FFFF:Temperatur BMP_280' ,
             'GPRINT:temp1:MIN:Min\\:  %3.2lf C '  ,
             'GPRINT:temp1:MAX:Max\\: %3.2lf C  ' ,
             'GPRINT:temp1:AVERAGE:Avg\\: %3.2lf C ' ,
             'GPRINT:temp1:LAST:Aktuell\\: %3.2lf C ' ,
	     'GPRINT:temp2:MIN:Min\\:  %3.2lf C '  ,
             'GPRINT:temp2:MAX:Max\\: %3.2lf C  ' ,
             'GPRINT:temp2:AVERAGE:Avg\\: %3.2lf C ' ,
             'GPRINT:temp2:LAST:Aktuell\\: %3.2lf C ')
