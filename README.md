# Presentation style (with CookieCutter)

This template provides a beamer style file, a beamer module, and a [Pandoc] template to use for making beautiful presentations simply. It is customized slightly for UC, but that is easy to replace with different branding.

## Quick setup

Get going fast with [cookiecutter]. Just use `pip install cookiecutter` to get the [cookiecutter] application. Then, run:

```bash
cookiecutter gh:henryiii/presentation
```
You will be asked a few questions. Make sure you do not add an extension to `file_name`; it will do that for you. You can select either LaTeX (`tex`) or Markdown via [Pandoc] (`md`) as the `type`.
It will make a new git repository, and check this repository out as a submodule. The basics will be prepared for you.


## Customization

The following is the built-in support for branding, you can customize it for your University (use `newcommmand` or `renewcommand` as necessary, in the style files `providecommand` is used):

```tex
\newcommand{\logomax}{\node [right] at (0,1.143) {\includegraphics[height=1.3cm]{logos/UC_logo_bb.pdf}};}
\newcommand{\logomini}{\node at (1,1.143/2) {\includegraphics[height=.75cm]{logos/UC_logo_bb.pdf}};}
\newcommand{\logowidth}{2.5}
```

To remove it:

```tex
\newcommand{\logomax}{}
\newcommand{\logomini}{}
\newcommand{\logowidth}{0}
```

## Builds

You can run `./makeslides.py` if you have Plumbum (and Pandoc) installed, and all `.md` or `.tex` files will be processed if out of date. If the names match, the `.md` file takes preference.

## Gitlab builds

If you use GitLab, you can use the CI system to build your PDFs for you. An example file for builds is included when you make a new presentation, and the output is available at `https://gitlab.cern.ch/<user>/<reponame>/builds/artifacts/master/file/<file_name>.pdf?job=compile_pdf`.

You might need a relative path or HTTPS path in `.gitmodules` to build (see [this page](https://docs.gitlab.com/ce/ci/git_submodules.html)). This is because GitLab CI uses HTTP(S) for all cloning. You'll get that option when the [cookiecutter] runs.


[cookiecutter]:   https://cookiecutter.readthedocs.io/en/latest/
[Pandoc]:         https://pandoc.org
