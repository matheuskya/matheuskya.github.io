AUTHOR = 'Matheus Kenzo'
SITENAME = 'Matheus Kenzo'
SITEURL = ""
# HEADER_COVER="clean-blog/static/images/Clearday.jpg"

PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
THEME = "/home/matheus/projetos/personal_blog/clean-blog"
PATH = "content"

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("Github", "https://github.com/matheuskya"),
    ("Linkedin", "https://www.linkedin.com/in/matheus-kenzo-614a4120b/"),
)

DEFAULT_PAGINATION = 0

LINKEDIN_URL = "https://www.linkedin.com/in/matheus-kenzo-614a4120b/"


# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True