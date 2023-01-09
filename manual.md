x_dir/texts/no$tes;1.txt i y2_dir/notes2.txt-> duplikaty
x_dir/scripts/main_cash.tmp + y2_dir/documents/another_cash.tmp - tymczasowy 
y1_dir/recordings/empty_file.txt - pusty
x_dir/the_same_name.txt i y2_dir/the_same_name.txt - ta sama nazwa, niech zostanie nowszy
x_dir/texts/no$tes;1.txt i y1_dir/images/tux:2.txt - błędna nazwa

X_dir
-> scripts
----> hello_world.py - ZOSTAJE
----> main_cash.tmp - DO USUNIĘCIA (tmp)
-> texts
----> no$tes;1.txt - zmiana znaków
the_same_name.txt - ta sama nazwa (1)

Y1_dir
-> images
----> books.jpg - ZOSTAJE
----> tux:1.png - zmiana nazwy
-> recordings
----> empty_file.txt - DO USUNIĘCIA (pusty)
----> rec1.md - ta sama zawartość (2)
----> rec2.md - ta sama zawartość (2)
notes2.txt - ZOSTAJE

Y2_dir
-> documents
----> another_cash.tmp  - DO USUNIĘCIA (tmp)
----> essay.docs - ZOSTAJE
sample_video.gif - ZOSTAJE
the_same_name.txt - ta sama nazwa (1)

python3 sort_files.py /home/jan/studia/ASU/projekt/X_dir /home/jan/studia/ASU/projekt/Y1_dir /home/jan/studia/ASU/projekt/Y2_dir