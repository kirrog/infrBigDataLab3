import hvac


class SecretVaultController:
    def __init__(self):
        self.client = hvac.Client(url='https://localhost:8200')

    def get_db_port(self):
        return self.client.secrets.kv.v1.read_secret('cassandra_port')['data']["port"]

    def get_db_password(self):
        return self.client.secrets.kv.v1.read_secret('cassandra_port')['data']["pw"]

    def get_db_username(self):
        return self.client.secrets.kv.v1.read_secret('cassandra_port')['data']["un"]
