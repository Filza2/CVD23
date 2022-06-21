checkroot() {

if [[ "$(id -u)" -ne 0 ]]; then
   printf "\e[1;77mPlease, run this installer as root!\n\e[0m"
   exit 1
fi

}

checkroot

apt install neofetch
clear
printf "'neofetch' Downloaded successfully !"
python3 installer.py