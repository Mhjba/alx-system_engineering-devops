# increase limits for holberton user

# increase hard limit
exec { 'increase-hard-limit':
  command => "sed -i 's/5/4096/' /etc/security/limits.conf",
  path    => '/bin'
}
# increase soft limit
exec { 'increase-soft-limit':
  command => "sed -i 's/4/4096/' /etc/security/limits.conf",
  path    => '/bin'
}
