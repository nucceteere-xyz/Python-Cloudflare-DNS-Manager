## What is this?
This is a Python script for adding DNS records to your domain connected to CloudFlare.
### How does it work?
It takes your inputs in accordance to the record you want to create, and then makes a request to CloudFlare API with your Zone ID and your CloudFlare API key.
## Usage
> [!CAUTION]
> Main branch is for use with dedicated environments.<br/>
> For use with local environments, see the local branch.
### Dedicated Environments
Run `git clone -b main https://github.com/nucceteere-xyz/Python-Cloudflare-DNS-Manager.git`<br/>

After that, you need to set 2 enviroment variables
1. ZONE_ID This will be your CloudFlare zone ID
2. API_KEY This will be your CloudFlare API key<br/>
After you do these, make sure that your env variables are set up correctly by running `env_check.py`.
### Local Enviroments
Run `git clone -b local https://github.com/nucceteere-xyz/Python-Cloudflare-DNS-Manager.git`

After that, create a .env file in the working directory.<br/>
Inside of the .env file should look like this:
```.env
ZONE_ID=YOUR_CLOUDFLARE_ZONE_ID
API_KEY=YOUR_CLOUDFLARE_API_KEY
```
After you do these, make sure that your env variables are set up correctly by running `env_check.py`.

[repl.it](https://replit.com/@EngurRuzgar/Python-Cloudflare-DNS-Manager#main.py)<br/>
[GitHub](https://github.com/nucceteere-xyz/Python-Cloudflare-DNS-Manager)<br/>
