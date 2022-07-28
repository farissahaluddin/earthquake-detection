"""
Earthquake detection
"""
from earthquake_latest import ekstrak_data, show_data

if __name__ == '__main__':
    print('Aplikasi Utama')
    result = ekstrak_data()
    show_data(result)