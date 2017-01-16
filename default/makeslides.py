#!/usr/bin/env python

from __future__ import print_function
from plumbum import local, cli, FG, colors

class MakeSlides(cli.Application):
    'Make slides from all available files in current directory'

    @cli.positional(cli.ExistingFile)
    def main(self, *filenames):
        if not filenames:
            filenames = local.cwd // ('*.mkd', '*.tex')

        names = {name.with_suffix('') for name in filenames}

        for name in names:
            fname = name.with_suffix('.mkd')
            if fname.exists():
                colors.info.print("Making", fname.basename, "with pandoc")
                local['pandoc']['-t', 'beamer',
                        '--template=lhcb.beamer',
                        fname,
                        '-o', name.with_suffix('.pdf')] & FG
            else:
                fname = name.with_suffix('.tex')
                colors.info.print("Making", fname.basename, "with latex")
                if fname.exists():
                    local['latexmk']['-pdf', fname] & FG

        generated = ('*.aux', '*.bcf', '*.fls', '*.idx', '*.ind', '*.lof', '*.lot',
                '*.out', '*.toc', '*.blg', '*.ilg', '*.log',
                'aux.bak', 'idx.bak', 'texput.log', 'texput.aux',
                '*.synctex.gz*', '*.nav', '*.snm',
                '*.fdb_latexmk')


        for gen in generated:
            files = (local.cwd // gen)
            if files:
                for f in files:
                    f.delete()




if __name__ == '__main__':
    MakeSlides()
