# -*- coding: utf-8 -*-

import time

# !! This is the configuration of Nikola. !! #
# !!  You should edit it to your liking.  !! #


# ! Some settings can be different in different languages.
# ! A comment stating (translatable) is used to denote those.
# ! There are two ways to specify a translatable setting:
# ! (a) BLOG_TITLE = "My Blog"
# ! (b) BLOG_TITLE = {"en": "My Blog", "es": "Mi Blog"}
# ! Option (a) is used when you don't want that setting translated.
# ! Option (b) is used for settings that are different in different languages.


# Data about this site
BLOG_AUTHOR = "Jan"  # (translatable)
BLOG_TITLE = "Blog"  # (translatable)
# This is the main URL for your site. It will be used
# in a prominent link. Don't forget the protocol (http/https)!
SITE_URL = "https://blog.jandroegehoff.de/"
# This is the URL where Nikola's output will be deployed.
# If not set, defaults to SITE_URL
# BASE_URL = "https://blog.jandroegehoff.de/"
BLOG_EMAIL = "jandroegehoff@gmail.com"
BLOG_DESCRIPTION = ""  # (translatable)

# Nikola is multilingual!
#
# Currently supported languages are:
#
# en        English
# af        Afrikaans
# ar        Arabic
# az        Azerbaijani
# bg        Bulgarian
# bs        Bosnian
# ca        Catalan
# cs        Czech [ALTERNATIVELY cz]
# da        Danish
# de        German
# el        Greek [NOT gr]
# eo        Esperanto
# es        Spanish
# et        Estonian
# eu        Basque
# fa        Persian
# fi        Finnish
# fr        French
# fur       Friulian
# gl        Galician
# he        Hebrew
# hi        Hindi
# hr        Croatian
# hu        Hungarian
# ia        Interlingua
# id        Indonesian
# it        Italian
# ja        Japanese [NOT jp]
# ko        Korean
# lt        Lithuanian
# ml        Malayalam
# mr        Marathi
# nb        Norwegian (Bokmål)
# nl        Dutch
# pa        Punjabi
# pl        Polish
# pt        Portuguese
# pt_br     Portuguese (Brazil)
# ru        Russian
# sk        Slovak
# sl        Slovene
# sq        Albanian
# sr        Serbian (Cyrillic)
# sr_latin  Serbian (Latin)
# sv        Swedish
# te        Telugu
# th        Thai
# tr        Turkish [NOT tr_TR]
# uk        Ukrainian
# ur        Urdu
# vi        Vietnamese
# zh_cn     Chinese (Simplified)
# zh_tw     Chinese (Traditional)
#
# If you want to use Nikola with a non-supported language you have to provide
# a module containing the necessary translations
# (cf. the modules at nikola/data/themes/base/messages/).
# If a specific post is not translated to a language, then the version
# in the default language will be shown instead.

# What is the default language?
DEFAULT_LANG = "en"

# What other languages do you have?
# The format is {"translationcode" : "path/to/translation" }
# the path will be used as a prefix for the generated pages location
TRANSLATIONS = {
    DEFAULT_LANG: "",
    # Example for another language:
    # "es": "./es",
}

# What will translated input files be named like?

# If you have a page something.rst, then something.pl.rst will be considered
# its Polish translation.
#     (in the above example: path == "something", ext == "rst", lang == "pl")
# this pattern is also used for metadata:
#     something.meta -> something.pl.meta

TRANSLATIONS_PATTERN = '{path}.{lang}.{ext}'

# Links for the sidebar / navigation bar.  (translatable)
# This is a dict.  The keys are languages, and values are tuples.
#
# For regular links:
#     ('https://getnikola.com/', 'Nikola Homepage')
#
# For submenus:
#     (
#         (
#             ('https://apple.com/', 'Apple'),
#             ('https://orange.com/', 'Orange'),
#         ),
#         'Fruits'
#     )
#
# WARNING: Support for submenus is theme-dependent.
#          Only one level of submenus is supported.
# WARNING: Some themes, including the default Bootstrap 4 theme,
#          may present issues if the menu is too large.
#          (in Bootstrap, the navbar can grow too large and cover contents.)
# WARNING: If you link to directories, make sure to follow
#          ``STRIP_INDEXES``.  If it’s set to ``True``, end your links
#          with a ``/``, otherwise end them with ``/index.html`` — or
#          else they won’t be highlighted when active.

NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ("https://jandroegehoff.de", "Homepage"),
        ("/archive.html", "Posts"),
        ("/rss.xml", "RSS"),
    ),
}

# Alternative navigation links. Works the same way NAVIGATION_LINKS does,
# although themes may not always support them. (translatable)
# (Bootstrap 4: right-side of navbar, Bootblog 4: right side of title)
NAVIGATION_ALT_LINKS = {
    DEFAULT_LANG: ()
}

