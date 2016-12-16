#Jekyll::Hooks.register :posts, :pre_render do |post|
#  post.content = post.content.sub "<!-- REPLACE:ME -->", <<-LIQUID
#      {{ page.content | append:"<p>test worked!</p>" }}
#  LIQUID
#end

#Jekyll::Hooks.register :posts, :pre_render do |post|
#  post.content = post.content.sub "permalink: /old/", <<-LIQUID
#    page.frontmatter | append: 'permalink: /test-worked/'
#  LIQUID
#end

require 'yaml'
thing = YAML.load_file('2016-12-14-test2.markdown')
print thing.inspect
