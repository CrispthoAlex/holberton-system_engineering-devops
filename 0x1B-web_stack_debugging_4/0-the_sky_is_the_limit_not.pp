# Increase the limit of HTTP requests to a web server

exec { 'fix-nginx-config':
command  => "sed -i 's/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/' /etc/default/nginx",
provider => shell,
}

exec { 'restart-nginx':
command  => 'service nginx restart',
provider => shell,
require  => Exec['fix-nginx-config'],
}