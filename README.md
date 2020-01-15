# Role wireguard server

This role installs and configures a wireguard server and creates client configs to be distributed to the clients.

# Example Playbook

Please refer to `molecule/default/playbook.yml` for a comprehensive example.

# Client setup (Debian / Ubuntu)

```
sudo add-apt-repository ppa:wireguard/wireguard
sudo apt-get install wireguard
cd /etc/wireguard
wg genkey | sudo tee private.key | sudo wg pubkey | sudo tee public.key
cat public.key
```

Provide the `public.key` content to the wireguard server administrator over a secure channel.

This role will create client configs on the server that can then be send to the clients over a secure channel. Save it to `/etc/wireguard/wg0.conf`.

Then run
```
wg-quick up wg0
```
or:
```
systemctl start wg-quick@wg0.service
systemctl enable wg-quick@wg0.service
```


# Client setup (other operating systems)

- Install wireguard
- Generate a keypair
- Provide the `public.key` content to the wireguard server administrator over a secure channel
- Receive the client config from the admin
- Install the client config

Further documentation:  
https://www.wireguard.com/install/


# License

Apache-2.0

# Author Information

Service and support for orchestrated hosting environments,
continuous integration/deployment/delivery and various Linux
and open-source technology stacks are available from:

```
Blunix GmbH - Consulting for Linux Hosting 24/7
Glogauer Straße 21
10999 Berlin - Germany

Web: www.blunix.org
Email: service[at]blunix.org
Phone: (+49) 30 / 12 08 39 90
```
