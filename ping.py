import subprocess

class Ping:
    def execute(self, ip_address):
        try:
            if ip_address.startswith("192."):
                for _ in range(10):
                    response = subprocess.run(["ping", "-c", "1", ip_address], stdout=subprocess.PIPE)
                    print(response.stdout.decode('latin-1'))  # Usamos 'latin-1' en lugar de 'utf-8'
            else:
                print("La dirección IP no comienza con '192.', la clase Ping no puede funcionar.")
        except UnicodeDecodeError:
            print("Error al decodificar la salida del ping.")

    def executefree(self, ip_address):
        try:
            for _ in range(10):
                response = subprocess.run(["ping", "-c", "1", ip_address], stdout=subprocess.PIPE)
                print(response.stdout.decode('latin-1'))  # Usamos 'latin-1' en lugar de 'utf-8'
        except UnicodeDecodeError:
            print("Error al decodificar la salida del ping.")

class PingProxy:
    def __init__(self):
        self.ping = Ping()

    def execute(self, ip_address):
        if ip_address == "192.168.0.254":
            self.ping.executefree("www.google.com")
        else:
            self.ping.execute(ip_address)

# Ejemplo de uso
if __name__ == "__main__":
    ping_proxy = PingProxy()
    ping_proxy.execute("192.168.0.1")
    ping_proxy.execute("8.8.8.8")
    ping_proxy.execute("192.168.0.254")
