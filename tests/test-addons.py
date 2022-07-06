import sh
import yaml

from utils import microk8s_enable, wait_for_pod_state, microk8s_disable


class TestAddons(object):
    def test_colours(self):
        microk8s_enable("colours")
        wait_for_pod_state("", "default", "running", label="app=colours")
        status = yaml.safe_load(sh.microk8s.status(format="yaml").stdout)
        expected = {"colours": "enabled"}
        microk8s_disable("colours")

    def test_grafana(self):
        microk8s_enable("grafana")
        wait_for_pod_state("", "default", "running", label="app=grafana")
        status = yaml.safe_load(sh.microk8s.status(format="yaml").stdout)
        print(status)
        expected = {"grafana": "enabled"}
        microk8s_disable("grafana")
