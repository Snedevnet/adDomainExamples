# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from ms_active_directory import ADDomain
import argparse


def discover_domain(domain_name, nameserver_addr=""):

    domain_dns_name = domain_name
    nameserver_addr = nameserver_addr
    dns_name_servers = []
    if nameserver_addr != "":
        dns_name_servers.append(nameserver_addr)
        domain = ADDomain(domain_dns_name, dns_nameservers=dns_name_servers)
    else:
        domain = ADDomain(domain_dns_name)
    ldap_servers = domain.get_ldap_uris()
    kerberos_servers = domain.get_kerberos_uris()
    print("Count of the ldap servers for " + domain_dns_name + ": " + str(len(ldap_servers)))
    print("Count of the kerberos servers for " + domain_dns_name + ": " + str(len(ldap_servers)))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Domain lookup examples
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--domain", help="AD domain name")
    parser.add_argument("-n", "--nameserver", help="Alternative dns server")

    args = parser.parse_args()
    if args.domain is not None and args.nameserver is not None:
        discover_domain(args.domain, args.nameserver)
    elif args.domain is not None:
        discover_domain(args.domain)




