import os, wget, time, requests, hashlib
from nslookup import Nslookup
from os.path import exists
#python sublist3r.py -v -d example.com -o ../list-subdomains
word_clear_and_delete_duplicated = 'sed -i s/www.//g list-subdomains && sort list-subdomains | uniq -u > list-subdomain-finish'
os.system(word_clear_and_delete_duplicated)

# Nslookup Constructor
dns_query = Nslookup()
dns_query = Nslookup(dns_servers=['8.8.8.8'], verbose=False, tcp=False)

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


file_subdomain = open('list-subdomain-finish', 'r')
Lines = file_subdomain.read().splitlines()

for line in Lines:
    ips_record = dns_query.dns_lookup(line)
    time.sleep(3)
    if len(ips_record.answer) == 0:
        print('404: FAIL ', line)
    elif (requests.get('https://'+line)).status_code == 401:
        print('401: NO-AUTH', line)
        print('\n')
    else:
        print('200: OK ',line)
        link = 'https://'+line
        if os.path.exists('files/'+line):
            print('deleting file repeat')
            os.remove('files/'+line)
            print('downloading ', line)
            wget.download(link, 'files/'+line)
            print('\n')
            print('MD5: ', md5('files/'+line), line, '\n')
            #md5('files/'+line)
            print('\n')
        else:
            print('Success '+line)
            wget.download(link, 'files/'+line)
            print('MD5: ', line, md5('files/'+line),'\n')
            time.sleep(3)
