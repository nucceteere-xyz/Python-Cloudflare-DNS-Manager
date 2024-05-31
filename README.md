[<img alt="github" height="56" src="https://cdn.jsdelivr.net/npm/@intergrav/devins-badges@3/assets/cozy/available/github_vector.svg">](https://github.com/nucceteere-xyz/Python-Cloudflare-DNS-Manager)
[<img alt="git" height="56" src="https://cdn.jsdelivr.net/npm/@intergrav/devins-badges@3/assets/cozy/available/git_vector.svg">](https://replit.com/@EngurRuzgar/Python-Cloudflare-DNS-Manager#main.py)

## What is this?
This is a Python script for adding DNS records to your domain connected to CloudFlare.
### How does it work?
It takes your inputs in accordance to the record you want to create, and then makes a request to CloudFlare API with your Zone ID and your CloudFlare API key.<br/>
## Usage
> [!CAUTION]
> We recomend using [Poetry](https://python-poetry.org/), if you dont have poetry, run these commands in your shell
> ```
> pip install requests
> pip install python-dotenv
> ```
Run `git clone -b main https://github.com/nucceteere-xyz/Python-Cloudflare-DNS-Manager.git`

After that, create a .env file in the working directory.<br/>
Inside of the .env file should look like this:
```.env
ZONE_ID=YOUR_CLOUDFLARE_ZONE_ID
API_KEY=YOUR_CLOUDFLARE_API_KEY
```
After you do these, make sure that your env variables are set up correctly by running `env_check.py`.

