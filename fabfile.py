from fabric.api import run, env, parallel, settings, quiet



#env.use_ssh_config = True

env.gateway = 'noor2'

env.hosts = ["gpu%02i" % i for i in range(38)]

env.skip_bad_hosts = True


#@parallel
def check_gpu():
    uname = run("lscpu | grep -i vendor", quiet=True, warn_only=True)
    out = run("lspci | grep -i Tesla", quiet=True, warn_only=True)


    #nvsmi = run("nvidia-smi | grep Tesla", quiet=True, warn_only=True)
    #nvdriver = run("nvidia-smi | grep Driver", quiet=True, warn_only=True)

    for i in out.split('\n'):
        print env.host, uname.split()[2], i.split()[5], i.split()[7][:-1]

