#!/bin/bash
git pull heroku master
git add --all
git commit -m ‘push’
git push heroku master
git push origin master -f