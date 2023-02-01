import time 
import subprocess 

start = time.time()
n_runs = 0

while time.time() - start < 600:
         print(f'run: {n_runs}')
         subprocess.call(["python3", "main.py", "gameboards/Rushhour9x9_5.csv", "-algo", "BF_NearExit" ,"output1.csv", "output2"])
         
         n_runs += 1