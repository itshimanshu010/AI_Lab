x=0
y=0

m=4
n=3

while x<=2: 
 rno = int(input("Enter Rule"))
 if rno == 1:
  if x < 4:
      x=4;

 
 elif rno == 2:
  if y > 3:
      y=3;


 elif rno == 3:
   if y > 0:
      y=0;

 elif rno == 4:
  if (x+y)<=4 and y>0:
    y=y-(x-3);

 elif rno == 5:
  if (x+y)>=3 and x>0:
    x=x-(3-y);

 elif rno == 6:
  if (x+y)<=4 and y>0:
    x=x+y;

 elif rno == 7:
  if (x+y)<=3 and x>0:
    y=x+y;  



  
 print(x,y)
