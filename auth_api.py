import hashlib  #Libreria del hash_sha1()
import secrets  #Libreria para generar valor aleatorio alfanumerico nonce
import base64  #Libreria para codificar en Base64
from datetime import datetime, timedelta  #Libreria para importar la fecha actual

login = ''
secretKey = ''
auth = {
  'login': login,
}
nonce = secrets.token_urlsafe()
nonceBase64 = base64.b64encode(nonce.encode('utf-8')).decode()
seed = datetime.now()
cifrado = hashlib.sha256(
  (nonce + seed.isoformat() + secretKey).encode('utf-8')).digest()
tranKey = base64.b64encode(cifrado).decode()
auth['nonce'] = nonceBase64
auth['tranKey'] = tranKey
auth['seed'] = seed.isoformat()
minutes = timedelta(minutes=20)
expiration = seed + minutes
print(auth)
