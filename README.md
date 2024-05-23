# GraphQL_Aliaser
Python script for creating payloads and bruteforce GraphQL using alias.

## Requirements
Python 3.6 or higher

## How it works
Tested with PortSwigger labs: https://portswigger.net/web-security/learning-paths/graphql-api-vulnerabilities/bypassing-rate-limiting-using-aliases/graphql/lab-graphql-brute-force-protection-bypass

```bash
└─$ python Graphql_alias_bruteforcer.py                                                             
usage: Graphql_alias_bruteforcer.py [-h] [--output OUTPUT] file_path username
Graphql_alias_bruteforcer.py: error: the following arguments are required: file_path, username
```

```bash
└─$ python3 Graphql_alias_bruteforcer.py /usr/share/wordlists/fasttrack.txt carlos --output dict.txt
Username: carlos
Wordlist count: 262
Created payload was saved in: dict.txt
```

And now you can copy the complete payload and paste it as a query.
![Request example of the attack](https://github.com/NikNitro/GraphQL_Aliaser/blob/main/Images/request.png?raw=true)

Here we can see the response of the attack:
![Response example of the attack](https://github.com/NikNitro/GraphQL_Aliaser/blob/main/Images/response.png?raw=true)

Now we only need to find any `"success":true`  and use that alias name for getting back the correct password.