# Name of the theme to use.
#THEME = "bootblog4"
THEME = "lanyon"

# A theme color. In default themes, it might be displayed by some browsers as
# the browser UI color (eg. Chrome on Android). Other themes might also use it
# as an accent color (the default ones don’t). Must be a HEX value.
THEME_COLOR = '#5670d4'

# Theme configuration. Fully theme-dependent. (translatable)
# Samples for bootblog4 (enabled) and bootstrap4 (commented) follow.
# bootblog4 supports: featured_large featured_small featured_on_mobile
#                     featured_large_image_on_mobile featured_strip_html sidebar
# bootstrap4 supports: navbar_light (defaults to False)
#                      navbar_custom_bg (defaults to '')

# Config for bootblog4:
THEME_CONFIG = {
    DEFAULT_LANG: {
        # Show the latest featured post in a large box, with the previewimage as its background.
        'featured_large': False,
        # Show the first (remaining) two featured posts in small boxes.
        'featured_small': False,
        # Show featured posts on mobile.
        'featured_on_mobile': True,
        # Show image in `featured_large` on mobile.
        # `featured_small` displays them only on desktop.
        'featured_large_image_on_mobile': True,
        # Strip HTML from featured post text.
        'featured_strip_html': False,
        # Contents of the sidebar, If empty, the sidebar is not displayed.
        'sidebar': ''
    }
}
# Config for bootstrap4:
# THEME_CONFIG = {
#     DEFAULT_LANG: {
#         # Use a light navbar with dark text. Defaults to False.
#         'navbar_light': False,
#         # Use a custom navbar color. If unset, 'navbar_light' sets text +
#         # background color. If set, navbar_light controls only background
#         # color. Supported values: bg-dark, bg-light, bg-primary, bg-secondary,
#         # bg-success, bg-danger, bg-warning, bg-info, bg-white, bg-transparent.
#         'navbar_custom_bg': '',
#     }
# }

# POSTS and PAGES contains (wildcard, destination, template) tuples.
# (translatable)
#
# The wildcard is used to generate a list of source files
# (whatever/thing.rst, for example).
#
# That fragment could have an associated metadata file (whatever/thing.meta),
# and optionally translated files (example for Spanish, with code "es"):
#     whatever/thing.es.rst and whatever/thing.es.meta
#
#     This assumes you use the default TRANSLATIONS_PATTERN.
#
# From those files, a set of HTML fragment files will be generated:
# cache/whatever/thing.html (and maybe cache/whatever/thing.html.es)
#
# These files are combined with the template to produce rendered
# pages, which will be placed at
# output/TRANSLATIONS[lang]/destination/pagename.html
#
# where "pagename" is the "slug" specified in the metadata file.
# The page might also be placed in /destination/pagename/index.html
# if PRETTY_URLS are enabled.
#
# The difference between POSTS and PAGES is that POSTS are added
# to feeds, indexes, tag lists and archives and are considered part
# of a blog, while PAGES are just independent HTML pages.
#
# Finally, note that destination can be translated, i.e. you can
# specify a different translation folder per language. Example:
#     PAGES = (
#         ("pages/*.rst", {"en": "pages", "de": "seiten"}, "page.tmpl"),
#         ("pages/*.md", {"en": "pages", "de": "seiten"}, "page.tmpl"),
#     )

POSTS = (
    ("posts/*.rst", "posts", "post.tmpl"),
    ("posts/*.md", "posts", "post.tmpl"),
    ("posts/*.txt", "posts", "post.tmpl"),
    ("posts/*.html", "posts", "post.tmpl"),
)
PAGES = (
    ("pages/*.rst", "pages", "page.tmpl"),
    ("pages/*.md", "pages", "page.tmpl"),
    ("pages/*.txt", "pages", "page.tmpl"),
    ("pages/*.html", "pages", "page.tmpl"),
)


# Below this point, everything is optional

# Post's dates are considered in UTC by default, if you want to use
# another time zone, please set TIMEZONE to match. Check the available
# list from Wikipedia:
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# (e.g. 'Europe/Zurich')
# Also, if you want to use a different time zone in some of your posts,
# you can use the ISO 8601/RFC 3339 format (ex. 2012-03-30T23:00:00+02:00)
TIMEZONE = "/usr/share/zoneinfo/Europe/Berlin"

# If you want to use ISO 8601 (also valid RFC 3339) throughout Nikola
# (especially in new_post), set this to True.
# Note that this does not affect DATE_FORMAT.
# FORCE_ISO8601 = False

# Date format used to display post dates. (translatable)
# Used by babel.dates, CLDR style: http://cldr.unicode.org/translation/date-time
# You can also use 'full', 'long', 'medium', or 'short'
# DATE_FORMAT = 'yyyy-MM-dd HH:mm'

