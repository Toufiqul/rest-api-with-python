# contributing
## running dockerfile locally 
```
sudo docker build -t flask-smorest-api .

sudo docker run -p 5000:5000 -w /app -v "$(pwd):/app" flask-smorest-api
```