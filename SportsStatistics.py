import numpy as np 
import pandas as pd
data=np.random.randint(0,100,(11,11))
print("The data of cricket runs:",data)
player=["M.S.Dhoni","Virat kholi","Rohit Sharma","Shubman Gill","K.L.Rahul","Shreyas Iyer","Hardik Pandya","Ravindra Jadeja","Rishabh Pant","Jasprit Bumrah","Mohammed Siraj"]
match=["Match1","Match2","Match3","Match4","Match5","Match6","Match7","Match8","Match9","Match10","Match11"]
table=pd.DataFrame(data,index=match,columns=player)
playertotal=data.sum(axis=0)
print("Total runs per player",playertotal)
matchtotal=data.sum(axis=1)
print("Total runs per match",matchtotal)
playeraverage=data.mean(axis=0)
print("Average score per player:",playeraverage)
best=playertotal.max()
indplayer=np.argmax(playertotal)
bestplayer=player[indplayer]
print("The best-performing player:",bestplayer)
bestm=matchtotal.max()
indmatch=np.argmax(matchtotal)
bestmatch=match[indmatch]
print("The highest overall score:",bestmatch)
p_per=(playertotal / playertotal.sum())*100
print("Percentage of each player",p_per)