# Date format used to display post dates, if local dates are used. (translatable)
# Used by Luxon: https://moment.github.io/luxon/docs/manual/formatting
# Example for presets: {'preset': True, 'format': 'DATE_FULL'}
# LUXON_DATE_FORMAT = {
#     DEFAULT_LANG: {'preset': False, 'format': 'yyyy-MM-dd HH:mm'},
# }

# Date fanciness.
#
# 0 = using DATE_FORMAT and TIMEZONE (without JS)
# 1 = using LUXON_DATE_FORMAT and local user time (JS, using Luxon)
# 2 = using a string like “2 days ago” (JS, using Luxon)
#
# Your theme must support it, Bootstrap already does.
# DATE_FANCINESS = 0

# Customize the locale/region used for a language.
# For example, to use British instead of US English: LOCALES = {'en': 'en_GB'}
# LOCALES = {}

# One or more folders containing files to be copied as-is into the output.
# The format is a dictionary of {source: relative destination}.
# Default is:
# FILES_FOLDERS = {'files': ''}
# Which means copy 'files' into 'output'

# One or more folders containing code listings to be processed and published on
# the site. The format is a dictionary of {source: relative destination}.
# Default is:
# LISTINGS_FOLDERS = {'listings': 'listings'}
# Which means process listings from 'listings' into 'output/listings'

# A mapping of languages to file-extensions that represent that language.
# Feel free to add or delete extensions to any list, but don't add any new
# compilers unless you write the interface for it yourself.
#
# The default compiler for `new_post` is the first entry in the POSTS tuple.
#
# 'rest' is reStructuredText
# 'markdown' is Markdown
# 'html' assumes the file is HTML and just copies it
COMPILERS = {
    "rest": ['.rst', '.txt'],
    "markdown": ['.md', '.mdown', '.markdown'],
    "textile": ['.textile'],
    "txt2tags": ['.t2t'],
    "bbcode": ['.bb'],
    "wiki": ['.wiki'],
    "ipynb": ['.ipynb'],
    "html": ['.html', '.htm'],
    # PHP files are rendered the usual way (i.e. with the full templates).
    # The resulting files have .php extensions, making it possible to run
    # them without reconfiguring your server to recognize them.
    "php": ['.php'],
    # Pandoc detects the input from the source filename
    # but is disabled by default as it would conflict
    # with many of the others.
    # "pandoc": ['.rst', '.md', '.txt'],
}

# Enable reST directives that insert the contents of external files such
# as "include" and "raw." This maps directly to the docutils file_insertion_enabled
# config. See: http://docutils.sourceforge.net/docs/user/config.html#file-insertion-enabled
# REST_FILE_INSERTION_ENABLED = True

# Create by default posts in one file format?
# Set to False for two-file posts, with separate metadata.
# ONE_FILE_POSTS = True

# Preferred metadata format for new posts
# "Nikola": reST comments, wrapped in a HTML comment if needed (default)
# "YAML": YAML wrapped in "---"
# "TOML": TOML wrapped in "+++"
# "Pelican": Native markdown metadata or reST docinfo fields. Nikola style for other formats.
# METADATA_FORMAT = "Nikola"

# Use date-based path when creating posts?
# Can be enabled on a per-post basis with `nikola new_post -d`.
# The setting is ignored when creating pages.
# NEW_POST_DATE_PATH = False

# What format to use when creating posts with date paths?
# Default is '%Y/%m/%d', other possibilities include '%Y' or '%Y/%m'.
# NEW_POST_DATE_PATH_FORMAT = '%Y/%m/%d'

# If this is set to True, the DEFAULT_LANG version will be displayed for
# untranslated posts.
# If this is set to False, then posts that are not translated to a language
# LANG will not be visible at all in the pages in that language.
# SHOW_UNTRANSLATED_POSTS = True

# Nikola supports logo display.  If you have one, you can put the URL here.
# Final output is <img src="LOGO_URL" id="logo" alt="BLOG_TITLE">.
# The URL may be relative to the site root.
LOGO_URL = 'https://jandroegehoff.de/images/15076013.png'

# When linking posts to social media, Nikola provides Open Graph metadata
# which is used to show a nice preview. This includes an image preview
# taken from the post's previewimage metadata field.
# This option lets you use an image to be used if the post doesn't have it.
# The default is None, valid values are URLs or output paths like
# "/images/foo.jpg"
# DEFAULT_PREVIEW_IMAGE = None

# If you want to hide the title of your website (for example, if your logo
# already contains the text), set this to False.
# SHOW_BLOG_TITLE = True

# Paths for different autogenerated bits. These are combined with the
# translation paths.

# Only include tags on the tag list/overview page if there are at least
# TAGLIST_MINIMUM_POSTS number of posts or more with every tag. Every tag
# page is still generated, linked from posts, and included in the sitemap.
# However, more obscure tags can be hidden from the tag index page.
# TAGLIST_MINIMUM_POSTS = 1

