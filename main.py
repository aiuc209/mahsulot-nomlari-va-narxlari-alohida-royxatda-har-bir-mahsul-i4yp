mahsulot_nomi = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
mahsulot_narxi = [10000, 5000, 20000, 15000, 12000]

cheqirma = 0.15
yangi_narxlar = [narx * (1 - cheqirma) for narx in mahsulot_narxi]

for i in range(len(mahsulot_nomi)):
    print(f"{mahsulot_nomi[i]}ning yangi narxi: {yangi_narxlar[i]}")
