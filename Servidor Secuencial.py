import socket
import time

def iniciar_servidor():
    # Creamos un socket TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8000))
    server_socket.listen(5)
    
    print("Servidor SECUENCIAL escuchando en el puerto 8000...")

    while True:
        # El servidor se bloquea aquí esperando un cliente
        client_socket, addr = server_socket.accept()
        print(f"Conexión recibida de {addr}")

        # SIMULACIÓN DE CARGA PESADA DE DATOS 
        print("Procesando datos pesados (10s)...")
        time.sleep(10) 
        
        client_socket.send(b"Respuesta del servidor: Proceso completado.\n")
        client_socket.close()
        print(f"Conexión con {addr} cerrada.")

if __name__ == "__main__":
    iniciar_servidor()