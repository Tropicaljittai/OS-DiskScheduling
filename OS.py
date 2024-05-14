def fcfs(initial_position, requests):
    total_head_movements = 0
    position = initial_position
    for request in requests:
        total_head_movements += abs(request - position)
        position = request
    return total_head_movements

def optimized_fcfs(initial_position, requests):
    total_head_movements = 0
    position = initial_position
    requests = sorted(requests)
    for request in requests:
        total_head_movements += abs(request - position)
        position = request
    return total_head_movements

def scan_optimized(initial_position, requests):
    total_head_movements = 0
    requests.sort()
    total_head_movements += (initial_position) 
    total_head_movements += (requests[-1]) 
    return total_head_movements

def scan(initial_position, requests):
    total_head_movements = 0
    position = initial_position
    if initial_position not in requests:
        requests.append(initial_position)
    sorted_requests = sorted(requests)
    index = sorted_requests.index(position)
    for i in range(index, len(sorted_requests)):
        total_head_movements += abs(sorted_requests[i] - position)
        position = sorted_requests[i]
    for i in range(index-1, -1, -1):
        total_head_movements += abs(sorted_requests[i] - position)
        position = sorted_requests[i]
    return total_head_movements


def cscan(initial_position, requests):
    total_head_movements = 0
    if initial_position not in requests:
        requests.append(initial_position)
    requests.sort()
    index = requests.index(initial_position)
    total_head_movements += (4999 - initial_position)
    total_head_movements += 4999 
    total_head_movements += requests[index-1]
    return total_head_movements

def cscan_optimized(initial_position, requests):
    total_head_movements = 0
    position = initial_position
    if initial_position not in requests:
        requests.append(initial_position)
    sorted_requests = sorted(requests)
    index = sorted_requests.index(position)
    for i in range(index, len(sorted_requests)):
        total_head_movements += abs(sorted_requests[i] - position)
        position = sorted_requests[i]
    total_head_movements += 4999 - position
    position = 0
    for i in range(0, index):
        total_head_movements += abs(sorted_requests[i] - position)
        position = sorted_requests[i]
    return total_head_movements


def read_requests_from_file(file_path):
    with open(file_path, 'r') as file:
        requests = [int(line.strip()) for line in file.readlines()]
    return requests

def main():
    import sys
    if len(sys.argv) != 3:
        print("Usage: python disk_scheduling.py <initial_position> <file_path>")
        return
    initial_position = int(sys.argv[1])
    file_path = sys.argv[2]

    requests = read_requests_from_file(file_path)

    print("Task 1:")
    print("FCFS total head movements:", fcfs(initial_position, requests))
    print("SCAN total head movements:", scan(initial_position, requests))
    print("C-SCAN total head movements:", cscan(initial_position, requests))

    sorted_requests = sorted(requests)
    print("\nTask 2:")
    print("FCFS total head movements:", optimized_fcfs(initial_position, sorted_requests))
    print("SCAN total head movements:", scan_optimized(initial_position, sorted_requests))
    print("C-SCAN total head movements:", cscan_optimized(initial_position, sorted_requests))

if __name__ == "__main__":
    main()
