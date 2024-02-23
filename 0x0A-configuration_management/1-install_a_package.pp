#!/usr/bin/pup
# an especific version of flask install (2.1.0)
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
