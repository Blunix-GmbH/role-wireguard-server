import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('bullseye1')


def test_client_reachable(host):
    command = host.run("ping -c 1 172.128.0.5")
    assert command.rc == 0
