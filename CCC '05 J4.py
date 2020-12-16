
# See the symbol table at the bottom of this page.
import sys
Niswanob1=[]
fuscat1=[]
def Chri2():
 for Chri1 in range(len(fuscat1)):
  print (fuscat1[Chri1])


for Niswanob2 in range(5):
 Niswanob1.append(int(input()))

(fuscat2,bitboostdotcom1)=((Niswanob1[2] + 1),1)
Chri4=(['#']*    (Niswanob1[0] + 2))
fuscat1.append(Chri4)
for fuscat3 in range(Niswanob1[1]):
 bitboostdotcom2=(['']*    (Niswanob1[0] + 2))
 for ordemo1 in range((Niswanob1[0] + 2)):
  bitboostdotcom2[ordemo1]='.'

 fuscat1.append(bitboostdotcom2)

fuscat1.append(Chri4)
for Niswanob2 in range(1,(Niswanob1[3] + 1)):
 for bitboostdotcom3 in range(1,(Niswanob1[2] + 1)):
  fuscat1[Niswanob2][bitboostdotcom3]='#'
  fuscat1[Niswanob2][((len(fuscat1[0]) - bitboostdotcom3) - 1)]='#'


for Niswanob2 in range(((len(fuscat1) - Niswanob1[3]) - 1),(len(fuscat1) - 1)):
 for bitboostdotcom3 in range(1,(Niswanob1[2] + 1)):
  fuscat1[Niswanob2][bitboostdotcom3]='#'
  fuscat1[Niswanob2][((len(fuscat1[0]) - bitboostdotcom3) - 1)]='#'


for Niswanob2 in range(len(fuscat1)):
 (fuscat1[Niswanob2][0],fuscat1[Niswanob2][(len(fuscat1[Niswanob2]) - 1)])=('#','#')

Chri3=0
fuscat5=0
fuscat1[bitboostdotcom1][fuscat2]='M'
for Niswanob2 in range(Niswanob1[4]):
 if (fuscat5==0):
  if (fuscat1[bitboostdotcom1][(fuscat2 + 1)]!='#'):
   fuscat1[bitboostdotcom1][fuscat2]='#'
   fuscat2+=1
  elif ((fuscat1[bitboostdotcom1][(fuscat2 + 1)]=='#') and (fuscat1[(bitboostdotcom1 + 1)][fuscat2]!='#')):
   fuscat1[bitboostdotcom1][fuscat2]='#'
   bitboostdotcom1+=1
  else:
   fuscat5=1


 if (fuscat5==1):
  if ((fuscat1[bitboostdotcom1][(fuscat2 - 1)]!='#') and (fuscat1[(bitboostdotcom1 + 1)][fuscat2]=='#')):
   fuscat1[bitboostdotcom1][fuscat2]='#'
   fuscat2-=1
  elif ((fuscat1[bitboostdotcom1][(fuscat2 + 1)]=='#') and (fuscat1[(bitboostdotcom1 + 1)][fuscat2]!='#')):
   fuscat1[bitboostdotcom1][fuscat2]='#'
   bitboostdotcom1+=1
  else:
   fuscat5=2


 if (fuscat5==2):
  if ((fuscat1[bitboostdotcom1][(fuscat2 - 1)]=='#') and (fuscat1[(bitboostdotcom1 - 1)][fuscat2]!='#')):
   fuscat1[bitboostdotcom1][fuscat2]='#'
   bitboostdotcom1-=1
  elif ((fuscat1[bitboostdotcom1][(fuscat2 - 1)]!='#') and (fuscat1[(bitboostdotcom1 + 1)][fuscat2]=='#')):
   fuscat1[bitboostdotcom1][fuscat2]='#'
   fuscat2-=1
  else:
   fuscat5=3


 if (fuscat5==3):
  if ((fuscat1[bitboostdotcom1][(fuscat2 + 1)]!='#') and (fuscat1[(bitboostdotcom1 - 1)][fuscat2]=='#')):
   fuscat1[bitboostdotcom1][fuscat2]='#'
   fuscat2+=1
   None
  elif ((fuscat1[(bitboostdotcom1 - 1)][fuscat2]!='#') and (fuscat1[bitboostdotcom1][(fuscat2 - 1)]=='#')):
   fuscat1[bitboostdotcom1][fuscat2]='#'
   bitboostdotcom1-=1
   None
  else:
   fuscat5=0
   None



fuscat1[bitboostdotcom1][fuscat2]='M'
print (fuscat2)
print (bitboostdotcom1)
Chri2()
