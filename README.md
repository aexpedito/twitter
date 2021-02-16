# aws, repository
http://ec2-3-129-20-171.us-east-2.compute.amazonaws.com:8080
https://github.com/aexpedito/twitter

# Create twitter keys
https://developer.twitter.com/
-- keys stored in .profile and .env file

# Looked for some sentiment analysis
https://textblob.readthedocs.io/en/dev/quickstart.html#sentiment-analysis
https://pypi.org/project/twitter-nlp-toolkit/ ->tried this but used to much memory

# created env
>apt-get update
>apt-get install -y python3
>apt-get install -y python3-pip python3-venv virtualenv tmux
>apt-get install -y htop

# setup virtual env
>$ virtualenv venv
>$ source ./venv/bin/activate
>$ pip3 install -r requirements.txt
>$ pip3 install -U textblob
>$ python3 -m textblob.download_corpora
>$ export FLASK_APP=twitter.py
>$ pip3 install gunicorn
>$ deactivate
>$ set .profile file with Twitter credentials or .env
>$ gunicorn -b 0.0.0.0:8080 -w 2 twitter:app --daemon

# notes 
>$ pkill -f gunicorn

# docker 
docker build -t twitter:1.0 .
docker run -p 8080:8080 -d twitter:1.0

docker build --build-arg https_proxy=https://genproxy.corp.amdocs.com:8080 --build-arg http_proxy=http://genproxy.corp.amdocs.com:8080 -t twitter .