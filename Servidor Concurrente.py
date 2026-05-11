import socket
import threading
import time

def manejar_cliente(client_socket, addr):
    print(f"[HILO] Iniciando atención para {addr}")
    # SIMULACIÓN DE CARGA PESADA
    time.sleep(10)
    client_socket.send(b"Respuesta del servidor concurrente: Completado.\n")
    client_socket.close()
    print(f"[HILO] Finalizado para {addr}")

def iniciar_servidor():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8000))
    server_socket.listen(5)
    
    print("Servidor CONCURRENTE (Multihilo) escuchando en el puerto 8000...")

    while True:
        client_socket, addr = server_socket.accept()
        # Creamos un hilo nuevo para cada cliente
        hilo = threading.Thread(target=manejar_cliente, args=(client_socket, addr))
        hilo.start() # El hilo corre de forma independiente
        # El bucle principal vuelve inmediatamente a 'accept()' para el siguiente cliente

if __name__ == "__main__":
    iniciar_servidor()