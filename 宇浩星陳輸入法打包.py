# %%

from datetime import datetime
# version = datetime.today().strftime('%Y%m%d')
import shutil
import os
from distutils.dir_util import copy_tree
from distutils.dir_util import remove_tree

version = "v0.1.2"

#%%
try:
    remove_tree("./dist/yustar")
except:
    pass

#%%
os.makedirs("./dist/yustar")
shutil.copyfile("./image/yustar.png", f"./dist/yustar/yustar_{version}.png")
shutil.copyfile("./beta/readme.md", f"./dist/yustar/readme.txt")
copy_tree("./beta/mabiao", "./dist/yustar/mabiao")
copy_tree("./beta/schema", "./dist/yustar/schema")

shutil.make_archive(f"./dist/yustar_{version}", 'zip', "./dist/yustar")
# %%
# shutil.make_archive(f"./dist/yustar_{version}_hotfix", 'zip', "./beta/hotfix")
# %%
