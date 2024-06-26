import socket
import timeit

def measure_response_time(server_host, server_port, query, num_iterations=100):
    """
    Measure the average response time of sending a query to the server multiple times.

    Args:
        server_host (str): The server's host.
        server_port (int): The server's port.
        query (str): The query string to send.
        num_iterations (int): The number of iterations to perform.

    Returns:
        float: The average response time in seconds.
    """
    def single_request():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((server_host, server_port))
            client_socket.sendall(query.encode('utf-8'))
            response = client_socket.recv(1024).decode('utf-8')
            return response

    # Time the execution of the single_request function
    total_time = timeit.timeit(single_request, number=num_iterations)
    average_time = total_time / num_iterations
    return average_time

if __name__ == '__main__':
    server_host = 'localhost'
    server_port = 12345
    query = 'hello'
    num_iterations = 100
    avg_response_time = measure_response_time(server_host, server_port, query, num_iterations)
    print(f'Average response time over {num_iterations} iterations: {avg_response_time:.6f} seconds')
