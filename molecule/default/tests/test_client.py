import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('bullseye2')


def test_server_reachable(host):
    command = host.run("ping -c 1 172.128.0.1")
    assert command.rc == 0


def test_etc_resolv_conf(host):
    f = host.file("/etc/resolv.conf")
    assert f.contains("nameserver 172.128.0.1")
