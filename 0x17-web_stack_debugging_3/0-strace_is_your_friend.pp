# Puppet script to fix internal server Error

exec { 'fix_internal_server_error':
command  => 'sed -i "s/class-wp-locale.phpp/class-wp-locale.php/g" /var/www/html/wp-settings.php',
provider => shell,
}