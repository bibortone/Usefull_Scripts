import subprocess

def run_amass(domain):
    try:
        # Run amass and capture the output
        result = subprocess.run(['amass', 'enum', '-d', domain], capture_output=True, text=True, check=True)
        return result.stdout.strip().split('\n')
    except subprocess.CalledProcessError as e:
        print(f"Error running amass: {e}")
        return []

def save_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write('\n'.join(data))

def main():
    # Prompt user for a domain name
    domain = input("Enter the target domain: ")

    # Run amass
    subdomains = run_amass(domain)

    if subdomains:
        # Print subdomains to console
        print(f"Subdomains for {domain}:")
        for subdomain in subdomains:
            print(subdomain)

        # Save subdomains to a text file
        output_file = 'amass-subdomains.txt'
        save_to_file(output_file, subdomains)
        print(f"Subdomains saved to {output_file}")
    else:
        print(f"No subdomains found for {domain}")

if __name__ == '__main__':
    main()
