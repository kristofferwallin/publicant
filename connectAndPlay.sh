TCPCLIENT=tcpclient.py
IP=106.187.94.97 # IP of Ants tcp server
ANT_PORT=2085 # Port for Beginners hill

BOT_COMMAND='python MyBot.py'
ANT_SERVER_USER=Wren
NUM_ROUNDS=-1 # Set to -1 to run infinitely

# The PORT env variable is provided by Heroku
# On Heroku, an app must bind to this port and server HTTP.
python -m SimpleHTTPServer $PORT &

python $TCPCLIENT $IP $ANT_PORT "$BOT_COMMAND" $ANT_SERVER_USER $ANT_SERVER_PASSWORD $NUM_ROUNDS

