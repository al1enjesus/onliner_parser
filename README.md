# Onliner parser
A Django App that gives you parsed onliner data (At this moment about videocards)
# Requirements
beautifulsoup4==4.9.3  
Django==3.2.1  
fake-useragent==0.1.11  
lxml==4.6.3  
requests==2.25.1  
# Installation
```
git clone https://github.com/al1enjesus/onliner_parser  
cd online_parser
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt   
```
# Initialize database and superuser
```
python manage.py migrate
python manage.py parse
```
Create superuser using **python manage.py createsuperuser**  
# Usage
```
python manage.py runserver
```
---
**Go http://127.0.0.1:8000/admin/ and enter your superuser data**
