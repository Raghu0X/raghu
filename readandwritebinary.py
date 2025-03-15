def write_binary_file(filename, data):
    
    with open(filename, 'wb') as file:
       
        file.write(data)
        print(f"Data written to {filename}.")

def read_binary_file(filename):
    
    with open(filename, 'rb') as file:
        
        data = file.read()
        print(f"Data read from {filename}: {data}")
        return data
def main():
  binary_data = b'\x01\x02\x03\x04\x05\x06'
  write_binary_file('example.bin', binary_data)
  read_binary_file('example.bin')

if __name__ == "__main__":
    main()
