Template project for running ants on Heroku
===========================================

Overview
--------


Language support
----------------
This template runs the python Ants TCP client, and can run a bot in another language that is supported on Heroku. The requirement is that there must exist a Heroku buildpack for that language.

In the .buildpacks file the buildpacks must be listed. Since python is used for the tcp client, it must be included in the .buildpacks.



Setup
-----
The boot script takes the ant server password from ENV, so it must be set thusly:

    heroku config:set ANT_SERVER_PASSWORD=mypassword

In the connectAndPlay.sh, change:

 * BOT_COMMAND: this command will be executed in a subprocess, running your bot
 * ANT_SERVER_USER: the username you will be listed as on the Ants TCP server


The Heroku app must be configured for multi-buildpack:

    heroku config:set BUILDPACK_URL=https://github.com/ddollar/heroku-buildpack-multi.git

If your bot is written in anything else than python, a buildpack for your language must be added to the .buildpacks file.


Heroku issues
-------------



