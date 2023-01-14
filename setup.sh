apt-get install python3
pip install -r requirements.txt
chmod +x main.py
DIR="/data/data/com.termux/files/usr/bin"
if [[ -d "$DIR" ]];
then
       cp main.py "$DIR"/yt5
else
       cp main.py /usr/bin/yt5
fi

echo '[*] yt5 installed successfully!'
sleep 2  && clear
yt5 -h   