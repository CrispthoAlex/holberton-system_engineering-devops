# Set up client SSH configuration file, so can connect to a server without a password
file { 'Turn off passwd auth':
ensure => 'presents',
path   => '~/.ssh/config',
line   => 'PasswordAuthentication no',
}

file { 'Declare identity file':
ensure => 'presents',
path   => '~/.ssh/config',
line   => 'IdentityFile ~/.ssh/holberton',
}