# A list of dictionaries specifying tags which translate to each other.
# Format: a list of dicts {language: translation, language2: translation2, …}
# For example:
#   [
#     {'en': 'private', 'de': 'Privat'},
#     {'en': 'work', 'fr': 'travail', 'de': 'Arbeit'},
#   ]
# TAG_TRANSLATIONS = []

# If set to True, a tag in a language will be treated as a translation
# of the literally same tag in all other languages. Enable this if you
# do not translate tags, for example.
# TAG_TRANSLATIONS_ADD_DEFAULTS = True

# Final locations are:
# output / TRANSLATION[lang] / CATEGORY_PATH / index.html (list of categories)
# output / TRANSLATION[lang] / CATEGORY_PATH / CATEGORY_PREFIX category.html (list of posts for a category)
# output / TRANSLATION[lang] / CATEGORY_PATH / CATEGORY_PREFIX category RSS_EXTENSION (RSS feed for a category)
# (translatable)
# CATEGORY_PATH = "categories"
# CATEGORY_PREFIX = "cat_"

# By default, the list of categories is stored in
#     output / TRANSLATION[lang] / CATEGORY_PATH / index.html
# (see explanation for CATEGORY_PATH). This location can be changed to
#     output / TRANSLATION[lang] / CATEGORIES_INDEX_PATH
# with an arbitrary relative path CATEGORIES_INDEX_PATH.
# (translatable)
# CATEGORIES_INDEX_PATH = "categories.html"

# If CATEGORY_ALLOW_HIERARCHIES is set to True, categories can be organized in
# hierarchies. For a post, the whole path in the hierarchy must be specified,
# using a forward slash ('/') to separate paths. Use a backslash ('\') to escape
# a forward slash or a backslash (i.e. '\//\\' is a path specifying the
# subcategory called '\' of the top-level category called '/').
CATEGORY_ALLOW_HIERARCHIES = False
# If CATEGORY_OUTPUT_FLAT_HIERARCHY is set to True, the output written to output
# contains only the name of the leaf category and not the whole path.
CATEGORY_OUTPUT_FLAT_HIERARCHY = False

# If CATEGORY_PAGES_ARE_INDEXES is set to True, each category's page will contain
# the posts themselves. If set to False, it will be just a list of links.
# CATEGORY_PAGES_ARE_INDEXES = False

# Set descriptions for category pages to make them more interesting. The
# default is no description. The value is used in the meta description
# and displayed underneath the category list or index page’s title.
# CATEGORY_DESCRIPTIONS = {
#    DEFAULT_LANG: {
#        "blogging": "Meta-blog posts about blogging.",
#        "open source": "My contributions to my many, varied, ever-changing, and eternal libre software projects."
#    },
# }

# Set special titles for category pages. The default is "Posts about CATEGORY".
# CATEGORY_TITLES = {
#    DEFAULT_LANG: {
#        "blogging": "Meta-posts about blogging",
#        "open source": "Posts about open source software"
#    },
# }

# If you do not want to display a category publicly, you can mark it as hidden.
# The category will not be displayed on the category list page.
# Category pages will still be generated.
HIDDEN_CATEGORIES = []

# A list of dictionaries specifying categories which translate to each other.
# Format: a list of dicts {language: translation, language2: translation2, …}
# See TAG_TRANSLATIONS example above.
# CATEGORY_TRANSLATIONS = []

# If set to True, a category in a language will be treated as a translation
# of the literally same category in all other languages. Enable this if you
# do not translate categories, for example.
# CATEGORY_TRANSLATIONS_ADD_DEFAULTS = True

# If no category is specified in a post, the destination path of the post
# can be used in its place. This replaces the sections feature. Using
# category hierarchies is recommended.
# CATEGORY_DESTPATH_AS_DEFAULT = False

# If True, the prefix will be trimmed from the category name, eg. if the
# POSTS destination is "foo/bar", and the path is "foo/bar/baz/quux",
# the category will be "baz/quux" (or "baz" if only the first directory is considered).
# Note that prefixes coming from translations are always ignored.
# CATEGORY_DESTPATH_TRIM_PREFIX = False

# If True, only the first directory of a path will be used.
# CATEGORY_DESTPATH_FIRST_DIRECTORY_ONLY = True

# Map paths to prettier category names. (translatable)
# CATEGORY_DESTPATH_NAMES = {
#    DEFAULT_LANG: {
#        'webdev': 'Web Development',
#        'webdev/django': 'Web Development/Django',
#        'random': 'Odds and Ends',
#    },
# }

# By default, category indexes will appear in CATEGORY_PATH and use
# CATEGORY_PREFIX. If this is enabled, those settings will be ignored (except
# for the index) and instead, they will follow destination paths (eg. category
# 'foo' might appear in 'posts/foo'). If the category does not come from a
# destpath, first entry in POSTS followed by the category name will be used.
# For this setting, category hierarchies are required and cannot be flattened.
# CATEGORY_PAGES_FOLLOW_DESTPATH = False

