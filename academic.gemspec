# frozen_string_literal: true

Gem::Specification.new do |spec|
  spec.name          = "academic"
  spec.version       = "1.0.0"
  spec.authors       = ["Paul Le"]
  spec.email         = ["hello@paulle.ca"]

  spec.summary       = "A Jekyll theme for academia."
  spec.homepage      = "https://github.com/LeNPaul/academic"
  spec.license       = "MIT"

  spec.files         = `git ls-files -z`.split("\x0").select { |f| f.match(%r!^(_data|_includes|_layouts|_posts|_sass|assets|courses|people|publications|_config\.yml|contact\.md|courses\.md|cv\.md|index.md|LICENSE|people\.md|publications\.md|README)!i) }

  spec.add_runtime_dependency "jekyll", "~> 4.2"
end
