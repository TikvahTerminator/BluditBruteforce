# BluditBruteforcer

## What is this?
This is a quick bruteforcing tool I wrote to work on the Bludit CMS platform to exploit  [CVE-2019-17240](https://www.cvedetails.com/cve/CVE-2019-17240/ "CVE-2019-17240 security vulnerability details") 
> bl-kernel/security.class.php in Bludit 3.9.2 allows attackers to bypass a brute-force protection mechanism by using many different forged X-Forwarded-For or Client-IP HTTP headers

## How to use?

```console
git clone https://github.com/TikvahTerminator/BluditBruteforce.git
cd BlunderBruteforce
python3 Bludit_Bruteforce.py [Webhost] [Password Wordlist] [Username to try]
```

*This was written to help on a certain box hacking site's machine*
