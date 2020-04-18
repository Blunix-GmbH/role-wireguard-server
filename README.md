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
systemctl enable wg-quick@wg0.service
systemctl start wg-quick@wg0.service
```


# Client setup (other operating systems)

- Install wireguard
- Generate a keypair
- Provide the `public.key` content to the wireguard server administrator over a secure channel
- Receive the client config from the admin
- Install the client config

Client config file example `/etc/wireguard/wg0.conf`:
```
[Interface]
Address = 10.0.0.5/32
#ListenPort = 12345
# client private key
PrivateKey = @@@secret-private-key@@@
# use wireguard server as dns server
#dns = 10.0.0.1

[Peer]
# server public key
PublicKey = @@@public-key@@@
Endpoint = serverIP:serverPort
PersistentKeepalive = 10

# regular VPN
AllowedIPs = 10.0.0.0/24, 172.16.0.0/24
# forward all traffic
AllowedIPs = 0.0.0.0/0, ::/0
```

Generate client certificate:
```
cd /etc/wireguard
wg genkey | tee client_private_key | wg pubkey > client_public_key
chmod 400 *
```

Start the client:
```
wg-quick up wg0
```

Monitor the connection:
```
watch sudo wg show
```

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
