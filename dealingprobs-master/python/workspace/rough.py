from time import sleep
from tqdm import tqdm
with tqdm(total=100000000000) as pbar:
    for i in range(1000000):
        pbar.update(100000)