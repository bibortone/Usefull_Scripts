import requests

def get_subdomains(domain):
    subdomains = set()

    try:
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        response = requests.get(url)
        data = response.json()

        for entry in data:
            subdomains.add(entry['name_value'])

    except Exception as e:
        print(f"Error querying crt.sh: {e}")

    return subdomains

def save_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write('\n'.join(data))

def main():
    domain = input("Enter the domain name: ")
    subdomains = get_subdomains(domain)

    if subdomains:
        print(f"Subdomains for {domain}:")
        for subdomain in subdomains:
            print(subdomain)

        # Save subdomains to a text file
        output_file = 'crt-subdomains.txt'
        save_to_file(output_file, subdomains)
        print(f"Subdomains saved to {output_file}")
    else:
        print(f"No subdomains found for {domain}")

if __name__ == "__main__":
    main()
