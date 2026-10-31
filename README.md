dataset yang digunakan merupakan data yang berisikan tentang spesifikasi dari mobil yang diperjual belikan

kondisi awal dari dataset memiliki kolom sebanyak 30 dan 205 baris yang nama dari kolom datasetnya sebagai berikut
transaction_date,symboling,normalized-losses,make,aspiration,num-of-doors,body-style,drive-wheels,engine-location,wheel-base,length,
width,height,curb-weight,engine-type,num-of-cylinders,engine-size,fuel-system,bore,stroke,compression-ratio,horsepower,peak-rpm,city-mpg,
highway-mpg,price,city-L/100km,horsepower-binned,diesel,gas

permasalahan yang ditemukan dari dataset ini yaitu masih memiliki missing values pada kolom
transaction_date, make, num-of-doors, stroke, horsepower, price, horsepower-binned

data duplikasi sebanyak 4 baris

kolom dengan data format yang tidak konsisten pada kolom
make, body-style, drive-wheels, fuel-system, transaction_date

cleaning yang dilakukan dengan
mengisi data sebelumnya untuk data kolom transaction_date agar mengikuti tanggal dengan semestinya
kolom make dengan "" karena tipe data string
kolom num-of-doors dengan modus karena data
kolom stroke dengan mean
kolom horsepower dengan mean
kolom price dengan median
