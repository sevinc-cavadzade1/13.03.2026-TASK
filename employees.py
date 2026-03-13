import sqlite3

def layiheni_baslat():
    # 1.Database
    connection = sqlite3.connect('shirket_arxivi.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Isciler (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ad_soyad TEXT NOT NULL,
            maash REAL NOT NULL,
            department TEXT NOT NULL
        )
    ''')

    def isci_elave_et(ad, maash, dep):
        # Validation
        if maash < 0:
            print(f"Xəta: {ad} üçün daxil edilən maaş ({maash}) mənfi ola bilməz!")
            return
        
        cursor.execute('INSERT INTO Isciler (ad_soyad, maash, department) VALUES (?, ?, ?)', (ad, maash, dep))
        connection.commit()
        print(f"Sistem: {ad} ({dep} şöbəsi) uğurla qeydiyyata alındı.")

    isciler = [
        ("Eli Memmedov", 450, "İnsan Resursları"),
        ("Leyla Eliyeva", 1200, "İT"),
        ("Anar Veliyev", -100, "Maliyyə"),
        ("Gunay Hesenzade", 850, "İT"),
        ("Fuad Qasimov", 550, "Marketinq")
    ]

    for ad, maash, dep in isciler:
        isci_elave_et(ad, maash, dep)

    # 3.Business Logic
    print("\n--- 500 AZN-dən yuxarı maaş alanlar (Şöbə ilə birgə) ---")
    cursor.execute('''
        SELECT ad_soyad, department, maash FROM Isciler 
        WHERE maash > 500 
        ORDER BY maash DESC
    ''')
    
    for setir in cursor.fetchall():
        print(f"İşçi: {setir[0]} | Şöbə: {setir[1]} | Maaş: {setir[2]} AZN")

    # 4.Output
    cursor.execute('SELECT MIN(maash), MAX(maash), AVG(maash) FROM Isciler')
    min_m, max_m, orta_m = cursor.fetchone()

    print("\n" + "="*40)
    print("YEKUN STATİSTİKA")
    print(f"Minimum Maaş: {min_m} AZN")
    print(f"Maksimum Maaş: {max_m} AZN")
    print(f"Orta Maaş: {round(orta_m, 2)} AZN")
    print("="*40)

    connection.close()

if __name__ == "__main__":
    layiheni_baslat()