# Set up client SSH configuration file, so can connect to a server without a password
file_line { 'Turn off passwd auth':
ensure => 'present',
path   => '/etc/ssh/ssh_config',
line   => 'PasswordAuthentication no',
}

file_line { 'Declare identity file':
ensure => 'present',
path   => '/etc/ssh/ssh_config',
line   => 'IdentityFile ~/.ssh/holberton',
}
