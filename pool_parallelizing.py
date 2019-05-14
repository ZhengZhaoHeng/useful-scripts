# Author: Zhaoheng Zheng
# zhaoheng.zheng@usc.edu
# Process Pool script for multi processing

from multiprocessing import Pool
import subprocess
import os
import time

def run(img_file, group_id):
    
    if os.path.exists('locks/{}.lock'.format(group_id)):
        return
    if os.path.exists('locks/{}.done'.format(group_id)):
        return
    os.makedirs('locks/{}.lock'.format(group_id))
    subprocess.call(cmd, shell=True)
    os.makedirs('locks/{}.done'.format(group_id))
    os.rmdir('locks/{}.lock'.format(group_id))

pool = Pool(5)

img_lists = os.listdir('img_lists')

for img_file in img_lists:
    if '.txt' not in img_file: 
        continue
    group_id = img_file[-12:-4]
    pool.apply_async(run, (os.path.join('img_lists', img_file), group_id, ))

pool.close()
pool.join()
    
