from threading import Thread
import subprocess


def get_ping(host):
    return subprocess.Popen(["ping", "-c", "1", "-n", host]).communicate()


hosts = ["google.com", "yandex.ru", "mail.ru", "vk.com", "bing.com"]

threads = [Thread(target = get_ping, args = (host,)) for host in hosts]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
