# Website

Content and theme templates for static site generator

The pages and news posts are all markdown files in the content directory. The theme templates are in themes. The site is
generated using pelican, a python based static site generator.

## Developement Enviroment

Install python3, python3-virtualenv

Create a virtual enviroment for pelican.

    mkdir -p ~/virtualenv/pelican
    virtualenv -p python3 pelican

Activate the python virtualenv

    cd ~/virtualenv/pelican
    source bin/activate

Install pelican into the virtualenv

    pip install pelican markdown

Create a directory for the Arch Classroom files

    mkdir projects/archclassroom

Git clone the files from this repository or download them as a zip.
