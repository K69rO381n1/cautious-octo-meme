import os
with open('self_path.txt','w') as f:
    f.write(os.path.split(os.path.abspath('a'))[0])