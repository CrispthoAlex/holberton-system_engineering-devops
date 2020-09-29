# Puppet script to fix internal server Error

file { '/var/www/html/wp-settings.php':
ensure => present,
}->
file_line { 'Replace line in wp-settings':
path    => '/var/www/html/wp-settings.php',
replace => true,
line    => "require_once( ABSPATH . WPINC . \'/class-wp-locale.php\' );",
match   => 'require_once( ABSPATH . WPINC . \'/class-wp-locale.phpp\' );',
}