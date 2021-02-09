

{"consumer_key": "pT5KOdDtgnpWWSXeaTQ0sgqoj",
"consumer_secret": "6PkBzvXHnYwT2ItygKzGYJguVdtnrkzhzf4A97wEpSHJ9bcqa3",
"access_token": "112226789-IMqzkzFRZ1ECugsHVOHFTrLuMz6wctLJHk6gs7Ul",
"access_secret": "lOPb9r3F0NBzxTLOdbWek8GcvaOkNeg4bwKv5xD5MVo0H"
}

pip install --upgrade setuptools --proxy http://genproxy:8080
python -m spacy download en_core_web_sm

#create env
>apt-get update
>apt-get install -y python3
>apt-get install -y python3-pip python3-venv virtualenv tmux
>apt-get install -y python3-venv
>apt-get install -y virtualenv
>apt-get install -y tmux
>apt-get install -y htop


#setup virtual env
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
