import psycopg2
import urllib.parse as urlparse
import os

url = urlparse.urlparse(os.environ['postgres://vcoeytqsykvquy:da3ec31136524582d9a2d15da762ce5fcf28d3af0df2ed750ad3c23355e9f209@ec2-107-20-141-145.compute-1.amazonaws.com:5432/d73epgrslvjlg7'])
dbname = url.path[1:]
user = url.username
password = url.password
host = url.hostname
port = url.port

con = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
)
