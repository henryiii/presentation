# LHCb Presentation setup
# This script can be obtained from:
# https://gitlab.cern.ch/hschrein/lhcb_presentation/raw/master/default/setup_pres.sh
#
# Source this script with an argument for the name of the presentation (folder) to make
#

def_dir="lhcb_presentation/default"

mkdir $1
cd $1
git init
git submodule add ssh://git@gitlab.cern.ch:7999/hschrein/lhcb_presentation.git

cp $def_dir/presentation_template.tex "$1.tex"
git add "$1.tex"

cp $def_dir/gitignore .gitignore
echo "$1.pdf" >> .gitignore
git add .gitignore

ln -s $def_dir/lhcb.beamer lhcb.beamer
git add lhcb.beamer

cp $def_dir/presentation_template.md "$1.md"
git add "$1.md"

ln -s $def_dir/makeslides.py makeslides.py
git add makeslides.py

sed s/default/$1/g < $def_dir/gitlab-ci.yml > .gitlab-ci.yml

git commit -m "Initial commit of lhcb-presentation"

echo "Add .gitlab-ci.yml to get automatic tex builds on gitlab"
echo "Add a remote and push to setup your repository"
