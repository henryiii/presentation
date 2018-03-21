# LHCb Presentation setup
# cookiecutter https://gitlab.cern.ch/hschrein/lhcb_presentation

from __future__ import print_function

import subprocess
import os

subprocess.check_call(['git', 'init'])
subprocess.check_call(['git', 'submodule', 'add', '{{cookiecutter.remote}}'])
subprocess.check_call(['git', 'submodule', 'update', '--init'])
os.symlink('lhcb_presentation/makeslides.py', 'makeslides.py')
os.symlink('lhcb_presentation/lhcb.beamer', 'lhcb.beamer')
subprocess.check_call(['git', 'add', '.'])
subprocess.check_call(['git', 'reset', '.gitlab-ci.yml'])
subprocess.check_call(['git', 'commit', '-m', 'Initial commit of {{cookiecutter.directory_name}}'])

print()
print("Add .gitlab-ci.yml to get automatic tex builds on gitlab.")
print("")
print("If you are on the same server as lhcb_presentation, update your .gitmodule file to use a relative address.")
print("")
print("Run:")
print("  git remote add origin <MY_REPO_ADDRESS>")
print("  git push -u origin master")
