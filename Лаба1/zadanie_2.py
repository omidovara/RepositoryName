# TODO Найдите количество книг, которое можно разместить на дискете
disk_volume_mb = 1.44  # объем дискеты в Мб
pages_in_book = 100     # количество страниц в книге
lines_per_page = 50     # количество строк на странице
chars_per_line = 25     # количество символов в строке
bytes_per_char = 4      # байты для хранения одного символа
disk_volume_bytes = disk_volume_mb * 1024 * 1024 #Мб в байты
total_chars_in_book = pages_in_book * lines_per_page * chars_per_line #количество всего символов в книге
book_volume_bytes = total_chars_in_book * bytes_per_char #объём данных в книге
number_of_books =round( disk_volume_bytes /book_volume_bytes) #количество одинаковых книг, помещающихся на дискету


print("Количество книг, помещающихся на дискету:", number_of_books)
