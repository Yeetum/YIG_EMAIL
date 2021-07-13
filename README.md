# YIG Send Email Program
## Initialize config.py for runtime

### Setup YIG Email Program
```bash
git clone https://github.com/Yeetum/atlas-email-services.git
cd YIG_EMAIL
pip install -r requirements.txt
```

### Initialize config.py for runtime
```python
USER_SMTP = 'SMTP User'
PASSWORD_SMTP = 'SMTP Password'
SENDER = 'Sender Email'
SENDERNAME = 'Sender Name'
SMTP_SERVER = 'SMTP Server'
SMTP_PORT = 'SMTP port'
SG_API_KEY = 'Send Grid Key'
```

### Initialize testRecepients.txt and prodRecepients.txt
```
test@test.com
test2@test.com
test3@test.com
```

```
prod@prod.com
prod2@prod.com
prod3@prod.com
```

### Run test program
```bash
python index.py FILEPATH TEST_RECEPIENTS_TXT_FILE SUBJECT_STRING
```

### Run production program
```bash
python index.py FILEPATH PROD_RECEPIENTS_TXT_FILE SUBJECT_STRING
```
# TODO
## Add customer as recepient through txt file