# If ENABLE_AUTHOR_PAGES is set to True and there is more than one
# author, author pages are generated.
# ENABLE_AUTHOR_PAGES = True

# Path to author pages. Final locations are:
# output / TRANSLATION[lang] / AUTHOR_PATH / index.html (list of authors)
# output / TRANSLATION[lang] / AUTHOR_PATH / author.html (list of posts by an author)
# output / TRANSLATION[lang] / AUTHOR_PATH / author RSS_EXTENSION (RSS feed for an author)
# (translatable)
# AUTHOR_PATH = "authors"

# If AUTHOR_PAGES_ARE_INDEXES is set to True, each author's page will contain
# the posts themselves. If set to False, it will be just a list of links.
# AUTHOR_PAGES_ARE_INDEXES = False

# Set descriptions for author pages to make them more interesting. The
# default is no description. The value is used in the meta description
# and displayed underneath the author list or index page’s title.
# AUTHOR_PAGES_DESCRIPTIONS = {
#    DEFAULT_LANG: {
#        "Juanjo Conti": "Python coder and writer.",
#        "Roberto Alsina": "Nikola father."
#    },
# }


# If you do not want to display an author publicly, you can mark it as hidden.
# The author will not be displayed on the author list page and posts.
# Tag pages will still be generated.
HIDDEN_AUTHORS = ['Guest']

# Allow multiple, comma-separated authors for a post? (Requires theme support, present in built-in themes)
# MULTIPLE_AUTHORS_PER_POST = False

# Final location for the main blog page and sibling paginated pages is
# output / TRANSLATION[lang] / INDEX_PATH / index-*.html
# (translatable)
# INDEX_PATH = ""

# Optional HTML that displayed on “main” blog index.html files.
# May be used for a greeting. (translatable)
FRONT_INDEX_HEADER = {
    DEFAULT_LANG: ''
}

# Create per-month archives instead of per-year
# CREATE_MONTHLY_ARCHIVE = False
# Create one large archive instead of per-year
# CREATE_SINGLE_ARCHIVE = False
# Create year, month, and day archives each with a (long) list of posts
# (overrides both CREATE_MONTHLY_ARCHIVE and CREATE_SINGLE_ARCHIVE)
# CREATE_FULL_ARCHIVES = False
# If monthly archives or full archives are created, adds also one archive per day
# CREATE_DAILY_ARCHIVE = False
# Create previous, up, next navigation links for archives
# CREATE_ARCHIVE_NAVIGATION = False
# Final locations for the archives are:
# output / TRANSLATION[lang] / ARCHIVE_PATH / ARCHIVE_FILENAME
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / index.html
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / MONTH / index.html
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / MONTH / DAY / index.html
# (translatable)
# ARCHIVE_PATH = ""
# ARCHIVE_FILENAME = "archive.html"

# If ARCHIVES_ARE_INDEXES is set to True, each archive page which contains a list
# of posts will contain the posts themselves. If set to False, it will be just a
# list of links.
# ARCHIVES_ARE_INDEXES = False

# URLs to other posts/pages can take 3 forms:
# rel_path: a relative URL to the current page/post (default)
# full_path: a URL with the full path from the root
# absolute: a complete URL (that includes the SITE_URL)
# URL_TYPE = 'rel_path'

# Extension for RSS feed files
# RSS_EXTENSION = ".xml"

# RSS filename base (without extension); used for indexes and galleries.
# (translatable)
# RSS_FILENAME_BASE = "rss"

# Final location for the blog main RSS feed is:
# output / TRANSLATION[lang] / RSS_PATH / RSS_FILENAME_BASE RSS_EXTENSION
# (translatable)
# RSS_PATH = ""

# Final location for the blog main Atom feed is:
# output / TRANSLATION[lang] / ATOM_PATH / ATOM_FILENAME_BASE ATOM_EXTENSION
# (translatable)
# ATOM_PATH = ""

# Atom filename base (without extension); used for indexes.
# (translatable)
ATOM_FILENAME_BASE = "feed"

# Extension for Atom feed files
# ATOM_EXTENSION = ".atom"

# Slug the Tag URL. Easier for users to type, special characters are
# often removed or replaced as well.
# SLUG_TAG_PATH = True

# Slug the Author URL. Easier for users to type, special characters are
# often removed or replaced as well.
# SLUG_AUTHOR_PATH = True

# A list of redirection tuples, [("foo/from.html", "/bar/to.html")].
#
# A HTML file will be created in output/foo/from.html that redirects
# to the "/bar/to.html" URL. notice that the "from" side MUST be a
# relative URL.
#
# If you don't need any of these, just set to []
REDIRECTIONS = []

