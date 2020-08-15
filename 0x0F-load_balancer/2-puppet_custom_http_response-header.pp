# Install and configure an Nginx server and Add a custom HTTP header

# install nginx
package { 'nginx':
ensure  => installed,
}

# Add custom HTTP header
file_line { 'Custom HTTP header':
ensure => 'present',
after  => 'listen 80 default_server',
path   => '/etc/nginx/sites-available/default',
line   => 'add_header X-Served-By \$HOSTNAME;',
}

# Restar nginx to apply change
service { 'nginx':
ensure  => running,
require => package['nginx'],
}