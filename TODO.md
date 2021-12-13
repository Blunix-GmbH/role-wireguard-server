# in templates/etc/wireguard/client.conf.j2, why doesn't this work?
Endpoint   = {{ hostvars[wireguard_server]['wireguard_server_public_ip'] }}:{{ hostvars[wireguard_server]['wireguard_server_port'] }}

says it can not find wireguard_server_public_ip and wireguard_server_public_port
