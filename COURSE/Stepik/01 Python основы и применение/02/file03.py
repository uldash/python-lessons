import os
import os.path

print(os.getcwd())
print(os.listdir())
print(os.path.exists('file03.py'))
print(os.path.exists('../02'))

print(os.path.isfile('file03.py'))
print(os.path.isfile('../02'))

print(os.path.isdir('file03.py'))
print(os.path.isdir('../02'))

print(os.path.abspath('file03.py'))

for current_dir, dirs, files in os.walk('.'):
    print(current_dir, dirs, files)