# Presets of commands to execute to deploy. Can be anything, for
# example, you may use rsync:
# "rsync -rav --delete output/ joe@my.site:/srv/www/site"
# And then do a backup, or run `nikola ping` from the `ping`
# plugin (`nikola plugin -i ping`).  Or run `nikola check -l`.
# You may also want to use github_deploy (see below).
# You can define multiple presets and specify them as arguments
# to `nikola deploy`.  If no arguments are specified, a preset
# named `default` will be executed.  You can use as many presets
# in a `nikola deploy` command as you like.
DEPLOY_COMMANDS = {
    'default': [
        "rsync -rav --delete output/ pi@192.168.178.27:/home/pi/blog",
    ]
}


# Where the output site should be located
# If you don't use an absolute path, it will be considered as relative
# to the location of conf.py
# OUTPUT_FOLDER = 'output

# where the "cache" of partial generated content should be located
# default: 'cache'
# CACHE_FOLDER = 'cache'

# Filters to apply to the output.
# A directory where the keys are either: a file extensions, or
# a tuple of file extensions.
#
# And the value is a list of commands to be applied in order.
#
# Each command must be either:
#
# A string containing a '%s' which will
# be replaced with a filename. The command *must* produce output
# in place.
#
# Or:
#
# A python callable, which will be called with the filename as
# argument.
#
# By default, only .php files uses filters to inject PHP into
# Nikola’s templates. All other filters must be enabled through FILTERS.
#
# Many filters are shipped with Nikola. A list is available in the manual:
# <https://getnikola.com/handbook.html#post-processing-filters>
#
# from nikola import filters
# FILTERS = {
#    ".html": [filters.typogrify],
#    ".js": [filters.closure_compiler],
#    ".jpg": ["jpegoptim --strip-all -m75 -v %s"],
# }

# Executable for the "yui_compressor" filter (defaults to 'yui-compressor').
# YUI_COMPRESSOR_EXECUTABLE = 'yui-compressor'

# Executable for the "closure_compiler" filter (defaults to 'closure-compiler').
# CLOSURE_COMPILER_EXECUTABLE = 'closure-compiler'

# Executable for the "optipng" filter (defaults to 'optipng').
# OPTIPNG_EXECUTABLE = 'optipng'

# Executable for the "jpegoptim" filter (defaults to 'jpegoptim').
# JPEGOPTIM_EXECUTABLE = 'jpegoptim'

# Executable for the "html_tidy_withconfig", "html_tidy_nowrap",
# "html_tidy_wrap", "html_tidy_wrap_attr" and "html_tidy_mini" filters
# (defaults to 'tidy5').
# HTML_TIDY_EXECUTABLE = 'tidy5'

# List of XPath expressions which should be used for finding headers
# ({hx} is replaced by headers h1 through h6).
# You must change this if you use a custom theme that does not use
# "e-content entry-content" as a class for post and page contents.
# HEADER_PERMALINKS_XPATH_LIST = ['*//div[@class="e-content entry-content"]//{hx}']
# Include *every* header (not recommended):
# HEADER_PERMALINKS_XPATH_LIST = ['*//{hx}']

# File blacklist for header permalinks. Contains output path
# (eg. 'output/index.html')
# HEADER_PERMALINKS_FILE_BLACKLIST = []

# Expert setting! Create a gzipped copy of each generated file. Cheap server-
# side optimization for very high traffic sites or low memory servers.
# GZIP_FILES = False
# File extensions that will be compressed
# GZIP_EXTENSIONS = ('.txt', '.htm', '.html', '.css', '.js', '.json', '.atom', '.xml')
# Use an external gzip command? None means no.
# Example: GZIP_COMMAND = "pigz -k {filename}"
# GZIP_COMMAND = None
# Make sure the server does not return a "Accept-Ranges: bytes" header for
# files compressed by this option! OR make sure that a ranged request does not
# return partial content of another representation for these resources. Do not
# use this feature if you do not understand what this means.

# #############################################################################
# Image Gallery Options
# #############################################################################

# One or more folders containing galleries. The format is a dictionary of
# {"source": "relative_destination"}, where galleries are looked for in
# "source/" and the results will be located in
# "OUTPUT_PATH/relative_destination/gallery_name"
# Default is:
# GALLERY_FOLDERS = {"galleries": "galleries"}
# More gallery options:
# THUMBNAIL_SIZE = 180
# MAX_IMAGE_SIZE = 1280
# USE_FILENAME_AS_TITLE = True
# EXTRA_IMAGE_EXTENSIONS = []

# Use a thumbnail (defined by ".. previewimage:" in the gallery's index) in
# list of galleries for each gallery
GALLERIES_USE_THUMBNAIL = False

# Image to use as thumbnail for those galleries that don't have one
# None: show a grey square
# '/url/to/file': show the image in that url
GALLERIES_DEFAULT_THUMBNAIL = None

