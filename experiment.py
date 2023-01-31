import time 
import subprocess 

start = time.time()
n_runs = 0

while time.time() - start < 600:
         print(f'run: {n_runs}')
         subprocess.call(["python3", "main.py", "-algo", "A_Star" ,"output.csv", "gameboards/Rushhour6x6_1.csv"])
         
         n_runs += 1