
## Clone
    git clone https://github.com/michelleNunes/ArtistAPI.git

## Python version

    >= Python 3.8 version

## Python dependencies

    pip install -r requirements.txt

## Start Redis server
    Download redis-server in the link: 
    https://github.com/re757575/myHubot/tree/master/redis-2.4.5-win32-win64
    unzip the file, then execute redis-server.exe and redis-cli.exe

## Install AWS CLI
    Download AWSCLIV2.msi in awshttps://aws.amazon.com/pt/cli/
    If you have the AWS CLI installed, then you can use the aws configure command to configure your credentials file:

    aws configure
    Alternatively, you can create the credentials file yourself. By default, its location is ~/.aws/credentials. At a minimum, the credentials file should specify the access key and secret access key. In this example, the key and secret key for the account are specified the default profile:

    [default]
    aws_access_key_id = YOUR_ACCESS_KEY
    aws_secret_access_key = YOUR_SECRET_KEY

## URL
    To access the code, enter with the localhost IP, the Artist and the Cache
    EX: http://192.168.1.106:5000/music/Evanescence/false