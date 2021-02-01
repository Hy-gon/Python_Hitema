from joblib import dump, load
from fastapi import FastAPI

app = FastAPI()
clf = load('algo.joblib')
print('StartUp')

def get_categ(name = 'random'):
    """
    Retourne la catégorie d'un projet a partir de son nom
    """
    print(name)
    test_value = [str(name)]
    #print(clf.predict(test_value))
    return str(clf.predict(test_value))[2:-2]
    

@app.get('/')
async def index(name):
    response = get_categ(name)
    print("response = " + response)
    return response
