mkdir $1
cd $1
git init
git submodule add ssh://git@gitlab.cern.ch:7999/hschrein/lhcb_presentation.git
cp lhcb_presentation/presentation_temlpate.tex "$1.tex"

