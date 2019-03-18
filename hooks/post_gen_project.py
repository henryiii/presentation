# Presentation setup
# cookiecutter gh:henryiii/presentation

from __future__ import print_function

import subprocess
import os

subprocess.check_call(['git', 'init'])
subprocess.check_call(['git', 'submodule', 'add', '{{cookiecutter.remote}}'])
subprocess.check_call(['git', 'submodule', 'update', '--init'])
os.symlink('presentation/makeslides.py', 'makeslides.py')
os.symlink('presentation/presentation.beamer', 'presentation.beamer')
subprocess.check_call(['git', 'add', '.'])
subprocess.check_call(['git', 'reset', '.gitlab-ci.yml'])
subprocess.check_call(['git', 'commit', '-m', 'Initial commit of {{cookiecutter.directory_name}}'])

print()
print("If you are on the same server as lhcb_presentation, update your .gitmodule file to use a relative address.")
print()
print("Run:")
print("  git remote add origin <MY_REPO_ADDRESS>")
print("  git push -u origin master")
