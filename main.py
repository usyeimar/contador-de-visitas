import os

def read_visits():
    if os.path.exists('visits.txt'):
        with open('visits.txt', 'r') as file:
            return int(file.read())
    return 0

def write_visits(count):
    with open('visits.txt', 'w') as file:
        file.write(str(count))

def main():
    visits = read_visits()
    visits += 1
    write_visits(visits)
    print(f"Visitas: {visits}")

if __name__ == "__main__":
    main()
