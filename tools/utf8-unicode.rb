#!/usr/bin/ruby
STDIN.each { |line|
  line.each_codepoint { |c|
    $stdout << "U+" << c.to_s(16) << " "
  }
}
