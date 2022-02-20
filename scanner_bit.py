import os
#python sublist3r.py -v -d example.com -o ../list-subdomains
word_clear_and_delete_duplicated = 'sed -i s/www.//g list-subdomains && sort list-subdomains | uniq -u > list-subdomain-finish'

os.system(word_clear_and_delete_duplicated)

file_subdomain = open('list-subdomain-finish', 'r')
Lines = file_subdomain.readlines()

count = 0
for line in Lines:
    count += 1
    print(count, line.strip())
