# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from ms_active_directory import ADDomain
import argparse

def discover_domain(domainName):

   domain_dns_name = domainName
   domain = ADDomain(domain_dns_name)
   ldap_servers = domain.get_ldap_uris()
   kerberos_servers = domain.get_kerberos_uris()
   print("Count of the ldap servers for " + domain_dns_name +": " +  str(len(ldap_servers)))
   print("Count of the kerberos servers for " + domain_dns_name + ": " + str(len(ldap_servers)))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Domain lookup examples
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--domain", help="AD domain name")

    args = parser.parse_args()
    if args.domain:
        discover_domain(args.domain)


