rows=int(input("Enter Diamond Pattern Rows="))
print ("Diamond Star Pattern")
for i in range (1,row+1):
  for j in range(1,row-i+1):
      print(end='')
  for k in range(0,2*1-1):
      print('*',end ='')
  print ()
for i in range (1,rows):
      for j in range(1,i+1):
          print (end='')
      for i in range(1,(2*(row-i))):
          print('*',end='')
      print()
