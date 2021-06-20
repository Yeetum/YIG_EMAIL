# YIG Send Email Program
## Initialize config.py for runtime

### Setup YIG Email Program
```bash
git clone https://github.com/Yeetum/FUMaaS_EMAIL.git
cd FUMaaS_EMAIL
pip install -r requirements.txt
```

### Initialize config.py for runtime
```python
USER_SMTP = 'SMTP User'
PASSWORD_SMTP = 'SMTP Password'
SENDER = 'Sender Email'
SENDERNAME = 'Sender Name'

RECEPIENT = ['recepient1', 'recepient2', 'etc']
SMTP_SERVER = 'SMTP Server'
SMTP_PORT = 'SMTP port'
SG_API_KEY = 'Send Grid Key'
```

### Run program
```bash
python send_YIG_Email.py FILEPATH
```
# TODO
## Add customer as recepient through txt file