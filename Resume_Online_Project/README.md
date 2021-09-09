# Resume Online - Mickael Lemieux

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">Goal of this project</a>
    </li>
    <li>
          <a href="#Plan-of-the-project">Plan of this project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#execution">Execution</a></li>
      </ul>
    </li>
    <li><a href="#route">Route</a></li>
    <li><a href="#version">version</a></li>
    <li><a href="#heroku">Heroku</a></li>
    <li><a href="#dockerhub">DockerHub</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## Goal of this project
i was only trying to create a Online Resume of myself with some new techno like :

- Flask
- Python3
- Heroku
- Docker

This resume will talk about : 

- Presentation 
- Experiences
- schools
- Skill

i could use "Frozen-Flask if this was an static page about my resume but i choosed to create a Back-End about my current status linked with a BDD

A second page will talk about the mood / news.
___
## Plan of the project
\
![](https://i.ibb.co/w7BNTXf/Untitled-Workspace.png)

\
This project will be linked with a second container which contain MySQL configured with Docker-compose and will be used to maintain a short "blog" on the status page.
___

## Prerequisites
WEB LINK : 
- Having a web browser compatible with HTML5

LOCAL USE :
 - Python3
 - Flask
 - CLI (Bash / Shell / PowerShell)
 - MySQL
___
## Execution
```
python3 app.py
```

You can now check the project on Local with "http://0.0.0.0:5000/"
___

## Route

I actually have only 2 differents route

### The first one is about the main page called "Index"
```
@app.route('/')
def index():
    return render_template('index.html')
```

### and the second one about the current mood
```
@app.route('/status')
def status():
    return render_template('status.html')
```

More route could come in future..
___

## Version
- Flask : 1.1.2

- Python : 3.8.10

- Docker : 20.10.6

- MySQL : X.X.X
___

## Heroku

### Link
* https://resume-online-hygon.herokuapp.com/

### Logs Heroku

```
-----> Building on the Heroku-20 stack
-----> Determining which buildpack to use for this app
-----> Python app detected
-----> No Python version was specified. Using the buildpack default: python-3.9.7
       To use a different version, see: https://devcenter.heroku.com/articles/python-runtimes
-----> Installing python-3.9.7
-----> Installing pip 20.2.4, setuptools 47.1.1 and wheel 0.36.2
-----> Installing SQLite3
-----> Installing requirements with pip
       Collecting Flask==1.1.2
         Downloading Flask-1.1.2-py2.py3-none-any.whl (94 kB)
       Collecting Werkzeug>=0.15
         Downloading Werkzeug-2.0.1-py3-none-any.whl (288 kB)
       Collecting Jinja2>=2.10.1
         Downloading Jinja2-3.0.1-py3-none-any.whl (133 kB)
       Collecting itsdangerous>=0.24
         Downloading itsdangerous-2.0.1-py3-none-any.whl (18 kB)
       Collecting click>=5.1
         Downloading click-8.0.1-py3-none-any.whl (97 kB)
       Collecting MarkupSafe>=2.0
         Downloading MarkupSafe-2.0.1-cp39-cp39-manylinux2010_x86_64.whl (30 kB)
       Installing collected packages: Werkzeug, MarkupSafe, Jinja2, itsdangerous, click, Flask
       Successfully installed Flask-1.1.2 Jinja2-3.0.1 MarkupSafe-2.0.1 Werkzeug-2.0.1 click-8.0.1 itsdangerous-2.0.1
-----> Discovering process types
       Procfile declares types -> (none)
-----> Compressing...
       Done: 52.6M
-----> Launching...
       Released v3
       https://resume-online-hygon.herokuapp.com/ deployed to Heroku

```

## Used template
* https://startbootstrap.com/theme/resume
___
## DockerHub
* https://hub.docker.com/repository/docker/hygon/online-resume

___
## Contact
- mickael.lemieux@outlook.com