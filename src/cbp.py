from pathlib import Path

import cbpro
import pprint

key = Path("../api/key.txt").read_text()
b64secret = Path("../api/b64secret.txt").read_text()
passphrase = Path("../api/passphrase.txt").read_text()

auth_client = cbpro.AuthenticatedClient(key, b64secret, passphrase)

print(auth_client.get_account("a317765b-278f-4edf-990a-b257e77a45ef"))
