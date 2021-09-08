# Resume Online - Mickael Lemieux

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">Goal of this project/a>
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
    <li><a href="#link">Link</a></li>
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
___

## Prerequisites
WEB LINK : 
- Having a web browser compatible with HTML5

LOCAL USE :
 - Python3
 - Flask
 - CLI (Bash / Shell / PowerShell)
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
___

## Link
* https://mickael-flaskapp.herokuapp.com/

## Used template
* https://startbootstrap.com/theme/resume

___
## Contact
- mickael.lemieux@outlook.com