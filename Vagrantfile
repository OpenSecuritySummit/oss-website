# -*- mode: ruby -*-
# vi: set ft=ruby :
# Run vagrant up to get started 
Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-16.04"
  config.vm.network "forwarded_port", guest: 1313, host: 1313, host_ip: "127.0.0.1" 
  config.vm.synced_folder ".", "/opt/oss2018"

  config.vm.provider "virtualbox" do |vb|
     vb.memory = "512"
  end

  config.vm.provision "shell", inline: <<-SHELL
    set -x
    apt-get update
    apt-get install -y git curl
    export HUGO_VERSION="0.49"
    export SRC_DIR="/opt/oss2018"
    export THEME_DIR="themes/oss-owasp"

    curl -Ls https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_Linux-64bit.tar.gz -o /tmp/hugo.tar.gz
    tar xf /tmp/hugo.tar.gz -C /usr/local/bin
    mkdir -p $SRC_DIR

    cd $SRC_DIR

    if [ ! -d "$THEME_DIR" ] ; then
       git clone https://github.com/devcows/hugo-universal-theme.git themes/oss-owasp
    else
       cd $THEME_DIR 
       git pull https://github.com/devcows/hugo-universal-theme.git
    fi
    cd "$SRC_DIR"
    hugo server --bind="0.0.0.0"
  SHELL
end
