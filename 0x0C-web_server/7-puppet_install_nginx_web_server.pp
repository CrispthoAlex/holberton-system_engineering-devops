# Install and configure an Nginx server using Puppet instead of Bash

# install nginx
package { 'nginx':
ensure  => installed,
}

# return a page that contains the string Holberton School
file { 'Return a string':
content => 'Holberton School',
path    => '/var/www/html/index.html'
}

# Add 301 Move Permanently
file_line { 'Add 301 Move Permanently':
ensure => 'present',
after  => 'listen 80 default_server',
path   => '/etc/nginx/sites-available/default',
line   => 'rewrite ^/redirect_me https://youtu.be/l9_-2oG4Cc0 permanent;',
}

# Restar nginx to apply change
service { 'nginx':
ensure  => running,
require => package['nginx'],
}