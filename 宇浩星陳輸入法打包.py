# %%

from datetime import datetime
# version = datetime.today().strftime('%Y%m%d')
import shutil
import os
from distutils.dir_util import copy_tree
from distutils.dir_util import remove_tree
from shutil import copyfile

version = "v3.2.0"

#%%
for _ in range(2):
    try:
        remove_tree("./dist/yustar")
    except:
        pass

#%%
os.makedirs("./dist/yustar")

#%%
# Copy yustar
shutil.copyfile("./image/yustar.png", f"./dist/yustar/yustar_{version}.png")
shutil.copyfile("./beta/readme.md", f"./dist/yustar/readme.txt")
copy_tree("./beta/mabiao/", "./dist/yustar/mabiao/")
copy_tree("./beta/schema/", "./dist/yustar/schema/")
copy_tree("./beta/hotfix/", "./dist/yustar/hotfix/")

#%%
# copy yuhao
copy_tree("../yuhao/beta/schema/lua/", "./dist/yustar/schema/lua/")
for file_name in [
    "default.yaml",
    "key_bindings.yaml",
    "punctuation.yaml",
    "rime.lua",
    "symbols_yuhao.yaml",
    "symbols.yaml",
    "yuhao_pinyin.dict.yaml",
    "yuhao_pinyin.schema.yaml",
    "yuhao/yuhao.extended.dict.yaml",
    "yuhao/yuhao.private.dict.yaml",
    # "yuhao/yuhao.symbols.dict.yaml",
]:
    copyfile(f"../yuhao/beta/schema/{file_name}", f"./dist/yustar/schema/{file_name}")

# %%
shutil.make_archive(f"./dist/yuhao_star_{version}", 'zip', "./dist/yustar")
# %%
copyfile(f"./dist/yuhao_star_{version}.zip", f"../yuhao/dist/yuhao_star_{version}.zip")
copyfile(f"./dist/yuhao_star_{version}.zip", f"../yuhao/dist/宇浩星陳_{version}.zip")
# %%
