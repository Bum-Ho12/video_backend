Steps:
1. clone repository.
2. run pip install -r requirements.txt
3. run python manage.py makemigrations
4. run python manage.py migrate
5. runserver.
6. urls (videos/urls.py) are:
   - videos list html http://127.0.0.1:8000.
   - video details html http://127.0.0.1:8000/<id>/
   - video upload html http://127.0.0.1:8000/upload/
   - videos list api http://127.0.0.1:8000/api/videos/
   - video details api http://127.0.0.1:8000/api/videos/<id>/
   - vidoe upload api http://127.0.0.1:8000/api/videos/upload/