# If set to False, it will sort by filename instead. Defaults to True
# GALLERY_SORT_BY_DATE = True

# If set to True, EXIF data will be copied when an image is thumbnailed or
# resized. (See also EXIF_WHITELIST)
# PRESERVE_EXIF_DATA = False

# If you have enabled PRESERVE_EXIF_DATA, this option lets you choose EXIF
# fields you want to keep in images. (See also PRESERVE_EXIF_DATA)
#
# For a full list of field names, please see here:
# http://www.cipa.jp/std/documents/e/DC-008-2012_E.pdf
#
# This is a dictionary of lists. Each key in the dictionary is the
# name of a IDF, and each list item is a field you want to preserve.
# If you have a IDF with only a '*' item, *EVERY* item in it will be
# preserved. If you don't want to preserve anything in a IDF, remove it
# from the setting. By default, no EXIF information is kept.
# Setting the whitelist to anything other than {} implies
# PRESERVE_EXIF_DATA is set to True
# To preserve ALL EXIF data, set EXIF_WHITELIST to {"*": "*"}

# EXIF_WHITELIST = {}

# Some examples of EXIF_WHITELIST settings:

# Basic image information:
# EXIF_WHITELIST['0th'] = [
#    "Orientation",
#    "XResolution",
#    "YResolution",
# ]

# If you want to keep GPS data in the images:
# EXIF_WHITELIST['GPS'] = ["*"]

# Embedded thumbnail information:
# EXIF_WHITELIST['1st'] = ["*"]

# If set to True, any ICC profile will be copied when an image is thumbnailed or
# resized.
# PRESERVE_ICC_PROFILES = False

# Folders containing images to be used in normal posts or pages.
# IMAGE_FOLDERS is a dictionary of the form {"source": "destination"},
# where "source" is the folder containing the images to be published, and
# "destination" is the folder under OUTPUT_PATH containing the images copied
# to the site. Thumbnail images will be created there as well.

# To reference the images in your posts, include a leading slash in the path.
# For example, if IMAGE_FOLDERS = {'images': 'images'}, write
#
#   .. image:: /images/tesla.jpg
#
# See the Nikola Handbook for details (in the “Embedding Images” and
# “Thumbnails” sections)

# Images will be scaled down according to IMAGE_THUMBNAIL_SIZE and MAX_IMAGE_SIZE
# options, but will have to be referenced manually to be visible on the site
# (the thumbnail has ``.thumbnail`` added before the file extension by default,
# but a different naming template can be configured with IMAGE_THUMBNAIL_FORMAT).

IMAGE_FOLDERS = {'images': 'images'}

INDEXES_PRETTY_PAGE_URL = True
#
# If the following is true, a page range navigation will be inserted to indices.
# Please note that this will undo the effect of INDEXES_STATIC, as all index pages
# must be recreated whenever the number of pages changes.
SHOW_INDEX_PAGE_NAVIGATION = True

# If the following is True, a meta name="generator" tag is added to pages. The
# generator tag is used to specify the software used to generate the page
# (it promotes Nikola).
META_GENERATOR_TAG = True

# Color scheme to be used for code blocks. If your theme provides
# "assets/css/code.css" this is ignored. Set to None to disable.
# Can be any of:
# algol, algol_nu, autumn, borland, bw, colorful, default, emacs, friendly,
# fruity, igor, lovelace, manni, monokai, murphy, native, paraiso-dark,
# paraiso-light, pastie, perldoc, rrt, tango, trac, vim, vs, xcode
# This list MAY be incomplete since pygments adds styles every now and then.
# Check with list(pygments.styles.get_all_styles()) in an interpreter.
#
CODE_COLOR_SCHEME = 'monokai'

FAVICONS = (
    ("icon", "https://jandroegehoff.de/favicons/favicon.ico", "16x16"),
    ("icon", "https://jandroegehoff.de/favicons/favicon-32x32.png", "32x32"),
)

# Show teasers (instead of full posts) in indexes? Defaults to False.
INDEX_TEASERS = True

# HTML fragments with the Read more... links.
# The following tags exist and are replaced for you:
# {link}                        A link to the full post page.
# {read_more}                   The string “Read more” in the current language.
# {reading_time}                An estimate of how long it will take to read the post.
# {remaining_reading_time}      An estimate of how long it will take to read the post, sans the teaser.
# {min_remaining_read}          The string “{remaining_reading_time} min remaining to read” in the current language.
# {paragraph_count}             The amount of paragraphs in the post.
# {remaining_paragraph_count}   The amount of paragraphs in the post, sans the teaser.
# {post_title}                  The title of the post.
# {{                            A literal { (U+007B LEFT CURLY BRACKET)
# }}                            A literal } (U+007D RIGHT CURLY BRACKET)

