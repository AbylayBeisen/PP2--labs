#ex1
import os
path = 'path/to/directory'
dirs = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
print(dirs)
files = [name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]
print(files)
all_items = os.listdir(path)
print(all_items)
#ex2
import os

path = '/path/to/check'

print('Existence:', os.path.exists(path))
print('Readability:', os.access(path, os.R_OK))
print('Writability:', os.access(path, os.W_OK))
print('Executability:', os.access(path, os.X_OK))
#ex3
import os

path = 'g:\\testpath\\a.txt'

if os.path.exists(path):
    print(f"The file {os.path.basename(path)} exists in the directory {os.path.dirname(path)}")
else:
    print(f"The file {os.path.basename(path)} does not exist in the directory {os.path.dirname(path)}")