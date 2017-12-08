dic = {'red':'stop','orange':'wait','green':'go'}
count = 0
while (1):
  signal = input("enter the signal:")
  if signal  in dic.keys():
      print(dic.get(signal))
      count = count +1
  else:
      break
print("no of signals: ",count)      
        