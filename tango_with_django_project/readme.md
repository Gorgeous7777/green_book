### Deployment project
```shell
git clone https://github.com/Gorgeous7777/green_book.git
cd green_book
virtualenv venv  (create venv)

# source venv\bin\active    (linux/mac)
# venv\bin\active    (windows)

(venv):pip install -r requirements.txt

(venv):python manage.py migrate

(venv):python manage.py runserver 127.0.0.1:8000

# add data,only categorized data will be added. (populate_rango.py:Cancel the addition of page data. Because we modified the model, this script cannot add page data)
python populate_rango.py
```

### Bootstrap
```shell
https://v4.bootcss.com/docs/getting-started/introduction/
```

### Add new html
1. Inherit `block body_block`, then write your page.for example:
    ```html
    {% extends 'rango/base.html' %}
    {% load staticfiles %}
    
    {% block title_block %}
        About Rango
    {% endblock %}
    
    {% block body_block %}
        <p>Visits: {{ visits }}</p>
        <h1>Rango says...</h1>
        <div>here is the about page.</div>
        <div>
            <strong>This tutorial has been put together by wangtuo</strong><br/>
        </div>
    
        <div>
            <img src="{% static 'images/rango.jpg' %}" alt="Picture of Rango"/>
            <img src="{{ MEDIA_URL }}cat.jpg" alt="Picture of a Cat."/>
        </div>
    {% endblock %}
    ```
2. If you don’t want the category bar, then you need to refill the `{% block content_block %}`,for example:
    ```html
    {% extends 'rango/base.html' %}
    {% load staticfiles %}
    
    {% block title_block %}
        About Rango
    {% endblock %}
    
    {% block content_block %}
        <p>Visits: {{ visits }}</p>
        <h1>Rango says...</h1>
        <div>here is the about page.</div>
        <div>
            <strong>This tutorial has been put together by wangtuo</strong><br/>
        </div>
    
        <div>
            <img src="{% static 'images/rango.jpg' %}" alt="Picture of Rango"/>
            <img src="{{ MEDIA_URL }}cat.jpg" alt="Picture of a Cat."/>
        </div>
    {% endblock %}
    ```
    
### Notice
1. New push, do not submit to the `master` branch.(This is the first step in team development.)
    ```shell
    + You should submit to a new branch, such as `dev_by_wangtuo`.
    + To merge the code, you need to submit a `merge` request.
    + How to add a new branch? You can find related buttons in pycharm.Or find related commands in google.
    ```
2. Before writing new code, you should update the code first, for example: `git pull`. (During your break, other people will modify the code. Otherwise, there will be unexpected troubles)