#!/usr/bin/pup
# Install an especific version of flask (2.1.0)
# puppet declarative script to grab puppet-lint
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
