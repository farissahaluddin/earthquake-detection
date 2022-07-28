def ekstrak_data():
    """
    Tangggal : 28 Juli 2022
    Waktu : 02:17:36 WIB
    Magnitudo : 4.1
    Kedalaman : 10 km
    Lokasi : 8.20 LS - 115.50 BT
    Pusat Gempa : Pusat gempa berada di darat 16 km barat laut Karangasem
    Dirasakan : Dirasakan (Skala MMI): II Karangasem
    :return:
    """

    data_gempa = dict()
    data_gempa['tanggal'] = '28 Juli 2022'
    data_gempa['waktu'] = '02:17:36 WIB'
    data_gempa['magnitudo'] = '4.1'
    data_gempa['kedalaman'] = '10 km'
    data_gempa['lokasi'] = '8.20 LS - 115.50 BT'
    data_gempa['pusat'] = 'Pusat gempa berada di darat 16 km barat laut Karangasem'
    data_gempa['dirasakan'] = 'Dirasakan (Skala MMI): II Karangasem'
    return data_gempa

def show_data(result):
    print('Data Gempa terakhir BMKG :')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi {result['lokasi']}")
    print(f"Pusat Gempa {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")