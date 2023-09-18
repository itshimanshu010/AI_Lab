print("Rule of This Game")
print("Rule 1 : there is one missionarie B1 to B2")
print("Rule 2 : there is two missionarie B1 to B2")
print("Rule 3 : there is one cannibal and missionarie B1 to B2")
print("Rule 4 : there is one cannibal B1 to B2 ")
print("Rule 5 : there is two cannibal B1 to B2 ")
print("Rule 6 : there is one missionarie B2 to B1")
print("Rule 7: there is two missionarie B2 to B1")
print("Rule 8: there is one cannibal and missionarie B2 to B1")
print("Rule 9: there is one cannibal B2 to B1")
print("Rule 10: there is two cannibal B2 to B1")


mis1=3;

can1=3;

mis2=0;

can2=0;



bord1 = 2;

bord2 = 2;



while(mis2!=3 or can2!=3):
  rno = int(input("Enter Rule"))
  
  if(rno == 1):
    mis1 = mis1 - 1;
    mis2 = mis2 + 1;
    print(mis1,mis2)
    
  
  elif(rno == 2):
    mis1 = mis1 - 2;
    mis2 = mis2 + 2;
    print(mis1,mis2)

  elif(rno == 3):
    mis1 = mis1 - 1;
    can1 = can1 - 1;
    mis2 = mis2 + 1;
    can2 = can1 + 1;
    print(mis1,can1)
    print(mis2,can2)

  elif(rno == 4):
    can1 = can1 - 1;
    can2 = can2 + 1;
    print(can1,can2)
    

  elif(rno == 5):
    can1 = can1 - 2;
    can2 = can2 + 2;
    print(can1,can2)

  elif(rno == 6):
    mis1 = mis1 + 1;
    mis2 = mis2 - 1;
    print(mis1,mis2)

  elif(rno == 7):
    mis1 = mis1 + 2;
    mis2 = mis2 - 2;
    print(mis1,mis2)

  elif(rno == 8):
    mis1 = mis1 + 1;
    can1 = can1 + 1;
    mis2 = mis2 - 1;
    can2 = can1 - 1;
    print(mis1,can1)
    print(mis2,can2)

  elif(rno == 9):
    can1 = can1 + 1;
    can2 = can2 - 1;
    print(can1,can2)


  elif(rno == 10):
    can1 = can1 + 2;
    can2 = can2 - 2;
    print(can1,can2)

  
  if((mis1>0 and mis1<can1) or (mis2>0 and mis2<can2)):
    break;

  
  




