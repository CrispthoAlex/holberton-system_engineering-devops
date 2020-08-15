# Install and configure an Nginx server and Add a custom HTTP header

# install nginx
package { 'nginx':
ensure  => installed,
}

# Add custom HTTP header
file_line { 'Custom_HTTP_header':
ensure  => 'present',
after   => 'listen 80 default_server',
path    => '/etc/nginx/sites-available/default',
line    => "add_header X-Served-By ${hostname};",
require => Package['nginx'],
}

# Restart nginx to apply change
service { 'nginx':
ensure  => running,
require => File_line['Custom_HTTP_header'],
}