# d0x3d-the-website
A website for [d0x3d!]

### Clone repository and work with `source` branch
    git clone git@github.com:d0x3d-the-game/d0x3d-the-game.github.io.git
    cd d0x3d-the-game.github.io
    git fetch origin
    git branch gh-pages origin/main

### Setup conda environment
	conda create --name d0x3d.com python=3
	conda activate d0x3d.com

### Install dependencies
    pip install pelican
    pip install Markdown
    pip install ghp-import
    pip install fontawesome-markdown  # for font-awesome icons

## Running Pelican for development
    # start local server
    make devserver
    # site is viewable at http://localhost:8000/
    # to stop: make stopserver

## Publish
    # You have some changes to the `source` branch
    #   They should be all committed; check with `git status` and commit if any
    #   Now we are about to re-generate the website in a `gh-pages` branch
    # Prep that by getting it up to date:
    git checkout gh-pages
    git pull origin main

    # now, switch back to the `source` branch
    git checkout source

    # now generate the new `output` and use it to update the `gh-pages` branch
    pelican content -o output -s publishconf.py
    ghp-import output

    # now push the local `gh-pages` branch to the remote `main` branch
    git push origin gh-pages:main

    # if you did this wrong, you'll get some type of merge error when
    #    you push gh-pages to the remote master branch and it will
    #    complain that you shoud have done a pull first
