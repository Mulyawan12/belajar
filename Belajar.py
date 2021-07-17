#!/usr/bin/sh


blue='\033[34;1m'
green='\033[32;1m'
purple='\033[35;1m'
cyan='\033[36;1m'
red='\033[31;1m'
white='\033[37;1m'
yellow='\033[33;1m'


user="p"
while [ "$username" != "$user" ]
do
    read -p "masukan username: " username
clear
figlet tools gabut berfaedah
done
    echo    $green"selamat datang"
    echo  $cyan"[•].new coding"
    echo  $red"[•].new coding simple"
    echo  $purple"[•].bikin nama v.1"
    echo  $red"[•].bikin nama v.2"
    echo  $cyan"[•].keluar/exit"
    
    echo $yellow"note:jika muncul teks merah itu teks penting"
read -p "pilih (1/2/3/4/5): " pil
if [ $pil = "1" ]
then
    nano hanz.py
elif [ $pil = "2" ]
then
    termux-setup-storage
    echo $red"masukan cd /sdcard/(nama file)"
    echo $cyan"contoh cd /sdcard/belajar"
    echo $green"nanti kalian salin ini buat command pertama supaya script nya jadi (#!/usr/bin/sh)"
    echo $cyan"salin yang di dalam kurung"
elif [ $pil = "3" ]
then
    pkg install toilet
    echo $red"contoh (toilet hanz)"
elif [ $pil = "4" ]
then
    pkg install figlet
    echo $red"contoh(figlet hanz)"
elif [ $pil = "5" ]
then
    echo "keluar"
else
    echo "imput salah..."
    sh belajar.sh
    
fi