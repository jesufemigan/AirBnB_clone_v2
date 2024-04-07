package { 'nginx':
  ensure  => present,
  command => /usr/bin/apt
}

file { '/data/web_static/releases/test':
  ensure  => 'directory',
  recurse => true.
}

file { '/data/web_static/shared':
  ensure  => 'directory',
  recurse => true,
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => '<html><head></head><body>Holberton School</body></html>',
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test/'
}

file { '/data':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true
}

$nginx_path='/etc/nginx/sites-available/default'
exec { 'nginx config':
  command   => sed -i '/listen 80 default_server/a location /hbnb_static { alias
	  /data/web_static/current/;}' $nginx_path,
}

exec { 'nginx restart':
  path  => '/etc/init.d'
}
