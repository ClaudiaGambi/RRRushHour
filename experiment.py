import time 
import subprocess 

start = time.time()
n_runs = 0

while time.time() - start < 600:
         print(f'run: {n_runs}')
         subprocess.call(["python3", "main.py", "-algo", "BF_NearExit" ,"output.csv", "gameboards/Rushhour9x9_5.csv"])
         
         n_runs += 1