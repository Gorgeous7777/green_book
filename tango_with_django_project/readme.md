### Deployment project
```shell
# source venv\bin\active    (linux/mac)
# venv\bin\active    (windows)

pip install -r requirements.txt

python manage.py migrate

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