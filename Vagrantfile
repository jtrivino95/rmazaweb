# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  # config.vm.network "private_network", ip: "10.0.0.10"
  # config.vm.synced_folder "../data", "/vagrant_data"
  config.vm.provision :shell, :path => "vagrant/provision.sh"
  # config.ssh.forward_agent = true
end