# 'Read more...' for the index page, if INDEX_TEASERS is True (translatable)
INDEX_READ_MORE_LINK = '<p class="more"><a href="{link}">{read_more}…</a></p>'
# 'Read more...' for the feeds, if FEED_TEASERS is True (translatable)
FEED_READ_MORE_LINK = '<p><a href="{link}">{read_more}…</a> ({min_remaining_read})</p>'

# Append a URL query to the FEED_READ_MORE_LINK in Atom and RSS feeds. Advanced
# option used for traffic source tracking.
# Minimum example for use with Piwik: "pk_campaign=feed"
# The following tags exist and are replaced for you:
# {feedRelUri}                  A relative link to the feed.
# {feedFormat}                  The name of the syndication format.
# Example using replacement for use with Google Analytics:
# "utm_source={feedRelUri}&utm_medium=nikola_feed&utm_campaign={feedFormat}_feed"
FEED_LINKS_APPEND_QUERY = False

LICENSE = """
<a rel="license" href="https://creativecommons.org/licenses/by-nc/4.0/">
<img alt="Creative Commons License BY-NC"
style="border-width:0; margin-bottom:12px;"
src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png"></a>
"""

# I recommend using the Creative Commons' wizard:
# https://creativecommons.org/choose/
# LICENSE = """
# <a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
# <img alt="Creative Commons License BY-NC-SA"
# style="border-width:0; margin-bottom:12px;"
# src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png"></a>"""

# A small copyright notice for the page footer (in HTML).
# (translatable)
CONTENT_FOOTER = 'Contents &copy; {date}         <a href="mailto:{email}">{author}</a> {license}'

CONTENT_FOOTER_FORMATS = {
    DEFAULT_LANG: (
        (),
        {
            "email": BLOG_EMAIL,
            "author": BLOG_AUTHOR,
            "date": time.gmtime().tm_year,
            "license": LICENSE
        }
    )
}

# A simple copyright tag for inclusion in RSS feeds that works just
# like CONTENT_FOOTER and CONTENT_FOOTER_FORMATS
RSS_COPYRIGHT = 'Contents © {date} <a href="mailto:{email}">{author}</a> {license}'
RSS_COPYRIGHT_PLAIN = 'Contents © {date} {author} {license}'
RSS_COPYRIGHT_FORMATS = CONTENT_FOOTER_FORMATS

COMMENT_SYSTEM = ""
COMMENT_SYSTEM_ID = ""

STRIP_INDEXES = True

ROBOTS_EXCLUSIONS = ["/archive.html", "/category/*.html"]

PRETTY_URLS = True

MARKDOWN_EXTENSIONS = ['markdown.extensions.fenced_code', 'markdown.extensions.codehilite', 'markdown.extensions.extra']

# Show link to source for the posts?
SHOW_SOURCELINK = True
# Copy the source files for your pages?
COPY_SOURCES = True

# Modify the number of Post per Index Page
# Defaults to 10
# INDEX_DISPLAY_POST_COUNT = 10


# Nikola supports Twitter Card summaries, but they are disabled by default.
# They make it possible for you to attach media to Tweets that link
# to your content.
#
# Uncomment and modify to following lines to match your accounts.
# Images displayed come from the `previewimage` meta tag.
# You can specify the card type by using the `card` parameter in TWITTER_CARD.
TWITTER_CARD = {
    'use_twitter_cards': True,      # enable Twitter Cards
    'card': 'summary',              # Card type, you can also use 'summary_large_image',
                                    # see https://dev.twitter.com/cards/types
    # 'site': '@website',           # twitter nick for the website
    'creator': '@jandroegehoff',    # Username for the content creator / author.
}

# Bundle JS and CSS into single files to make site loading faster in a HTTP/1.1
# environment but is not recommended for HTTP/2.0 when caching is used.
# Defaults to True.
# USE_BUNDLES = True
USE_BUNDLES = False

# Plugins you don't want to use. Be careful :-)
# DISABLED_PLUGINS = ["render_galleries"]

# If set to True, the tags 'draft', 'mathjax' and 'private' have special
# meaning. If set to False, these tags are handled like regular tags.
USE_TAG_METADATA = False

# If set to True, a warning is issued if one of the 'draft', 'mathjax'
# and 'private' tags are found in a post. Useful for checking that
# migration was successful.
WARN_ABOUT_TAG_METADATA = False

# Templates will use those filters, along with the defaults.
# Consult your engine's documentation on filters if you need help defining
# those.
# TEMPLATE_FILTERS = {}

# Put in global_context things you want available on all your templates.
# It can be anything, data, functions, modules, etc.
GLOBAL_CONTEXT = {}

# Add functions here and they will be called with template
# GLOBAL_CONTEXT as parameter when the template is about to be
# rendered
GLOBAL_CONTEXT_FILLER = []
