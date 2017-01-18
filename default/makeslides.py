#!/usr/bin/env python

from __future__ import print_function
from plumbum import local, cli, FG, colors

class Doc(object):
    def __init__(self, filename, ext):
        self.filename = filename
        self.input = filename.with_suffix(ext)
        self.output = filename.with_suffix('.pdf')
        self.name = filename.with_suffix('').basename
    def exists(self):
        return self.input.exists()
    def needs_update(self):
        if not self.output.exists():
            return True
        return self.input.stat().st_mtime > self.output.stat().st_mtime

class MakeSlides(cli.Application):
    'Make slides from all available files in current directory'

    @cli.positional(cli.ExistingFile)
    def main(self, *filenames):
        if not filenames:
            filenames = local.cwd // ('*.mkd', '*.tex')

        for fname in filenames:
            document = Doc(fname, '.mkd')
            if document.exists() and document.needs_update():
                colors.info.print("Making", document.name, "with pandoc")
                local['pandoc']['-t', 'beamer',
                        '--template=lhcb.beamer',
                        document.input,
                        '-o', document.output] & FG
            else:
                document = Doc(fname, '.tex')
                if document.exists() and document.needs_update():
                    colors.info.print("Making", document.name, "with latex")
                    local['latexmk']['-pdf', document.input] & FG

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
