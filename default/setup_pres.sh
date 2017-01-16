def_dir="lhcb_presentation/default"

mkdir $1
cd $1
git init
git submodule add ssh://git@gitlab.cern.ch:7999/hschrein/lhcb_presentation.git
cp $def_dir/presentation_temlpate.tex "$1.tex"
cp $def_dir/gitignore .gitignore
echo "$1.pdf" >> .gitignore
sed s/default/$1/g < $def_dir/gitlab-ci.yml > .gitlab-ci.yml
