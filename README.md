# pypasteee

A simple Python wrapper for the [paste.ee](https://paste.ee/)  


## Instalation 
```
pip install pypasteee
```


## Usage

Initialization
```python
from pypasteee import Pasteee, Paste, Section

api = Pasteee(API_TOKEN)
```


Get a list of your pastes
```python
...
pastes = api.getPastesList()
for i in pastes:
    print(f'ID: {i.id}. Description: {i.description}. Views: {i.views}. Created at: {i.created_at}')
```


Get paste info
```python
...
pastes = api.getPaste('<id>')
```

Create a new paste
```python
...

new_paste = Paste(description='First paste from pypasteee', encrypted=False, sections=[Section(syntax="autodetect", name='Section1', content='Feels great')]) 
api.paste(new_paste)
```

Delete paste
```python
...
api.deletePaste('<id>')
```



