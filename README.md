# academic

### A Jekyll theme for academia

## Installation

Add this line to your Jekyll site's `Gemfile`:

```ruby
gem "academic"
```

And add this line to your Jekyll site's `_config.yml`:

```yaml
theme: academic
```

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install academic

## Usage

### Layouts

The following sections describe usage instructions for this Jekyll theme,including available layouts, includes, sass and/or assets.

#### People

The `_layouts/people.html` layout can be used to showcase and describe people in your research group. People are defined in the `_data/settings.yml` file, and markdown pages for each person with the `_layouts/page.html` layout can be placed in the `people` directory.

#### Publications

The `_layouts/publications` layout can be used to showcase selected publications, or the entire catalogue of publications. Direct links to the paper can be used, or a PDF copy of the paper can be served. Publications are defined in the `_data/publications.yml` file, and any PDF files that are served can be placed in the `publications` directory.

#### Courses

The `_layouts/courses` layout can be used to showcase courses that were taught in the past or are currently being taught. Courses are defined in the `_data/settings.yml` file, and markdown pages for each course with the `_layouts/page.html` layout can be placed in the `courses` directory. Related course material, such as PDF files, can also be placed in the `courses` directory in a subdirectory with the same name as the corresponding course.

#### CV

The `_layouts/cv` layout can be used to showcase a curriculum vitae. The sections of the cv are defined in the `_data/cv` directory, where each section has its own `<section>.yml` file.

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/LeNPaul/academic. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

## Development

To set up your environment to develop this theme, run `bundle install`, then run `bundle exec jekyll serve`, and open your browser at `http://localhost:4000`. This starts a Jekyll server using this theme. Make changes to the pages, documents, data, etc. like normal to test this theme's contents. As you make modifications to this theme the site will regenerate and you should see the changes in the browser after a refresh.

## License

The theme is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).
