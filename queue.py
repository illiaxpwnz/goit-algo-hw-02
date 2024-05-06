import queue
import time
import random

# Створення черги заявок
request_queue = queue.Queue()

def generate_request():
    request_id = random.randint(1000, 9999)  # Генерація унікального ID для заявки
    print(f"Generating request {request_id}")
    request_queue.put(request_id)  # Додавання заявки до черги

def process_request():
    if not request_queue.empty():
        request_id = request_queue.get()  # Видалення заявки з черги для обробки
        print(f"Processing request {request_id}")
    else:
        print("No requests to process")

# Головний цикл програми
try:
    while True:
        generate_request()
        time.sleep(1)  # Імітація часу на обробку
        process_request()
        time.sleep(1)  # Імітація часу на обробку
except KeyboardInterrupt:
    print("Program terminated by user") # CTRL + C
