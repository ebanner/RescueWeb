# --- Install packages we need ---
package 'python3'
package 'git'
package 'postfix'

# --- Add the data partition ---
#directory '/mnt/data_joliss'

# mount '/mnt/data_joliss' do
#   action [:mount, :enable]  # mount and add to fstab
#   device 'data_joliss'
#   device_type :label
#   options 'noatime,errors=remount-ro'
# end

# --- Set host name ---
include_recipe "python::virtualenv"
include_recipe "python::pip"

python_pip "pyramid" do
  action :install
end

python_pip "pyramid_mailer" do
  action :install
end

python_virtualenv "/home/ubuntu/myapp" do
  interpreter "python3"
  owner "ubuntu"
  group "ubuntu"
  options "--system-site-packages"
  action :create
end

directory "/tmp/private_code/.ssh" do
  owner "ubuntu"
  recursive true
end

cookbook_file "/tmp/private_code/.ssh/id_deploy" do
  source "serverKey"
  owner "ubuntu"
  mode 00400
end

cookbook_file "/tmp/private_code/wrap-ssh4git.sh" do
  source "wrap-ssh4git.sh"
  owner "ubuntu"
  mode 00700
end

git "/home/ubuntu/myapp/teamMurrica" do
  user "ubuntu"
  group "ubuntu"
  destination "/home/ubuntu/myapp/teamMurrica"
  repository "git@cs.potsdam.edu:cis420/teamMurrica.git"
  revision "master"
  ssh_wrapper "/tmp/private_code/wrap-ssh4git.sh"

  action :checkout
end

bash "setup app" do
  user "ubuntu"
  cwd "/home/ubuntu/myapp"
  code <<-EOF
source bin/activate
cd teamMurrica/rescueweb
python setup.py develop
EOF
end

bash "populate" do
  user "ubuntu"
  cwd "/home/ubuntu/myapp"
  code <<-EOF
source bin/activate
cd teamMurrica/rescueweb
../../bin/initialize_rescueweb_db development.ini
EOF
  not_if "test -e /home/ubuntu/myapp/teamMurrica/rescueweb/rescueweb.sqlite"
end

bash "halt app" do
  user "ubuntu"
  cwd "/home/ubuntu/myapp"
  code <<-EOF
source bin/activate
cd teamMurrica/rescueweb
sudo killall -9 pserve
EOF
  only_if "pgrep pserve"
end

bash "start app" do
  user "ubuntu"
  cwd "/home/ubuntu/myapp"
  code <<-EOF
source bin/activate
cd teamMurrica/rescueweb
../../bin/pserve development.ini  
EOF
end

