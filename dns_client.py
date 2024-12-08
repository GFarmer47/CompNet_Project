import dns.resolver

resolver = dns.resolver.Resolver()
resolver.nameservers = ['192.168.1.104']

domain = 'www.google.com'

answers = resolver.resolve(domain, 'A')
for rdata in answers:
    print(f"{domain} has address {rdata.address}")
