#!/bin/bash
git add --all
git commit -m ‘push’
git push heroku master
git push -u origin master