# Eventex

Sistema de Eventos encomendados pela Morena.

## Como desenvolver?

1. Clone um repósitorio.
2. Crie um virtualenv com Python 3.8.10
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone git@github.com:pabloaugmat/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test

```


## Como fazer o deploy?

1. heroku.