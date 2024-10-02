## CLOUDFLARE TOKEN MINER

---

## Description

The bot helps to mining CF response captcha keys. <br>
It allows to avoid using such services as 2captcha / anti-captcha
<br>
it's free and much faster

---

### Docker run
Runs redis which contains captcha response keys with expiry - 2 minutes
<br>
After, The codes automatically delete
<br>
The codes are taken according to the FIFO principle
<br><br>
```TARGET_URL="https://visa.vfsglobal.com/ind/en/nor/login" docker-compose run -d --name vfs cf-miner```
<br><br>
TARGET_URL - specify the site where the captcha should be solved
<br>
--name - name of the container
<br>
cf-miner - name of the service in the docker-compose file

---

### Notes

* You can add several containers for each site
