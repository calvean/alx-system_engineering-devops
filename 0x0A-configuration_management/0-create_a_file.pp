# Create a file named school in tmp with owner and group www-data
file {'/tmp/school':
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
  mode    => '0744',
}
