#After Provision

1. curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
1. sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
1. sudo apt-get update
1. sudo apt-get install docker-ce docker-ce-cli containerd.io build-essential git
