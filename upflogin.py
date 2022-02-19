import requests
from bs4 import BeautifulSoup as bs
import urllib3


requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
try:
    requests.packages.urllib3.contrib.pyopenssl.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
except AttributeError:
    print('ERRO DE SSL')
    pass
user = str(input('Usuário: '))
password = str(input('Senha: '))

with requests.Session() as s:

    login_data = {"f_login": "logar", "f_usuario": user, "f_senha": password}
    s.post("https://secure.upf.br/apps/login.php", login_data, verify=False)
    home_page = s.get("https://secure.upf.br/apps/academico/aluno/atualiza_dados.php", verify=False)
    print(home_page.content)
