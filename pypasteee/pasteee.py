import requests

from .paste import Paste, Section



class Pasteee:
    def __init__(self, token: str) -> None:
        assert Pasteee.verifyToken(token), 'ERROR: Ivalid API token provided'
        self.token = token

        self.session = requests.Session()
        self.session.headers = {'X-Auth-Token': self.token}

        


    def getPastesList(self, perpage: int = 25, page: int = 1) -> list[Paste]:
        data = {
            'perpage': perpage,
            'page': page
        }


        response = self.session.get('https://api.paste.ee/v1/pastes', params=data)
        data = response.json()['data']
        

        pastes = []
        for i in data:
            pastes.append(Paste(id=i['id'], encrypted=False, description=i['description'], views=i['views'], created_at=i['created_at']))
        return pastes
        
    def getPaste(self, id: str) -> Paste | None:
        response = self.session.get(f'https://api.paste.ee/v1/pastes/{id}')
        if response.status_code == 404:
            return None

        data = response.json()['paste']
        sections = [Section(syntax=i['syntax'], name=i['name'], content=i['contents'], size=i['size']) for i in data['sections']]
        return Paste(id=data['id'], encrypted=data['encrypted'], description=data['description'], sections=sections, views=data['views'], 
                    created_at=data['created_at'], expires_at=data['expires_at'])


    def getPastesCount(self) -> int:
        response = self.session.get(f'https://api.paste.ee/v1/pastes/{id}')
        return int(response.json()['total'])


    def paste(self, paste: Paste) -> str:
        assert paste.sections != [] and paste.sections != None, 'ERROR: Section list cant be empty'


        headers = {
            'Content-Type': 'application/json',
            'X-Auth-Token': self.token,
        }

        data = {
            'description': paste.description,
            'encrypted': paste.encrypted,
            'sections': [{
                'name': i.name,
                'syntax': i.syntax,
                'contents': i.content
                } for i in paste.sections
            ]
        }


        response = self.session.post('https://api.paste.ee/v1/pastes', headers=headers, json=data).json()
        assert response['success'], f'ERROR: {response['errors'][0]['message']}'
        return response['link']


    def deletePaste(self, id: str) -> None:
        self.session.delete(f'https://api.paste.ee/v1/pastes/{id}')


    def getSyntaxes(self) -> list[str]:
        response = self.session.get('https://api.paste.ee/v1/syntaxes')
        return [i['short'] for i in response.json()['syntaxes']] 



    @staticmethod
    def verifyToken(token: str) -> bool:
        response = requests.get('https://api.paste.ee/v1/users/info', headers={'X-Auth-Token': token}).json()
        if response.get('type') == 'Application':
            return False

        return response['success']

