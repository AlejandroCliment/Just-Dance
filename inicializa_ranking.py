import cv2
fs2 = cv2.FileStorage('ranking.xml', cv2.FileStorage_WRITE)
best1name=''
best2name=''
best3name=''
best1=0
best2=0
best3=0
fs2.write('primero', best1)
fs2.write('segundo', best2)
fs2.write('tercero', best3)
fs2.write('best1name', best1name)
fs2.write('best2name', best2name)
fs2.write('best3name', best3name)