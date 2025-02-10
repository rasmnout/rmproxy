import socket
import threading
import argparse

def load_replacements(replacements):
    mapping = {}
    if replacements:
        for pair in replacements.split():
            key, value = pair.split("=")
            with open(value, "r", encoding="utf-8") as file:
                mapping[key] = file.read().strip()
    return mapping

def replace_text(data, mapping):
    for key, value in mapping.items():
        if key in data:
            data = data.replace(key, value)
    return data

def handle_client(client_socket, remote_host, remote_port, response_logging, comm_map, in_comm_map):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect((remote_host, remote_port))

    def forward(source, destination, source_ip, destination_ip, label, comm_map):
        while True:
            data = source.recv(4096).decode(errors='ignore')
            if not data:
                break
            modified_data = replace_text(data, comm_map)
            destination.sendall(modified_data.encode())
            if response_logging:
                print(f"{label} {source_ip}> {modified_data}")

    client_ip = client_socket.getpeername()[0]
    client_thread = threading.Thread(target=forward, args=(client_socket, server_socket, client_ip, remote_host, "CLIENT", {}))
    server_thread = threading.Thread(target=forward, args=(server_socket, client_socket, remote_host, client_ip, "SERVER", in_comm_map))

    client_thread.start()
    server_thread.start()

    client_thread.join()
    server_thread.join()

    client_socket.close()
    server_socket.close()

def start_proxy():
    parser = argparse.ArgumentParser()
    parser.add_argument("-listen", required=True, help="Listening address")
    parser.add_argument("-listen-port", type=int, required=True, help="Listening port")
    parser.add_argument("-dst", required=True, help="Destination address")
    parser.add_argument("-dst-port", type=int, required=True, help="Destination port")
    parser.add_argument("-response", action="store_true", help="Enable response logging")
    parser.add_argument("-change-communication", help="Text replacements for server-client communication")
    parser.add_argument("-in-change-communication", dest="in_change_comm", help="Text replacements for server-proxy communication")  # Opravený název argumentu

    args = parser.parse_args()
    comm_map = load_replacements(args.change_communication)
    in_comm_map = load_replacements(args.in_change_comm)

    proxy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy.bind((args.listen, args.listen_port))
    proxy.listen(5)
    print(f"Listening on {args.listen}:{args.listen_port} -> {args.dst}:{args.dst_port}")

    while True:
        client_socket, _ = proxy.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, args.dst, args.dst_port, args.response, comm_map, in_comm_map))
        thread.start()

if __name__ == "__main__":
    start_proxy()
