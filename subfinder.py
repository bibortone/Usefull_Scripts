import subprocess

def run_subfinder(domain):
    try:
        # Run subfinder and capture the output
        result = subprocess.run(['subfinder', '-d', domain], capture_output=True, text=True, check=True)
        return result.stdout.strip().split('\n')
    except subprocess.CalledProcessError as e:
        print(f"Error running subfinder: {e}")
        return []

def save_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write('\n'.join(data))

def main():
    # Prompt user for a domain name
    domain = input("Enter the target domain: ")

    # Run subfinder
    subdomains = run_subfinder(domain)

    if subdomains:
        # Print subdomains to console
        print(f"Subdomains for {domain}:")
        for subdomain in subdomains:
            print(subdomain)

        # Save subdomains to a text file
        output_file = 'subfinder-subdomains.txt'
        save_to_file(output_file, subdomains)
        print(f"Subdomains saved to {output_file}")
    else:
        print(f"No subdomains found for {domain}")

if __name__ == '__main__':
    main()
