#!/usr/bin/python3

import rrdtool
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
             'DEF:luft1='+filename2+':luft1:AVERAGE',           
             'AREA:luft1#CCCFCC:',
             'LINE1:luft1#000FFF:Temperatur BMP_280' ,
             'GPRINT:luft1:MIN:Min\\:  %3.2lf C '  ,
             'GPRINT:luft1:MAX:Max\\: %3.2lf C  ' ,
             'GPRINT:luft1:AVERAGE:Avg\\: %3.2lf C ' ,
             'GPRINT:luft1:LAST:Aktuell\\: %3.2lf C ')
